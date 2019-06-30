my_dict = {}
index = 0
my_list = []
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
with open('output.txt') as fileobj:
    for line in fileobj:
        global index
        if index == 0:
            key = line.strip().split(None)
        else:
            value = line.strip().split(None)
            my_list.append(value[0])
            my_list1.append(value[1])
            my_list2.append(value[2])
            my_list3.append(value[3])
            my_list4.append(value[4])
            my_list5.append(value[5])
            my_dict[key[0]] = my_list
            my_dict[key[1]] = my_list1
            my_dict[key[2]] = my_list2
            my_dict[key[3]] = my_list3
            my_dict[key[4]] = my_list4
            my_dict[key[5]] = my_list5
        index = index + 1

import json

my_json = json.dumps(my_dict,sort_keys=True, indent=2)
print(my_json)