import pandas as pd
from eda_train import *

def merge_dataframes(df_coe, df_stocks, df_train_with_locs):
    '''
    Merge all the dataframes obtained so far

    :param df_coe:
    :param df_stocks:
    :param df_train_with_locs:
    :return:
    '''
    # change the columns for date for easier merging
    df_coe["rent_approval_date"] = df_coe["date"]
    df_coe = df_coe.drop(columns=["date"])
    df_stocks["rent_approval_date"] = df_stocks["date"]
    df_stocks = df_stocks.drop(columns=["date"])

    # merge the dataframes together
    merged_df = pd.merge(df_train_with_locs, df_coe, on='rent_approval_date', how='outer')
    merged_df = pd.merge(merged_df, df_stocks, on='rent_approval_date', how='outer')

    # Drop rows where any column contains NaN values
    merged_df = merged_df.dropna()

    return merged_df

def clean(train_with_loc_path, coe_df_path, stock_df_path, output_path):
    # read all the input dfs
    df_train_with_locs = pd.read_csv(train_with_loc_path)
    df_coe = pd.read_csv(coe_df_path)
    df_stocks = pd.read_csv(stock_df_path)

    #merge dataframes
    df_dirty = merge_dataframes(df_coe, df_stocks, df_train_with_locs)

    #normalize and clean dataframe
    df_clean = clean_and_normalize(df_dirty)

    #save cleaned dataset
    df_clean.to_csv(output_path, index=False)

    return df_clean


if __name__ == '__main__':
    train_with_loc_path = "../../datasets/transformed/train_with_nearest_locations.csv"
    coe_df_path = "../../datasets/transformed/sg-coe-prices.csv"
    stock_df_path = "../../datasets/transformed/sg-stock-prices.csv"
    output_path = "../../datasets/transformed/cleaned-dataset.csv"
    merged_df = clean(train_with_loc_path, coe_df_path, stock_df_path, output_path)
    print("done")
