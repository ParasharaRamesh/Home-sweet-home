import pandas as pd
from utils.data_utils import duplicate, to_lower, flat_type_to_lower_case, delete_column, count_planning_areas, get_ordinality_for_flat_type, normalize_column

def clean_and_normalize(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''

    # clean dataset
    df_unnormalized = clean_dataset(df)

    # Normalize all values
    df_normalized = normalize_dataset(df_unnormalized)

    return df_normalized


def clean_dataset(df):
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
