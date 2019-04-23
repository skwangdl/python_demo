import numpy as np
import pandas as pd

def get_value():
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    print(df)
    print(df.loc['20190102':'20190103', ['A', 'B']])

if __name__ == '__main__':
    get_value()
