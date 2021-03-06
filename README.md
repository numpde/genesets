# Gene sets

[This is the original GitHub repository](https://github.com/numpde/genesets).


## Molecular Signatures Database gene sets (MSigDB)

This repository
contains the 
[MSigDB gene sets](https://www.gsea-msigdb.org/gsea/msigdb/index.jsp) --
specifically the CC-BY subset
that includes 
the cancer hallmark, the GO gene sets, etc.,
but excludes KEGG and BIOCARTA (and AAAS/STKE) gene sets.
The aim is to provide the gene sets
in a format that is compressed, easy to load and reference,
and to assist code reproducibility.


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


### Python quick-start

This is the quickest way to inspect the gene sets in Python:

```python
import pandas as pd

url = "https://github.com/numpde/genesets/raw/53ce4ba8614d6d3ac2ca33243ea3f9f2c1f86ef5/genesets/msigdb/parsed/v7.1/genesets.json.zip"
print(pd.read_json(url))
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


### R quick-start

```R
# install.packages("jsonlite")
tmp <- tempfile()
download.file("https://github.com/numpde/genesets/raw/53ce4ba8614d6d3ac2ca33243ea3f9f2c1f86ef5/genesets/msigdb/parsed/v7.1/genesets.json.zip", tmp)
genesets <- jsonlite::stream_in(unz(tmp, "genesets.json"))  # Ignore warnings
genesets$HALLMARK_HYPOXIA$entrez
```


### Download

Download [genesets.json.zip](https://github.com/numpde/genesets/raw/53ce4ba8614d6d3ac2ca33243ea3f9f2c1f86ef5/genesets/msigdb/parsed/v7.1/genesets.json.zip).


### How to cite

As of 2020-06-28, 
the [original website](https://www.gsea-msigdb.org/gsea/msigdb)
([archive](http://archive.ph/0SuZl))
recommends citing

- Subramanian, Tamayo, et al. ([2005, PNAS 102, 15545-15550](http://www.pnas.org/cgi/content/abstract/102/43/15545))

and some of 

- Liberzon, et al. ([2011, Bionformatics](https://doi.org/10.1093/bioinformatics/btr260))
- Liberzon, et al. ([2015, Cell Systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707969/))
- the source for the gene set as listed on the [gene set page](https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp)

as appropriate.
Hence, as "the source for the gene set"
you can refer to the URL of this repository
or the specific link that you used
to download the gene sets.



## Signatures of Single Cell Identities (SCSig)

This repository
contains the 
[SCSig gene sets](https://www.gsea-msigdb.org/gsea/msigdb/supplementary_genesets.jsp#SCSig)
([archive](http://archive.ph/wROHG)),
compiled from 
`scsig.all.v1.0.1.symbols.gmt`,
`scsig.all.v1.0.1.entrez.gmt`
and
`scsig.v1.0.metadata.txt`.
The *symbols*, *entrez* and *metadata* files 
are
merged into one JSON file.


### Python quick-start

```python
import pandas as pd

url = "https://github.com/numpde/genesets/raw/c3ee17dfb92b51be82e9bd7ff292a28a801da8aa/genesets/scsig/parsed/v1.0.1/genesets.json.zip"
print(pd.read_json(url))
```

```
                                Fan_Embryonic_CTX_Big_Groups_Cajal_Retzius  ...                                Hu_Fetal_Retina_RPE
card                                                                    na  ...                                                 na
symbols                  [RELN, WFIKKN2, IGFBP5, PRPH, PCP4, LINC01133,...  ...  [PMEL, TYRP1, PTGDS, SERPINF1, TTR, TYR, ELN, ...
entrez                   [5649, 124857, 3488, 5630, 5121, 100505633, 79...  ...  [6490, 7306, 5730, 5176, 7276, 7299, 2006, 430...
organism                                                      Homo sapiens  ...                                       Homo sapiens
organ_system                                        Central Nervous System  ...                                      Visual System
pmid                                                              29867213  ...                                           31269016
publication_title        Spatial transcriptomic survey of human embryon...  ...  Dissecting the transcriptome landscape of the ...
authors                  Fan X,Dong J,Zhong S,Wei Y,Wu Q,Yan L,Yong J,S...  ...  Hu Y,Wang X,Hu B,Mao Y,Chen Y,Yan L,Yong J,Don...
geoid                                                            GSE103723  ...                                          GSE107618
exact_source             Supplementary information, Table S3: DEGs_of_8...  ...                S4 Table: DEGs of all cell classes.
external_details_url                                                        ...                                                   
chip                                                     HUMAN_GENE_SYMBOL  ...                                  HUMAN_GENE_SYMBOL
category_code                                                        SCSig  ...                                              SCSig
contributor                                               Anthony Castanza  ...                                   Anthony Castanza
contributor_org                                                MSigDB Team  ...                                        MSigDB Team
description_brief                                                           ...                   Retinal Pigment Epithelium Cells
raw_publication_members  RELN,WFIKKN2,IGFBP5,PRPH,PCP4,LINC01133,NDNF,A...  ...  PMEL,TYRP1,PTGDS,SERPINF1,TTR,TYR,ELN,TRPM1,TI...

[17 rows x 257 columns]
```

### How to cite

Refer to 
the [gsea-msigdb website](https://www.gsea-msigdb.org/gsea/msigdb/supplementary_genesets.jsp#SCSig)
([archive](http://archive.ph/wROHG))
and 
the respective publication/s of the gene set/s
from the metadata.

