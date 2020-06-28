import json
from zipfile import ZipFile

with ZipFile("parsed/v7.1/genesets.zip") as zf:
    with zf.open("genesets.json") as fd:
        genesets = json.load(fd)

print(genesets['HALLMARK_DNA_REPAIR'])
