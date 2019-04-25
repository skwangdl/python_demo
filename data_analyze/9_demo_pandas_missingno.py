import pandas as pd
import numpy as np

def demo():
    df = pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','g'], columns=['one','two','three'])
    df = df.reindex(['a','b','c','d','e','f','g'])
    print(df)
    print(df['one'].isnull())
    print(df['a':'c'].isnull())
    print(df['one'].notnull())
    print(df['a':'c'].notnull())

if __name__ == '__main__':
    demo()