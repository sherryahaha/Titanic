#%% Modules and Files Import
import numpy as np
import pandas as pd

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

#%% Descritive Statistics & Pre-processing
# distinguish the numeric and category variables
def sort_variables(df, cate_cols):
    numeric_cols = []
    
    for col in list(df.columns):
        



# fill na
def fill_na_zero(nadata, col1, col2):
    idx = nadata[nadata[col2]==0].index
    nadata.loc[idx, col1] = 0
    return nadata


def fill_discrete_conti_na(nadata):
    i = 0
    for col in nadata.columns:
        i += 1
        if i%10 == 0:
            print(i)
        if col in ['user', 'label']:
            continue
        if nadata[col].dtype in ['int64','float64', 'int32', 'float32']:
            num = len(set(nadata[col]))
            if num < 10: # 离散型
                print(col)
                nadata[col] = nadata[col].fillna(nadata[col].mode())
                nadata[col] = nadata[col].astype(float)
            else:
                nadata[col] = nadata[col].fillna(nadata[col].median())
                nadata[col] = nadata[col].astype(float)
    return nadata  


# descriptive analysis
def descriptive_numeric(df, col):
    # input:df--data frame; col--numeric column names list
    temp = df.loc[:,col].apply(lambda x: pd.Series([x.count(), x.nunique(), x.sum(), x.mean(), x.std(), x.min(), x.max(), x.median(), x.skew(), x.kurtosis(), np.percentile(x,0.25), np.percentile(x, 0.75)], index = ['count', 'nunique', 'sum', 'mean', 'std', 'min', 'max', 'median', 'skew', 'kurtosis', 'per25', 'per75']))
    return temp
    
def descriptive_category(df, col):
    # input:df--data frame; col--category column names list
    temp = {}
    for column in col:
        temp[column] = df.loc[:,col].value_counts()
    return temp



train_df.head()
train_df.info()

