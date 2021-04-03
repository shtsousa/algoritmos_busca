def linear_search(my_list, key):
    for i, item in enumerate(my_list):
        if key == item:
            return True, i
        return False, -1
import random

if __name__ == '__main__':

    main_list = random.sample(range(1000), 100)
    main_key = 999
    print(f'Before {main_list}')
    print(f'After {main_list}')

    answer, index = linear_search(my_list=main_list, key=main_key)

    if answer:
        print(f'{main_key} is present at position{index}')
    else:
        print(f'{main_key} is not present in your data set{index}')

    #print(f'{main_key} {"is" if answer else "is not"}'
         # f' present in your data set')