import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_red(c):
    return f"\033[31m{c}\033[0m"

def format_green(c):
    return f"\033[32m{c}\033[0m"

def play_round(digit_count, flash_time):
    number = random.randint(10 ** (digit_count - 1), 10 ** digit_count - 1)
    number = str(number)
    
    print("The number is:", number)
    time.sleep(flash_time)
    clear()
    print("What was the number?")
    
    while True:
        Guess = input("Type here: ")
        guess_len = len(Guess)

        if guess_len != len(number):
            print(f"Your guess is off by {format_red(abs(guess_len - digit_count))} characters")
            continue
        break
    

    character_count = 0
    correct_count = 0 
    result_string = ""
    for character in Guess: 
        target_character = number[character_count]
        formatter = format_red
        if target_character == character:
            formatter = format_green
            correct_count += 1
        result_string += formatter(character)
        character_count += 1

    print("The:  number", number)
    print("Your: answer", result_string)


    return correct_count
    

def handle_intermission():
    time.sleep(1)
    intermission_length = 3
    while intermission_length != 0:
        clear()
        print(f"Next round in {format_green(intermission_length)} seconds")
        intermission_length -= 1
        time.sleep(1)




def main(): 
    clear()
    digit_count = int(input("How many digits would you like to recall? "))
    round_total = int(input("How many rounds would you like to play? ")) 
    flash_time = ({
        "easy" : 5,
        "medium": 2,
        "hard": 0.8,
    })[input("Difficulty (Easy, Medium, Hard): ").lower()]

    total_numbers_correct = 0
    for i in range(1, round_total + 1):
        clear()
        print(f"Round {i}/{round_total}")
        numbers_correct = play_round(digit_count, flash_time)
        total_numbers_correct += numbers_correct
        
        print(f'''
Results for round {i}/{round_total}
    Correct: {numbers_correct}/{digit_count} digits

Results for game:
    Total percentage: {total_numbers_correct / (digit_count * i) * 100}%
''')
        if i != round_total:
            handle_intermission()
        
main()
