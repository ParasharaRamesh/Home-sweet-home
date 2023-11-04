# custom_distance_metric.pyx
from libc.math cimport sin, cos, sqrt, atan2
cimport numpy as np
cimport sklearn.metrics.pairwise as pairwise

# Define a custom distance metric
cdef double haversine_distance(double lat1, double lon1, double lat2, double lon2) nogil:
    cdef double earth_radius_km = 6371.0
    cdef double lat1_rad = lat1 * 0.01745329252
    cdef double lon1_rad = lon1 * 0.01745329252
    cdef double lat2_rad = lat2 * 0.01745329252
    cdef double lon2_rad = lon2 * 0.01745329252
    cdef double dlon = lon2_rad - lon1_rad
    cdef double dlat = lat2_rad - lat1_rad
    cdef double a = (sin(dlat * 0.5)) ** 2 + cos(lat1_rad) * cos(lat2_rad) * (sin(dlon * 0.5)) ** 2
    cdef double c = 2 * atan2(sqrt(a), sqrt(1 - a))
    cdef double distance = earth_radius_km * c
    return distance * 1000.0

cpdef custom_distance_with_haversine(np.ndarray[double, ndim=1] X1, np.ndarray[double, ndim=1] X2) nogil:
    cdef int i
    cdef int lat_long_indices[2]
    cdef int remaining_indices[42]
    cdef double lat_X1, long_X1, lat_X2, long_X2
    cdef double haversine_dist
    cdef np.ndarray[double, ndim=2] X1_rem, X2_rem
    cdef np.ndarray[double, ndim=2] euclidean_dist
    cdef double combined_dist
    cdef int idx
    cdef bint found = False

    # Populate the indices
    lat_long_indices[0] = 4
    lat_long_indices[1] = 5

    remaining_len = 0
    for i in range(len(X1)):
        idx = i
        for lat_long_idx in lat_long_indices:
            if idx == lat_long_idx:
                found = True
                break

        if not found:
            remaining_indices.append(idx)
            remaining_len += 1

    # Calculate the Haversine distance for latitude and longitude columns
    lat_X1, long_X1 = X1[lat_long_indices[0]], X1[lat_long_indices[1]]
    lat_X2, long_X2 = X2[lat_long_indices[0]], X2[lat_long_indices[1]]
    haversine_dist = haversine_distance(lat_X1, long_X1, lat_X2, long_X2) / 1000.0

    # Calculate the Euclidean distance for all columns
    X1_rem = np.empty((1, remaining_len), dtype=np.double)
    X2_rem = np.empty((1, remaining_len), dtype=np.double)

    for i in range(remaining_len):
        X1_rem[0, i] = X1[remaining_indices[i]]
        X2_rem[0, i] = X2[remaining_indices[i]]

    euclidean_dist = pairwise.pairwise_distances(X1_rem, X2_rem, metric='euclidean')

    # Combine the two distance matrices
    combined_dist = euclidean_dist[0, 0] + haversine_dist

    return combined_dist  # Return a C-level buffer view
