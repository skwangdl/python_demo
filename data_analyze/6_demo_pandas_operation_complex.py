import numpy as np
import pandas as pd

def calculate():
    d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu',
                           'Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
         'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
         'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
    df = pd.DataFrame(d)
    print(df)
    print(df.sum())
    print(df.sum(0))
    print(df.mean(1))
    print(df.std(0))
    print(df.describe())
    print(df.describe(include=['object']))
    print(df.describe(include='all'))

# 变化率
def demo_pct_change():
    s = pd.Series([1,2,3,6])
    print((s.pct_change()))
    d = {'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
         'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
    df = pd.DataFrame(d)
    print((df.pct_change()))

# 相关性
def demo_pearson_spearman_kendall():
    frame = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))
    print(frame['A'].corr(frame['B']))

# 协方差
def demo_cov():
    s1 = pd.Series(np.random.randn(10))
    s2 = pd.Series(np.random.randn(10))
    print(s1.cov(s2))
    frame = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))
    print(frame['A'].cov(frame['B']))
    print(frame.cov())

# 相关性
def demo_pearson_spearman_kendall():
    frame = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))
    print(frame['A'].corr(frame['B']))
    print(frame.corr())

# 排名统计
def demo_rank():
    s = pd.Series(np.random.randn(5), index=list('edcba'))
    # s['d'] = s['b']
    print(s)
    print(s.rank())

if __name__ == '__main__':
    # calculate()
    # demo_pct_change()
    # demo_cov()
    # demo_pearson_spearman_kendall()
    demo_rank()