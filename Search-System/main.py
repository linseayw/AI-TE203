import random

def binladen(element, collection, start, stop):
    if start > stop:return False#base case

    middle = (start + stop) // 2

    if collection[middle] == element:return True
    if collection[middle] > element:return binladen(element, collection, start, middle - 1)#Search left
    return binladen(element, collection, middle + 1, stop)#search right

binladen_wanted_list = sorted(random.sample(range(1, 100), 10))#generates a random list
wanted = random.randint(1,100)

print("binladen is searching for",wanted,"in",binladen_wanted_list)
print(binladen(wanted, binladen_wanted_list, 0, len(binladen_wanted_list) - 1))
