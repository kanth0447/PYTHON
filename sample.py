my_dict = {}
index = 0
my_list = []
with open('/home/teja/output.txt') as fileobj:
  for line in fileobj:
      global index
      index = 0
      if index == 0:
          key = line.strip().split(None)
          print(key)
      else:
          value = line.strip().split(None)
          my_list.append(value[0])
          my_dict[key[0]] = my_list
      index = index + 1

print(my_dict)
print("Hello")

