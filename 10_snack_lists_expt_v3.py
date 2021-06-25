import pandas

# initialise snack lists



all_names = ['Luke', 'Scott', 'Lily', 'Zavier', 'Akinah']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

#data frame dictionary
movie_data_dict = {
    'name': all_names,
    'popcorn': popcorn,
    'water': water,
    'pita chips': pita_chips,
    'm&ms': mms,
    'orange juice': orange_juice
}

test_data = [
    [[2, 'popcorn'], [1, 'pita chips'], [1, 'orange juice']],
    [[]],
    [[1, 'water']],
    [[1, 'popcorn'], [1, 'orange juice']],
    [[1, 'm&ms'], [1, 'pita chips'], [3, 'orange juice']]
]

count = 0
for client_order in test_data:

    # assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print (snack_lists)

    # get order (hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict [to_find]
            add_list [-1] = amount

print ()
print ("popcorn: ", snack_lists[0])
print ("m&ms: ", snack_lists[1])
print ("pita chips: ", snack_lists[2])
print ("water: ", snack_lists[3])
print ("orange juice: ", snack_lists[4])
# print details...
movie_frame = pandas.DataFrame (movie_data_dict)
movie_frame = movie_frame.set_index ('name')
print (movie_frame) 