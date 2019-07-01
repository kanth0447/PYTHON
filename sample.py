my_dict = {}
my_dict1 = {}
index = 0
#my_list = []
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
with open('output.txt') as fileobj:
    for line in fileobj:
        my_list = []
        global index
        if index == 0:
            key = line.strip().split(None)
            my_dict[key[0]] = []
            my_dict[key[1]] = []
            my_dict[key[2]] = []
            my_dict[key[3]] = []
            my_dict[key[4]] = []
            my_dict[key[5]] = []
        else:
            value = line.strip().split(None)
            my_list.append(value[0])
            my_list.append(value[1])
            my_list.append(value[2])
            my_list.append(value[3])
            my_list.append(value[4])
            my_list.append(value[5])
            my_dict[key[0]].append(my_list[0])
            my_dict[key[1]].append(my_list[1])
            my_dict[key[2]].append(my_list[2])
            my_dict[key[3]].append(my_list[3])
            my_dict[key[4]].append(my_list[4])
            my_dict[key[5]].append(my_list[5])
        index = index + 1

print(my_dict)
# import json

# my_json = json.dumps(my_dict,sort_keys=True, indent=2)
# print(my_json)