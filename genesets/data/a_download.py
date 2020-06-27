# RA, 2020-06-27

PARAM = {
    'urls': {
        'symbols': "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/7.1/msigdb.v7.1.symbols.gmt",
        'entrez': "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/7.1/msigdb.v7.1.entrez.gmt",
    },

    'download_to': "originals/v7.1",
}


def download(url, file):
    from json import dumps as stringify
    from shutil import copyfileobj
    from zipfile import ZipFile, ZIP_DEFLATED as COMPRESSION
    from pathlib import Path
    from datetime import datetime, timezone
    from contextlib import closing
    from urllib.request import urlopen

    file = Path(file).with_suffix(".zip")
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.exists():
        print(F"{file.name} exists -- skipping download")
    else:
        with closing(urlopen(url=url)) as rd:
            with ZipFile(file, mode='w', compression=COMPRESSION, compresslevel=9) as zf:
                with zf.open("", mode='w') as fd:
                    copyfileobj(rd, fd)
                with zf.open("meta", mode='w') as fd:
                    meta = {
                        'source': url,
                        'datetime': datetime.now(tz=timezone.utc).isoformat(sep=' '),
                    }
                    fd.write(stringify(meta).encode())

        print(F"{file.name} downloaded")


def download_all():
    from pathlib import Path
    for (name, url) in PARAM['urls'].items():
        download(url, (Path(__file__).parent / PARAM['download_to']) / name)


def main():
    print("Downloading...")
    download_all()


if __name__ == '__main__':
    main()
