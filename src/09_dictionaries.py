"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""
import json

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append(   {
        "lat": 120,
        "lon": -11,
        "name": "Some random place"
})

# Another way
# anotherPlace = { "lat": 42, "lon": -120, "name": "a fourth place"}
# waypoints.append(anotherPlace)
# print(waypoints)

# *************How to print json data **************
# json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
#             '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

# json_object = json.loads(json_data)
# json_formatted_str = json.dumps(json_object, indent=2)
# print(json_formatted_str)
# dont forget to import json

# with open('EmployeeData.json', 'r') as json_file:
#     json_object = json.load(json_file)

#     print(json_object)
#     print(json.dumps(json_object))
#     print(json.dumps(json_object, indent=1))
#  **********************************************************


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"

# Write a loop that prints out all the field values for all the waypoints

# YOUR CODE HERE
for i, waypoint in enumerate(waypoints):
    print(f"Waypoint #{i + 1}")
    for key, value in waypoint.items():
        print(f" { key }: {value}")