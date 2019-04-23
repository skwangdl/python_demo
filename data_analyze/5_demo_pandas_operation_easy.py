import numpy as np
import pandas as pd

def get_value():
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    print(df)
    print(df.loc['20190102':'20190103', ['A', 'B']])

def get_value_quick():
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print(df.at[dates[0], 'A'])

def get_value_by_index():
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    print(df.iloc[0:5, 0:2])
    print(df.iloc[[1,4,5], [0,2]])
    print(df[df.A > 0])
    print(df[df > 0])

def filter_with_isin():
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    df['E'] = ['one', 'one', 'two', 'two', 'three', 'three']
    print(df[df['E'].isin(['one', 'three'])])

def add_delete_column_to_dateframe():
    d = {'one':pd.Series([1,2,3], index=['a','b','c']), 'two':pd.Series([4,5,6], index=['a', 'b', 'c'])}
    df = pd.DataFrame(d)
    print(df)
    df['three'] = pd.Series([7,8,9], index=['a', 'b', 'c'])
    print(df)
    df['four'] = df['three'] + df['two']
    print(df)
    del df['three']
    temp = df.pop('four')
    print(temp)

def append_drop_dateframe():
    df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
    df2 = pd.DataFrame([[5,6], [7,8]], columns=['a', 'b'])
    df = df.append(df2)
    print(df)
    df = df.drop(0)
    print(df)

if __name__ == '__main__':
    # get_value()
    # get_value_quick()
    # get_value_by_index()
    # filter_with_isin()
    # add_delete_column_to_dateframe()
    append_drop_dateframe()