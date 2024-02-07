# Name : Fric Carlo Joseph Benedict
# Roll no : 201720702

# Intro : Defining the empty lists
cache = []
requests = []
value = 1

# Defining the function first in first out
def fifo():  
    for element1 in requests:
        if cache == []:
            print("Miss")
            cache.append(element1)
        elif element1 in cache:
            print("Hit")
        elif len(cache) > 7:
            print("Miss")
            cache.pop(0)
            cache.append(element1)
        else:
            print("Miss")       
            cache.append(element1)
    print("Requests:", requests)
    print("Cache:", cache)
    cache.clear()
    requests.clear()
counter = {}
# Defining the Least frequently used function
def counterfunc(element1):
    if element1 in counter:
        counter[element1] += 1
    else:
        counter[element1] = 1    

def sorting_list(counter):
    sorted_items = sorted(counter.items(), key=lambda item: item[1])
    sorted_values = [item[0] for item in sorted_items]
    return sorted_values

counter = {}
# Defining the Least frequently used function
def counterfunc(element1):
    if element1 in counter:
        counter[element1] += 1
    else:
        counter[element1] = 1    

def lfu():
    
    for element1 in requests:
        if cache == []:
            print("Miss")
            counterfunc(element1)
            cache.append(element1)
        elif element1 in cache:
            counterfunc(element1)
            print("Hit")
        elif len(cache) >7:
            print("Miss")
            res = sorting_list(counter)
            for i in range(len(res)):
                if res[i] not in cache:
                    pass
                else:
                    output = res[i]
                    cache.remove(output)
                    break 
            counterfunc(element1)
            cache.append(element1)
        else:
            print("Miss")
            counterfunc(element1)
            cache.append(element1)
    print("Requests:", requests)
    print("Cache:", cache)
    cache.clear()
    requests.clear()
    counter.clear()

# Getting input from the user. Input ends on entering 0.

while(True):
    while(value !=0):
        value = int(input("Enter the page you want to add" +
                "(0 to finish the request):"))
        if value != 0:
            requests.append(value)
        else:
            continue
    choice=input("Choose the Memory Eviction Method: \nPress 1 for fifo\n" +
            "Press 2 for lfu\nPress Q to quit the program\nPlease Enter:")
    match choice:
        case '1':
            fifo()
            value = 1
        case '2':
            lfu()
            value = 1
        case 'Q':
            print("Exiting the program")
            exit()
        case _:
            print('Choose the right option')
            choice=input("Choose the Memory Eviction Method: \nPress 1 for fifo\n" +
            "Press 2 for lfu\nPress Q to quit the program\nPlease Enter:")