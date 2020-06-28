# RA, 2020-06-28

import pandas

url = "https://github.com/numpde/genesets/raw/6b506a98045d3f1a71fcb0040df861c220cb13e2/genesets/data/parsed/v7.1/genesets.zip"
df = pandas.read_json(url)

print(df)
