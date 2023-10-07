import pandas as pd
from utils.data_utils import *


def normalize_column(df, col_name):
    '''
    Perform min max normalization to get it in range of 0-1

    :param df:
    :param col_name:
    :return:
    '''
    # Apply the min-max scaling function to the specified column
    df[col_name] = min_max_scaling(df[col_name])
    return df

def duplicate(df):
    """Removes duplicates from dataset

    Args:
        df (pandas dataframe): dataset

    Returns:
        df : Dataframe after removing duplicate entries
    """    ''''''

    exact_duplicates = df[df.duplicated(keep='first')]
    print("Number of duplicates = ", len(exact_duplicates))
    print("Number of rows before duplicate deletion = ", len(df))
    df = df.drop_duplicates(keep="first")
    print("Number of rows after duplicate deletion = ", len(df))
    return df


def delete_column(df, col_name):
    """Deletes col_name from df

    Args:
        df (pandas dataframe): df from which col_name has to be removed
        col_name (column name): The column which has to be removed

    Returns:
        df: Dataframe after removing column 
    """
    print(f"Number of columns BEFORE {col_name} column deletion = {df.shape[1]}")
    df = df.drop(col_name, axis=1)
    print(f"Number of columns AFTER {col_name} column deletion = {df.shape[1]}")
    return df


def to_lower(df):
    """Converts all values to lower case

    Args:
        df (pandas dataframe): df which is to be normalized

    Returns:
        df: Dataframe conatining values after converting all values to lower case.
    """    ''''''
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    return df


def flat_type_to_lower_case(df):
    """Normalize flat_type column. Replace the string with the number of rooms.
       Eg "3-rooms" will be "3".
        only for "Executive" type we will replace it with an ordinal value of 6

    Args:
        df (pandas dataframe): df which is to be normalized for the flat_type column

    Returns:
        df: Dataframe after normalizing for flat_type 
    """    ''''''
    df['flat_type'] = df['flat_type'].apply(lambda value: '6' if value[0] == 'e' else value[0])
    return df


def count_planning_areas(df):
    """Prints number of `planning_areas` values which are subset of `town` column

    Args:
        df (pandas dataframe): df which is to be summarized for planning_areas column
    """    ''''''
    count = 0
    for row in df.itertuples():
        if (row.planning_area in row.town):
            count += 1
    print("Number of rows which have `planning_area` as a subset of `town` = ", count)


def get_ordinality_for_flat_type(df):
    '''
    Assign an ordinality for the flat_type column

    :param df:
    :return:
    '''
    #TODO. need to implement this ordinality
    return df


def clean_and_normalize(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    # remove duplicates
    df_no_duplicate = duplicate(df)

    # convert to lower case
    df_elevation_to_lower_case = to_lower(df_no_duplicate)
    df_flat_type_lower_case = flat_type_to_lower_case(df_elevation_to_lower_case)

    # delete columns
    df_elevation_delete = delete_column(df_flat_type_lower_case, "elevation")
    df_furnished_delete = delete_column(df_elevation_delete, "furnished")
    count_planning_areas(df_furnished_delete)
    df_elevation_delete = delete_column(df_furnished_delete, "planning_area")
    df_block_delete = delete_column(df_elevation_delete, "block")
    df_street_name_delete = delete_column(df_block_delete, "street_name")
    df_delete = df_street_name_delete

    # convert all date time to unix
    # Convert the 'date' column to a datetime object with day set to 01
    df_delete['rent_approval_date'] = pd.to_datetime(df_delete['rent_approval_date'] + '-01', format='%Y-%m-%d')

    # Convert the datetime objects to Unix timestamps in seconds
    df_delete['rent_approval_date'] = (df_delete['rent_approval_date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)

    # Find out ordinality order for flat_type
    df_flat_type_ordinality = get_ordinality_for_flat_type(df_delete)
    df_unnormalized = df_flat_type_ordinality

    # Normalize all values
    df_unnormalized = normalize_column(df_unnormalized, "rent_approval_date")
    df_unnormalized = normalize_column(df_unnormalized, "floor_area_sqm")
    df_unnormalized = normalize_column(df_unnormalized, "lease_commence_date")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_existing_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_planned_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_school")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_mall")
    df_unnormalized = normalize_column(df_unnormalized, "coe_price_indicator")
    df_normalized = normalize_column(df_unnormalized, "stock_price")

    print("Number of rows after cleaning = ", len(df_normalized))
    print("Number of columns after cleaning = ", df_normalized.shape[1])
    return df_normalized
