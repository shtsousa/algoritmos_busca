def linear_search(my_list, key): #Busca Sequêncial
    for i, item in enumerate(my_list):
        if key == item:
            return True, i
        return False, -1

#main
    list_main = random.sample(range(1000), 100)
    key_main = 152
    print(f'Before {list_main}')
    print(f'After {list_main}')

    answer, index = linear_search(my_list=list_main, key=key_main)

    if answer:
        #index +1 > cuz data sets in python start with index 0
        print(f'{key_main} is present at position{index + 1}')
        print(f'Index of key:{list_main.index(key_main)}')
    else:
        print(f'{key_main} is not present in your data set{index}')

import random

def binary_search(list_fun, key): #Busca binária
    start = 0
    finish = len(list_fun) - 1
    while start < finish:
        middle = (start+finish) //2
        if key < list_fun[middle]:
            finish = middle -1
        elif key > list_fun[middle]:
            start = middle +1
        else:
            return True

if __name__ == '__main__':

    key_main = 34
    list_main = random.sample(range(1000), 100)
    print(f'Before:{list_main}')
    list_main.sort()
    print(f'After:{list_main}')
    answer = binary_search(key=key_main, list_fun=list_main)

    if answer:
        #index +1 > cuz data sets in python start with index 0
        print(f'{key_main} is present at position')
        print(f'Index of key:{list_main.index(key_main)}')
    else:
        print(f'{key_main} is not present in your data set')