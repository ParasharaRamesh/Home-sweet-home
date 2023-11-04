import pandas as pd
from utils.data_utils import duplicate, to_lower, ordinalize_flat_type, delete_column, count_planning_areas, get_ordinality_for_flat_type, normalize_column

def clean_and_normalize(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    #TODO.x remove

    streets = df["street_name"].value_counts() #1083
    subzones = df["subzone"].value_counts() #152
    print("done")

    # clean dataset
    df_unnormalized = clean_dataset(df)

    # Normalize all values
    df_normalized = normalize_dataset(df_unnormalized)

    return df_normalized


def clean_dataset(df):

    # 1. delete columns
    df_delete = delete_column(df, "elevation")
    df_delete = delete_column(df_delete, "furnished")
    count_planning_areas(df_delete)
    df_delete = delete_column(df_delete, "planning_area")
    df_delete = delete_column(df_delete, "block")
    df_delete = delete_column(df_delete, "street_name")

    #2. Convert all string columns to lower case
    df_lower_case = to_lower(df_delete)

    #3. Convert the datetime objects to Unix timestamps in seconds
    df_lower_case['rent_approval_date'] = pd.to_datetime(df_lower_case['rent_approval_date'] + '-01', format='%Y-%m-%d')
    df_lower_case['rent_approval_date'] = (df_lower_case['rent_approval_date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)

    #4. make flat type & flat model ordinal
    df_flat_type_lower_case = ordinalize_flat_type(df_lower_case)
    df_flat_type_ordinality = get_ordinality_for_flat_type(df_delete)

    #5. remove duplicates
    df_no_duplicate = duplicate(df_flat_type_ordinality)

    return df_flat_type_ordinality

def normalize_dataset(df_unnormalized):
    df_unnormalized = normalize_column(df_unnormalized, "rent_approval_date")
    df_unnormalized = normalize_column(df_unnormalized, "floor_area_sqm")
    df_unnormalized = normalize_column(df_unnormalized, "lease_commence_date")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_existing_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_planned_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_school")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_mall")
    df_unnormalized = normalize_column(df_unnormalized, "coe_price_indicator")
    df_normalized = normalize_column(df_unnormalized, "stock_price")
    return df_normalized
