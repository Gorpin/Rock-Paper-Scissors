import random
from os import path

all_options = ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
               'devil', 'lightning', 'gun', 'rock']
current_game_options = ["paper", "scissors", "rock"]
win_conditions = {}
user_rating = 0
user_name: str
users_data = {}


def create_win_condition_dict():
    global win_conditions
    global all_options
    for item in all_options:
        copy = all_options.copy()
        start_index = copy.index(item)
        copy.remove(item)
        end_index = int(start_index + (len(copy) / 2))
        if (start_index + (len(copy) / 2)) <= (len(copy)):
            win_conditions[item] = copy[start_index: end_index]
        else:
            win_conditions[item] = copy[start_index:] + copy[: int(end_index - len(copy))]


def gen_computer_answer(user_choice):
    random_option = random.choice(current_game_options)
    if user_choice == random_option:
        print(f"There is a draw ({random_option})")
        add_rating(50)
    elif random_option in win_conditions[user_choice]:
        print(f"Well done. The computer chose {random_option} and failed")
        add_rating(100)
    else:
        print(f"Sorry, but the computer chose {random_option}")


def print_rating():
    print(f"Your rating: {user_rating}")


def get_name():
    global user_name
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    check_file()
    create_win_condition_dict()
    get_game_options()
    main_menu()


def get_game_options():
    global current_game_options
    user_input = input()
    if user_input != "":
        user_input = user_input.replace(",", " ")
        current_game_options = user_input.split()
    print("Okay, let's start")


def check_file():
    if path.exists("rating.txt"):
        get_data_from_file()
    else:
        file = open("rating.txt", "w")
        file.close()


def get_data_from_file():
    global users_data
    global user_rating
    with open("rating.txt") as file:
        for line in file:
            arr = line.split()
            users_data[arr[0]] = int(arr[1])
            if user_name in line:
                user_rating = int(arr[1])


def add_rating(value):
    global user_rating
    user_rating += value
    users_data[user_name] = user_rating
    with open("rating.txt", "w") as file:
        for key, value in users_data.items():
            print(f"{key} {value}", sep="\n", file=file)


def main_menu():
    while (user_input := input()) != "!exit":
        if user_input in all_options:
            gen_computer_answer(user_input)
        elif user_input == "!rating":
            print_rating()
        else:
            print("Invalid input")
    print("Bye")


get_name()

