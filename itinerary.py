flight_route = [
    ("New Orleans", "Atlanta"),
    ("Atlanta", "London"),
    ("London", "Dubai"),
    ("Dubai", "Tokyo"),
]

def print_itinerary(route_list):
    print("--- FLIGHT ITINERARY ---")
    leg = 1
    for departure, arrival in route_list:   # tuple unpacking
        print("Leg", leg, ":", departure, "->", arrival)
        leg += 1
    print("Total legs:", len(route_list))

print_itinerary(flight_route)
