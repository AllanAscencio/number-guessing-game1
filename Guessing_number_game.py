import random

random_pick = random.choice(range(1, 101))
# Include an ASCII art logo.
print("""
                                       __  .__                                 ___.                 
   ____  __ __  ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  |  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/ \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/            \/     \/     \/             \/     \/       \/            \/    \/     \/       

""")


# Track the number of turns remaining.
easy_lifes = 10
hard_lifes = 5
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(f"""
Welcome to the Number Guessing Game!
Im thinking of a number between 1 and 100.
Psssst, the correct answer is {random_pick}
""")

easy_lifes = 10
hard_lifes = 5

answer_not_correct = True


def dif_easy():
    if player_answer == random_pick:
        print(f"You got it! the answer was {random_pick}")
    elif player_answer > random_pick:
        print("Number too high.")
        return easy_lifes - 1
    elif player_answer < random_pick:
        print("Number too low.")
        return easy_lifes - 1


def dif_hard():
    if player_answer == random_pick:
        print(f"You got it! the answer was {random_pick}")
    elif player_answer > random_pick:
        print("Number too high.")
        return hard_lifes - 1
    elif player_answer < random_pick:
        print("Number too low.")
        return hard_lifes - 1


difficulty = input("Choose a difficulty. Type 'easy'  or 'hard': \n").lower()

while answer_not_correct:
    if difficulty == "easy":
        if easy_lifes != None:
            print(f"You have {easy_lifes} remaining lifes  to guess the number")
            player_answer = int(input("Make a guess: \n"))
            easy_lifes = dif_easy()
            if easy_lifes == 0:
                print("You ran out of lifes, better luck next time!")
                answer_not_correct = False
    elif difficulty == "hard":
        print(f"You have {hard_lifes} remaining lifes to guess the number")
        player_answer = int(input("Make a guess: \n"))
        hard_lifes = dif_hard()
        if hard_lifes == 0:
            print("You ran out of lifes, better luck next time!")
            answer_not_correct = False



