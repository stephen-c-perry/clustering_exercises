import pandas as pd
import numpy as pd

def summarize(df):
    shape = df.shape
    info = df.info()
    describe = df.describe()
    distributions = df.hist(figsize=(24, 10), bins=20)
    return shape, info, describe, distributions
