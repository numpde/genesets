# RA, 2020-06-27

PARAM = {
    'files': {
        'symbols': "originals/v7.1/symbols.zip",
        'entrez': "originals/v7.1/entrez.zip",
    },

    'parsed': "parsed/v7.1",

    # Expected number of gene sets in the parsed file
    'nsets': 25249,
}


def parse(file):
    from zipfile import ZipFile
    from pandas import DataFrame

    with ZipFile(file, mode='r') as zf:
        with zf.open("") as fd:
            lines = [l.strip().split('\t') for l in fd.load().decode().split('\n') if l]
            data = [
                {
                    'name': line[0],
                    'card': line[1],
                    'genes': line[2:],
                }
                for line in lines
            ]

            return DataFrame(data).set_index('name', verify_integrity=True)


def keep_ccby(df):
    # https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp
    # See originals/readme.txt

    indices_kegg = df.index.str.startswith("KEGG_")
    indices_bioc = df.index.str.startswith("BIOCARTA_")
    assert indices_kegg.sum() and indices_bioc.sum()

    # "These gene sets have been removed in MSigDB version 7.0 and above."
    indices_st = df.index.str.startswith("ST_")
    assert all(indices_st == False)

    # Drop those
    df = df[~indices_kegg & ~indices_bioc]

    return df


def make():
    import pandas as pd
    from pathlib import Path

    dfs = [
        parse(Path(__file__).parent / file).rename(columns={'genes': name})
        for (name, file) in PARAM['files'].items()
    ]

    # Drop duplicate column 'card'
    dfs = dfs[0:1] + [df.drop(columns="card") for df in dfs[1:]]

    # Collect in one dataframe
    df = pd.concat(dfs, join='outer', axis=1, verify_integrity=True)

    # Drop dubiously licensed entries
    df = keep_ccby(df)

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


def main():
    test(save(make()))


if __name__ == '__main__':
    main()
