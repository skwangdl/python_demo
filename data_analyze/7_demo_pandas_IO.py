import numpy as np
import pandas as pd

def demo_pandas_io():
    df = pd.read_csv("data/test.csv", index_col=['PassengerId'])
    print(df)


if __name__ == '__main__':
    demo_pandas_io()