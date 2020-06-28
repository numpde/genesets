# Gene sets

## About

This repository contains the MSigDB gene sets -- 
specifically the CC-BY subset
that includes 
the cancer hallmark, the GO gene sets, etc.,
but excludes KEGG and BIOCARTA (and AAAS/STKE) gene sets.

Hence, this dataset is licensed 
[CC(4.0)-BY](https://creativecommons.org/licenses/by/4.0/) Broad Institute.
See 
[here](https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp)
for details
([archived url](http://archive.ph/HCO4L)).

The gene sets are provided in a 
single 
JSON file (~60MB)
compressed down to (~13MB)
with [bzip2](https://en.wikipedia.org/wiki/Bzip2).

The file was compiled from
 `msigdb.v7.1.symbols.gmt`
and
`msigdb.v7.1.entrez.gmt`
downloaded from 
the [downloads](https://www.gsea-msigdb.org/gsea/downloads.jsp)
page of MSigDB (2020-06-28).


## Python quick-start

This is the quickest way to inspect the gene sets in Python:

```python
import pandas
url = "https://github.com/numpde/genesets/raw/master/genesets/data/parsed/v7.1/genesets.zip"
df = pandas.read_json(url)
print(df)
```

```
                                         AAANWWTGC_UNKNOWN  ...                                     CTTTGT_LEF1_Q2
card     http://www.gsea-msigdb.org/gsea/msigdb/cards/A...  ...  http://www.gsea-msigdb.org/gsea/msigdb/cards/C...
symbols  [MEF2C, ATP1B1, RORA, CITED2, APP, MAP3K4, ATP...  ...  [MEF2C, AJUBA, SCN3A, RTL8A, SYNCRIP, RORB, AM...
entrez   [4208, 481, 6095, 10370, 351, 4216, 493, 2904,...  ...  [4208, 84962, 6328, 26071, 10492, 6096, 154810...
```

Note that this will not cache the downloaded file.
You can download the archive and read from disk, 
as assumed in the following example.

```python
import pandas
df = pandas.read_json("parsed/v7.1/genesets.zip")
i = 'HALLMARK_DNA_REPAIR'
print(df[i].card)
print(df[i].symbols)
print(df[i].entrez)
```

```
http://www.gsea-msigdb.org/gsea/msigdb/cards/HALLMARK_DNA_REPAIR
['POLR2H', 'POLR2A', 'POLR2G', 'POLR2E', 'POLR2J', 'POLR2F', ...]
['5437', '5430', '5436', '5434', '5439', '5435', '5432', ...]
```

The genes 
(but not necessarily the gene sets)
are in the same order as in 
the original files. 


## Download

[Download link](https://github.com/numpde/genesets/raw/master/genesets/data/parsed/v7.1/genesets.zip).
