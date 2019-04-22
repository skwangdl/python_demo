# pandas data structure: 1. Series(1D) 2. DataFrame(2D) 3. Panel(nD)

import pandas as pd
import numpy as np

def demo_series():
    s = pd.Series([1,4,5,3, np.nan, 'kepler'])
    print(s)

def demo_dateFrame():
    dates = pd.date_range('20190301', periods=7)
    print(dates)
    df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
    print(df)


if __name__ == '__main__':
    demo_series()
    demo_dateFrame()