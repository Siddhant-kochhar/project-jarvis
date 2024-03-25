import pandas as pd
from settings import GFORM_RESPONSES_EXPORT

df = pd.read_csv(GFORM_RESPONSES_EXPORT)
print(df)

