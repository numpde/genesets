Gene sets
=========

About
-----

This repository contains the 
[MSigDB](https://www.gsea-msigdb.org/gsea/msigdb/collections.jsp)
gene sets --
specifically the CC-BY subset
that includes 
the cancer hallmark, the GO gene sets, etc.,
but excludes KEGG and BIOCARTA (and AAAS/STKE) gene sets.
The aim is to provide the gene sets
in a format that is easy to load 
as well as 
a reference point for better code reproducibility.


This dataset is licensed 
[CC(4.0)-BY](https://creativecommons.org/licenses/by/4.0/) Broad Institute.
See 
[here](https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp)
for details
([archived url](http://archive.ph/HCO4L)).

The gene sets are stored in a 
single 
JSON file (~60MB)
compressed down to (~13MB)
with [bzip2](https://en.wikipedia.org/wiki/Bzip2).
The file was compiled from
 `msigdb.v7.1.symbols.gmt`
and
`msigdb.v7.1.entrez.gmt`
obtained from 
the [downloads](https://www.gsea-msigdb.org/gsea/downloads.jsp)
page of MSigDB (2020-06-28).

The file contains both
the [Entrez Gene Identifiers](https://www.ncbi.nlm.nih.gov/gene) 
and
the [HUGO Gene Symbols.](https://www.genenames.org/)

Please consider 
hitting the star 
if this is useful to you.


Python quick-start
------------------

This is the quickest way to inspect the gene sets in Python:

```python
import pandas

url = "https://github.com/numpde/genesets/raw/6b506a98045d3f1a71fcb0040df861c220cb13e2/genesets/data/parsed/v7.1/genesets.zip"
df = pandas.read_json(url)

print(df)
```

```
                                         AAANWWTGC_UNKNOWN  ...                                     CTTTGT_LEF1_Q2
card     http://www.gsea-msigdb.org/gsea/msigdb/cards/A...  ...  http://www.gsea-msigdb.org/gsea/msigdb/cards/C...
symbols  [MEF2C, ATP1B1, RORA, CITED2, APP, MAP3K4, ATP...  ...  [MEF2C, AJUBA, SCN3A, RTL8A, SYNCRIP, RORB, AM...
entrez   [4208, 481, 6095, 10370, 351, 4216, 493, 2904,...  ...  [4208, 84962, 6328, 26071, 10492, 6096, 154810...
```

The above URL refers to a certain commit on GitHub and
its content is therefore immutable.
Note that this will not cache the downloaded file.
You can download the archive programmatically or manually 
and read from disk, 
as assumed in the following example.

```python
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

```

The genes 
(but not necessarily the gene sets)
are in the same order as in 
the original files. 

The following is a more Python-native way
of loading the file as a dictionary.

```python
import json
from zipfile import ZipFile

with ZipFile("parsed/v7.1/genesets.zip") as zf:
    with zf.open("genesets.json") as fd:
        genesets = json.load(fd)

print(genesets['HALLMARK_DNA_REPAIR'])
```

```
{
  "card": "http://www.gsea-msigdb.org/gsea/msigdb/cards/HALLMARK_DNA_REPAIR",
  "symbols": [
    "POLR2H",
    "POLR2A",
    "POLR2G",
    ...
  ],
  "entrez": [
    "5437",
    "5430",
    "5436",
    ...
  ]
}
```


R quick-start
-------------

```R
install.packages("jsonlite")
library(jsonlite)
download.file("https://github.com/numpde/genesets/raw/6b506a98045d3f1a71fcb0040df861c220cb13e2/genesets/data/parsed/v7.1/genesets.zip", tmp)
genesets <- jsonlite::stream_in(unz(tmp, "genesets.json"))
```


Download
--------

Download [the archive](https://github.com/numpde/genesets/raw/6b506a98045d3f1a71fcb0040df861c220cb13e2/genesets/data/parsed/v7.1/genesets.zip).
