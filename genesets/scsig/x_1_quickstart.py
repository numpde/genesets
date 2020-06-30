# RA, 2020-06-30

import pandas as pd

url = "https://github.com/numpde/genesets/raw/c3ee17dfb92b51be82e9bd7ff292a28a801da8aa/genesets/scsig/parsed/v1.0.1/genesets.json.zip"
print(pd.read_json(url))
