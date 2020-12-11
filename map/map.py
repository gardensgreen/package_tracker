# A simple graph representing a series of cities and the connections between
# them.

map = {
    "Seattle": {("San Francisco", 679)},
    "San Francisco": {("Los Angeles", 381), ("Seattle", 679), ("Denver", 474)},
    "Los Angeles": {("San Francisco", 381), ("Phoenix", 357)},
    "Phoenix": {("Los Angeles", 357), ("Denver", 586)},
    "Denver": {("Phoenix", 586), ("San Francisco", 474), ("Houston", 878), ("Kansas City", 557)},
    "Kansas City": {("Denver", 557), ("Houston", 815), ("Chicago", 412), ("Nashville", 554)},
    "Houston": {("Kansas City", 815), ("Denver", 878)},
    "Chicago": {("Kansas City", 412), ("New York", 712)},
    "Nashville": {("Kansas City", 554), ("Houston", 665), ("Miami", 817)},
    "New York": {("Chicago", 712), ("Washington D.C.", 203)},
    "Washington D.C.": {("Chicago", 701), ("Nashville", 566), ("Miami", 926)},
    "Miami": {("Washington D.C.", 926), ("Houston", 483), ("Nashville", 817)}
}

679 + 381 + 357 + 586 + 557 + 412 + 712 + 203 + 926
679 + 381 + 357 + 586 + 557 + 554 + 817
679 + 474 + 557 + 554 + 817

DELIVERED = "Delivered"


def find_shortest_path(start, end):
    next_cities = [start]
    visited = set()
    distances = {start: {"distance_from_start": 0, "previous": None}}

    while next_cities and end not in visited:
        current = next_cities.pop(0)
        current_distance = distances.get(current).get("distance_from_start")
        for city, next_distance in map[current]:
            if city not in visited and (city not in distances or distances.get(city).get("distance_from_start") > (current_distance + next_distance)):
                distances[city] = {
                    "distance_from_start": current_distance + next_distance, "previous": current}
                if city not in next_cities:
                    next_cities.append(city)
        visited.add(current)
    return sift_back(distances, start, end)


def sift_back(distances, start, end):
    path = [end]
    while path[0] != start:
        current = distances.get(path[0])
        previous = current.get("previous")
        path.insert(0, previous)
    return path


# def find_shortest_path_dij(start, end):
#     # Track list of cities that we need to visit next
#     # Cities that we have fully explored
#     # Track each city we encounter, the total distance to get there, and the previous city in the route
#     # While we have cities to explore and we haven't exhausted all connections to our end city
#         # Take the first city from the list
#         # Get reference to the total distance it took to get here
#         # For each connected city, get a reference to the city name and distance of that leg of the route
#             # If we haven't fully explored that city
#             # AND we either haven't been to that city before
#             # OR getting there from this route is shorter than our previous route
#                 # Assign the updated total distance and pointer to the previous city
#                 # Add the city to the list that we need to explore if it's not already there
#         # After we explored all connected cities, add this one in to our visited set
#         # Find the city in the next_cities list that is closest to our start that we know of
#             # Put it at the beginning of the list so that on our next iteration we can take out the first element
# retirm distances


def advance_delivery(location, destination):
    print("advancing", location, destination)
    # shouldn't be called in this case
    if location == DELIVERED:
        return DELIVERED
    if location == destination:
        return DELIVERED

    path = find_shortest_path(location, destination)
    # Safe to say there is a next city if we get here
    return path[1]


# Testing
print(find_shortest_path("Seattle", "Kansas City"))
print(find_shortest_path("Seattle", "Miami"))
