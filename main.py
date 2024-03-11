import random
import os
import time

hiragana = {}

def lerp(a, b, t):
    if t < 0:
        t = 0
    if t > 1:
        t = 1
    return a * (1 - t) + b * t

def read_file():
    with open("deck.txt", "r", encoding = "utf-8") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            token = line.split(sep = " ")
            hiragana[token[0]] = token[1]

grace_timer = 1.5
full_timer  = 5

if __name__ == "__main__":
    read_file()
    os.system("cls")
    print("Welcome to Hiragana Practice Program")
    l = int(input("Input the start of the list you want to memorize (start from 1): "))
    l = max(1, l)
    l = min(l, len(hiragana.keys()))
    r = int(input("Input the end of the list you want to memorize (start from 1):   "))
    r = max(1, r)
    r = min(r, len(hiragana.keys()))
    test_list = list(hiragana.keys())[l - 1 : r]
    os.system("cls")
    print("Let's put your memory to the test.")
    print("Memorize these: ")
    for character in test_list:
        print(f"{character} : {hiragana[character]}")
    print(f"Answer the question in {grace_timer}s to get maximum bonus score.")
    print(f"If you don't, bonus score will decay for an additional {full_timer - grace_timer}s before losing bonus entirely.")
    os.system("pause")

    random.shuffle(test_list)
    score = 0
    bonus = 0
    crit = 0
    max_score = len(test_list)

    for char in test_list:
        os.system("cls")
        print(f"What is '{char}'?")
        start_time = time.time()
        guess = input("--> ")
        end_time = time.time()
        if (guess == hiragana[char]):
            score += 1
            duration = end_time - start_time
            bonus_value = 1
            if duration <= grace_timer:
                bonus_value = 1
                crit += 1
            else:
                bonus_value = lerp(1, 0, (duration - grace_timer) / (full_timer - grace_timer))
            print(f"That is correct! (Speed Bonus +{(bonus_value / max_score):.04f}%)")
            bonus += bonus_value
        else:
            print(f"That is incorrect! The correct answer is '{hiragana[char]}'")
        os.system("pause")
    
    os.system("cls")
    accuracy = (score / max_score) * 100 + (bonus / max_score)
    print(f"        Accuracy: {accuracy:.04f}%")
    print(f"Critical Perfect: {crit}")
    print(f"         Perfect: {score - crit}")
    print(f"            Miss: {max_score - score}")
    rank = ""
    if accuracy >= 100.5:
        rank = "[SSS+]"
    elif accuracy >= 100:
        rank = "[SSS]"
    elif accuracy >= 99.5:
        rank = "[SS+]"
    elif accuracy >= 99:
        rank = "[SS]"
    elif accuracy >= 98:
        rank = "[S+]"
    elif accuracy >= 97:
        rank = "[S]"
    elif accuracy >= 94:
        rank = "<AAA>"
    elif accuracy >= 90:
        rank = "<AA>"
    elif accuracy >= 80:
        rank = "<A>"
    elif accuracy >= 75:
        rank = "BBB"
    elif accuracy >= 70:
        rank = "BB"
    elif accuracy >= 60:
        rank = "B"
    elif accuracy >= 50:
        rank = "C"
    else:
        rank = "D"
    print(f"            Rank: {rank}")