# RA, 2020-06-28

import pandas

url = "https://github.com/numpde/genesets/raw/53ce4ba8614d6d3ac2ca33243ea3f9f2c1f86ef5/genesets/msigdb/parsed/v7.1/genesets.json.zip"
df = pandas.read_json(url)

print(df)
