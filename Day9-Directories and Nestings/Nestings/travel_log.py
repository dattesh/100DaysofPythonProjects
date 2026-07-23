capitals={
    'france':'Paris',
    'Germany':"Berlin"
}

# travel_log ={
#     'France':["Paris","lille","dijon"],
#     "Germany":["Stuttgart","Berlin"]
# }

# print(travel_log['France'][1])
#
# nested_list=['a','b',['c','d']]
# print(nested_list[2][1])

travel_log={
    'france':{
        'cities_visited':["Paris","lille","dijon"],
        'total_visit':12
    },
    'germany':{
        'cities_visited':["berlin","hamburg","stuttgart"],
        'total_visit':8
    }
}
print(travel_log['france']['cities_visited'][-1])
