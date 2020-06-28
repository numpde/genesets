# RA, 2020-06-28

import pandas as pd

df = pd.read_json("parsed/v7.1/genesets.zip")

i = 'HALLMARK_DNA_REPAIR'
print(df[i].card)
print(df[i].symbols)
print(df[i].entrez)
# http://www.gsea-msigdb.org/gsea/msigdb/cards/HALLMARK_DNA_REPAIR
# ['POLR2H', 'POLR2A', 'POLR2G', 'POLR2E', 'POLR2J', 'POLR2F', ...]
# ['5437', '5430', '5436', '5434', '5439', '5435', '5432', ...]


# All 50 "cancer hallmark" gene sets
print(df.T[[c.startswith("HALLMARK") for c in df]])
#                                                                                   card  ...                                             entrez
# HALLMARK_TNFA_SIGNALING_VIA_NFKB     http://www.gsea-msigdb.org/gsea/msigdb/cards/H...  ...  [3726, 2920, 467, 4792, 7128, 5743, 2919, 8870...
# HALLMARK_HYPOXIA                     http://www.gsea-msigdb.org/gsea/msigdb/cards/H...  ...  [5230, 5163, 2632, 5211, 226, 2026, 5236, 1039...
# HALLMARK_CHOLESTEROL_HOMEOSTASIS     http://www.gsea-msigdb.org/gsea/msigdb/cards/H...  ...  [2224, 1595, 3422, 2222, 1717, 6713, 3157, 508...
