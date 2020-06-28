# RA, 2020-06-28

"""
This works, but the resulting R dataset has stringified lists (?)
"""

PARAM = {
    'src': "parsed/v7.1/genesets.json.zip",
    'trg': "parsed/v7.1/genesets.rds.zip",
}


def load():
    import pandas as pd
    from pathlib import Path
    file = Path(__file__).parent / PARAM['src']
    return pd.read_json(file)


def write(df):
    import shutil
    import pyreadr
    from pathlib import Path
    from tempfile import TemporaryDirectory

    file = Path(__file__).parent / PARAM['trg']

    with TemporaryDirectory() as tmpdir:
        tmprds = (Path(tmpdir) / Path(PARAM['trg']).stem).with_suffix(".rds")
        pyreadr.write_rds(str(tmprds), df)

        with open(tmprds, 'rb') as fd_in:
            # import gzip
            # with gzip.open(file, 'wb') as fd_out:
            from zipfile import ZipFile, ZIP_BZIP2 as ZIP
            with ZipFile(file, 'w', compression=ZIP) as zf:
                with zf.open(tmprds.name, 'w') as fd_out:
                    shutil.copyfileobj(fd_in, fd_out)


def main():
    write(load())


if __name__ == '__main__':
    main()
