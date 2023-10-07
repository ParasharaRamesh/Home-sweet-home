import pandas as pd


def duplicate(df):
    exact_duplicates = df[df.duplicated(keep='first')]
    print("Number of duplicates = ",len(exact_duplicates))
    print("Number of rows before duplicate deletion = ",len(df))
    df = df.drop_duplicates(keep="first")
    print("Number of rows after duplicate deletion = ",len(df))
    return df

def delete_column(df, col_name):
    print("Number of columns BEFORE elevation column deletion = ",df.shape[1])
    df = df.drop(col_name, axis=1)
    print("Number of columns AFTER elevation column deletion = ",df.shape[1])
    return df

def to_lower(df):
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    return df

def normalize_flat_type(df):
    df['flat_type']=df['flat_type'].str[0]
    return df

def count_planning_areas(df):
    count=0
    for row in df.itertuples():
        if(row.planning_area in row.town):
            count+=1
    print("number of rows which have `planning_area` as a subset of `town` = ",count)