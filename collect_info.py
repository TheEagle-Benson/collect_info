import random
print("___WELCOME TO THE EAGLE'S TERMINAL___")
print(" ")
print("Enter The Required Information At Each Prompt")
print("_________________________________________________")

user_answer_key = ["first_name", "last_name", "age", "fav_color", "fav_food", "city", "shs", "fav_soccer_team"]
questions = ["first name", "surname", "age", "favorite color", "favorite food", "place of residence", "SHS you attended", "favorite soccer team"]
user_answer_storage = {}

def collect_user_info():
    idx = 0
    for question in questions:
        user_answer_storage[user_answer_key[idx]] = input(f"Enter your {question}: ")
        idx += 1
    # print(user_answer_storage)
    return user_answer_storage


def randomize_questions(qs, uky):
    idx = 0
    combined_list = list(zip(qs,uky))
    random.shuffle(combined_list)
    q, uak = zip(*combined_list)
    while idx < len(questions):
        user_answer_storage[uak[idx]] = input(f"Enter your {q[idx]}: ")
        idx += 1
    return user_answer_storage


def display_info():
    first_name = user_answer_storage[user_answer_key[0]]
    last_name =user_answer_storage[user_answer_key[1]]
    age = user_answer_storage[user_answer_key[2]]
    fav_color = user_answer_storage[user_answer_key[3]]
    fav_food = user_answer_storage[user_answer_key[4]]
    city = user_answer_storage[user_answer_key[5]]
    shs = user_answer_storage[user_answer_key[6]]
    fav_soccer_team = user_answer_storage[user_answer_key[7]]

    summary_info = f"Hello, {first_name} {last_name} \n You are {age} years old, love the color {fav_color}, enjoy eating {fav_food}, and also enjoy watching {fav_soccer_team} football match \n {shs} must be proud of you \n Enjoy your stay in {city}"
    print(summary_info)
    return first_name, summary_info

def save_to_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)
    rating = input("On a scale of 1 - 10, give a rating for the terminal survey: ")
    with open(f"{file_name}.txt", "a") as file:
        file.write(f"\nYour rating for the terminal survey is: {rating}")


def run_script():
    collect_user_info()
    file_name, file_content = display_info()
    save_file = input("Do you want to save the summary above to a text file? (Y/N): ").lower()
    if save_file == "y" or save_file == "yes":
        save_to_file(file_name, file_content)
    option = input("Do you want to re-input info? (Y/N): ").lower()
    if option == "yes" or option == "y":
        randomize_questions(questions, user_answer_key)
        file_name, file_content = display_info()
        save_file = input("Do you want to save the summary above to a text file? (Y/N): ").lower()
        if save_file == "y" or save_file == "yes":
            save_to_file(file_name, file_content)

if __name__ == "__main__":
    run_script()



