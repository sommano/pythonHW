import sys
import time
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


def test1():
    cols = 13
    rows = 10000000
    raw_data = np.random.randint(2, size=cols * rows).reshape(rows, cols)
    col_names = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07',
                 'v08', 'v09', 'v10', 'v11', 'v12', 'outcome']
    df = pd.DataFrame(raw_data, columns=col_names)
    df['v11'] = df['v03'].apply(
        lambda x: ['t1', 't2', 't3', 't4'][np.random.randint(4)])
    df['v12'] = df['v03'].apply(lambda x: ['p1', 'p2'][np.random.randint(2)])
    return df


def test2(df):
    logit_formula = 'outcome ~ v01 + v02 + v03 + v04 + v05 + v06 + v07 + v08 + v09 + v10 + C(v11) + C(v12)'
    logit_model = smf.logit(formula=logit_formula, data=df).fit()
    print(logit_model.summary())


start_time = time.time()
df = test1()
t1 = time.time() - start_time

start_time = time.time()
test2(df)
t2 = time.time() - start_time

print(sys.version, "\nTest1: {}sec, Test2: {}sec".format(t1, t2))