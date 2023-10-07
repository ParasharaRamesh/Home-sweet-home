import math

#For computing haversine distances
def haversine_distance(lat1, lon1, lat2, lon2):
    '''
    Compute the distances between 2 lat and long

    :param lat1:
    :param lon1:
    :param lat2:
    :param lon2:
    :return:
    '''
    # Radius of the Earth in kilometers
    earth_radius_km = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = earth_radius_km * c

    return distance * 1000

# For finding distances to nearest mrt
def calculate_distance_to_nearest_mrt(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_mrt_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_mrts = []
        for point2 in list2:
            lat2, lon2 = point2
            #distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mrts.append(distance)
        distance_to_closest_mrt = min(distances_to_all_mrts)
        distances_to_closest_mrt_for_all_houses.append(distance_to_closest_mrt)


    return distances_to_closest_mrt_for_all_houses

#For finding distances to nearest planned mrt
def apply_alpha(distance, years):
    '''
    apply some kind of weight to ensure that future planned MRTs have more distance ( to indicate the patience level of the customer)

    :param distance:
    :param years:
    :return:
    '''
    distance = distance + (math.exp(years) * 100)
    return distance

def calculate_distance_to_nearest_mrt_planned(lat_long_of_houses, house_rent_approval_year, lat_long_of_mrts, mrt_opening_year):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param lat_long_of_houses:
    :param house_rent_approval_year:
    :param lat_long_of_mrts:
    :param mrt_opening_year:
    :return:
    '''

    num_houses = len(lat_long_of_houses)
    num_mrt = len(lat_long_of_mrts)
    distances_to_closest_mrt_for_all_houses = []

    for house_index in range(num_houses):
        point1 = lat_long_of_houses[house_index]
        lat1, lon1 = point1
        distances_to_all_mrts = []

        for mrt_index in range(num_mrt):
            point2 = lat_long_of_mrts[mrt_index]
            lat2, lon2 = point2
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mrts.append(distance)

        min_index = distances_to_all_mrts.index(min(distances_to_all_mrts))
        distance_to_closest_mrt = distances_to_all_mrts[min_index]
        rent_approval_date = house_rent_approval_year[house_index]
        rent_approval_year = rent_approval_date.split('-')[0]
        metro_opening_year = mrt_opening_year[min_index]

        years_left_for_metro_opening = int(rent_approval_year) - int(metro_opening_year)
        distance_to_closest_mrt = apply_alpha(distance_to_closest_mrt,years_left_for_metro_opening )
        distances_to_closest_mrt_for_all_houses.append(distance_to_closest_mrt)


    return distances_to_closest_mrt_for_all_houses

# For finding distances to nearest school
def calculate_distance_to_nearest_school(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_school_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_school = []
        for point2 in list2:
            lat2, lon2 = point2
            #distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_school.append(distance)
        distance_to_closest_school = min(distances_to_all_school)
        distances_to_closest_school_for_all_houses.append(distance_to_closest_school)


    return distances_to_closest_school_for_all_houses

# For finding distances to nearest mall
def calculate_distance_to_nearest_mall(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_mall_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_mall = []
        for point2 in list2:
            lat2, lon2 = point2
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mall.append(distance)
        distance_to_closest_mall = min(distances_to_all_mall)
        distances_to_closest_mall_for_all_houses.append(distance_to_closest_mall)


    return distances_to_closest_mall_for_all_houses

# Define the min-max scaling function
def min_max_scaling(column):
    min_val = column.min()
    max_val = column.max()
    scaled_column = (column - min_val) / (max_val - min_val)
    return scaled_column