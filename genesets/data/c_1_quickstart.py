# RA, 2020-06-28

url = "https://github.com/numpde/genesets/raw/master/genesets/data/parsed/v7.1/genesets.zip"

import pandas
df = pandas.read_json(url)

print(df)
