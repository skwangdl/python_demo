# pandas data structure: 1. Series(1D) 2. DataFrame(2D) 3. Panel(nD)

import pandas as pd
import numpy as np

def demo_series():
    s = pd.Series([1,4,5,3, np.nan, 'kepler'])
    print(s)

def demo_dateFrame():
    dates = pd.date_range('20190301', periods=7)
    df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
    print(df)
    print('df index:')
    print(df.index)
    print('df columns:')
    print(df.columns)
    print('df values:')
    print(df.values)
    print('df describe')
    print(df.describe())
    print('df T')
    print(df.T)

def demo_dateFrame_with_map():
    df2 = pd.DataFrame({'A':1, 'B':pd.Timestamp('20190423'), 'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D':np.array([3] * 4, dtype='int32'), 'E':pd.Categorical(['test', 'train', 'test', 'train']),
                        'F':'foo'})
    print(df2)

def demo_dateFrame_sort_by_axis():
    dates = pd.date_range('20190301', periods=7)
    df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
    print(df.sort_index(axis=0, ascending=False))

def demo_dateFrame_get_value():
    dates = pd.date_range('20190301', periods=7)
    df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
    print(df)
    print(df['A'])
    print(df[0:3])
    print(df['20190301':'20190304'])

def demo_dateFrame_get_value_by_section():
    dates = pd.date_range('20190423', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df)
    print(df.loc[dates[0]])
    print(df.loc['20190424':'20190425',['A']])


if __name__ == '__main__':
    demo_series()
    demo_dateFrame()
    demo_dateFrame_with_map()
    demo_dateFrame_sort_by_axis()
    demo_dateFrame_get_value()
    demo_dateFrame_get_value_by_section()