# RA, 2020-06-28

import pandas

url = "https://github.com/numpde/genesets/raw/16f1abd7b0673879d59ab9f74ff459beb86d99cf/genesets/msigdb/parsed/v7.1/genesets.json.zip"
df = pandas.read_json(url)

print(df)

