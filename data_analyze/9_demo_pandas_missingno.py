import pandas as pd
import numpy as np

def demo_isnull_notnull_calculator():
    df = pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','g'], columns=['one','two','three'])
    df = df.reindex(['a','b','c','d','e','f','g'])
    print(df)
    print(df['one'].isnull())
    print(df['a':'c'].isnull())
    print(df['one'].notnull())
    print(df['a':'c'].notnull())
    # Nan不被当做0处理，自动跳过
    print(df['one'].sum())

def demo_all_nan():
    # 计算时遇到Nan时跳过， Nan相加为Nan
    df = pd.DataFrame(index=[1,2,3,4,5], columns=['one', 'two'])
    print(df)
    print(df['one'].sum())

def demo_fillna():
    df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'g'], columns=['one', 'two', 'three'])
    df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(df)
    print(df.fillna(0))

def demo_pad_fill_back_fill_dropna():
    df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'g'], columns=['one', 'two', 'three'])
    df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(df)
    print(df.fillna(method='pad'))
    print(df.fillna(method='bfill'))
    print(df.dropna())

def demo_replace():
    df = pd.DataFrame({'one':[10,20,50],'two':[60,70,90]})
    print(df)
    print(df.replace({50:5000, 90:9000}))

if __name__ == '__main__':
    # demo_isnull_notnull_calculator()
    # demo_all_nan()
    # demo_fillna()
    # demo_pad_fill_back_fill_dropna()
    demo_replace()