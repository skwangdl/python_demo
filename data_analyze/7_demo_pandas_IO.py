import pandas as pd

def demo_pandas_io():
    df = pd.read_csv("data/test.csv", index_col=['PassengerId'])
    print(df)
    tips = df[['Pclass', 'Name']].head(5)
    print(tips)
    rs = tips[tips['Pclass'] == 2]
    print(rs)
    rs = tips.groupby('Pclass').size()
    print(rs)

if __name__ == '__main__':
    demo_pandas_io()