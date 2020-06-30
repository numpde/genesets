# RA, 2020-06-27

PARAM = {
    'files': {
        'data': {
            'symbols': "originals/v1.0.1/symbols.zip",
            'entrez': "originals/v1.0.1/entrez.zip",
        },
        'meta': "originals/v1.0.1/metadata.zip",
    },

    'parsed': "parsed/v1.0.1",

    'meta_id_field': "STANDARD_NAME",

    # Expected number of gene sets in the parsed file
    'nsets': 257,
}


def parse_data(file):
    from zipfile import ZipFile
    from pandas import DataFrame

    with ZipFile(file, mode='r') as zf:
        with zf.open("") as fd:
            lines = [l.strip().split('\t') for l in fd.read().decode().split('\n') if l]
            data = [
                {
                    'name': line[0],
                    'card': line[1],
                    'genes': line[2:],
                }
                for line in lines
            ]

            return DataFrame(data).set_index('name', verify_integrity=True)


def parse_meta(file):
    from collections import defaultdict
    from zipfile import ZipFile
    from pandas import DataFrame

    with ZipFile(file, mode='r') as zf:
        with zf.open("") as fd:
            meta = defaultdict(dict)
            lines = [(l.strip() + "\t").split('\t')[0:2] for l in fd.read().decode().split('\n') if l]
            for (field, v) in lines:
                if (field == PARAM['meta_id_field']):
                    current_id = v
                    continue
                assert current_id
                meta[current_id][field.lower()] = v

            return DataFrame(meta).T


def make():
    import pandas as pd
    from pathlib import Path

    dfs = [
        parse_data(Path(__file__).parent / file).rename(columns={'genes': name})
        for (name, file) in PARAM['files']['data'].items()
    ]

    # Drop duplicate column 'card'
    dfs = dfs[0:1] + [df.drop(columns="card") for df in dfs[1:]]

    # Collect in one dataframe
    df = pd.concat(dfs, join='outer', axis=1, verify_integrity=True)

    # Append metadata
    df_meta = parse_meta(PARAM['files']['meta'])
    assert df.index.equals(df_meta.index)
    df = df.merge(right=df_meta, how='outer', left_index=True, right_index=True)

    return df


def save(df):
    import json
    from io import TextIOWrapper
    from zipfile import ZipFile, ZIP_BZIP2 as ZIP
    from pathlib import Path

    file = (Path(__file__).parent / PARAM['parsed']) / "genesets.json.zip"
    file.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(file, mode='w', compression=ZIP) as zf:
        with zf.open("genesets.json", mode='w') as fd:
            json.dump(df.T.to_dict(), TextIOWrapper(fd))

    return file


def test(file):
    # Read using pandas
    import pandas
    df = pandas.read_json(file)
    assert (len(df.columns) == PARAM['nsets'])

    # Read using json
    import json
    from io import TextIOWrapper
    from zipfile import ZipFile
    with ZipFile(file).open("genesets.json") as fd:
        data = json.load(TextIOWrapper(fd))
        assert (len(data) == PARAM['nsets'])

    return df


def main():
    df = test(save(make()))
    print(df)


if __name__ == '__main__':
    main()
