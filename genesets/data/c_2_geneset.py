# RA, 2020-06-28

import pandas
df = pandas.read_json("parsed/v7.1/genesets.zip")
i = 'HALLMARK_DNA_REPAIR'
print(df[i].card)
print(df[i].symbols)
print(df[i].entrez)
