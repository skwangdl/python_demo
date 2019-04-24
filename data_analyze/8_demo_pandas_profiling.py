import numpy as np
import pandas as pd
import pandas_profiling as pfr

def demo_pandas_profiling():
    df = pd.read_csv("data/tcdata.csv")
    result = pfr.ProfileReport(df)
    result.to_file("data/report.html")

if __name__ == '__main__':
    demo_pandas_profiling()