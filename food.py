import random
import time

menu = []

def add_menu():
    food_info = open("menu.txt", 'a')
    food_name = " "
    print("if you want stop, you insert 0")
    while 1:
        food_name = input(" ")
        if food_name == "0":
            break
        else:
            food_info.write(food_name + '\n')
    food_info.close()
    
def random_num_func(length):
    random.seed(time.time())
    random_num = random.randint(0, length - 1)
    return random_num

if __name__ == "__main__":
    while 1:
        num = int(input("1. add menu    2. choice menu\n"))
        
        if num == 1:
            add_menu()
        elif num == 2:
            menu_text = open("menu.txt", 'r')
            menu = menu_text.readlines()
            button = 1
            while button:
                random_num = random_num_func(len(menu))
                print(menu[random_num])
                button = int(input("again? press 1 or not pree 0"))
            break
        else:
            print("it wrong number!! press again!!")