#Write a program that allows someone to play the classic game of rock, paper, scissors against the computer.
# First, prompt the user to enter how many games should be played in a “best of” format,
# i.e. best of 5 would require someone to win 3 times, best of 9 would require someone to win 5 times, etc.
#Next, start to simulate the games. For the human player,
# you should prompt them to enter whether they would like to play rock, paper, or scissors.
# The computer player should randomly choose one of the three options.
# You should then display the result of the match and current number of wins for each player.
# If a tie occurs, it should not count towards the total number of matches played.

from random import *

def game(times):
    rock = 1
    paper = 2
    scissors = 3
    wins = int(times) - 2
    print("Winner needs "+str(wins)+" wins to be the champion")

    count = 0
    player_count = 0
    comp_count = 0
    while count !=3:
        if player_count < wins or comp_count < wins:
            user_hand = input("Enter rock, paper, or scissors?:")
            if user_hand == "rock":
                user_hand = 1
            elif user_hand == "paper":
                user_hand = 2
            elif user_hand == "scissors":
                user_hand = 3
            computer_hand = randint(1, wins)

            print(user_hand)
            print(computer_hand)

            if user_hand == computer_hand:
                count = 0
            elif user_hand > computer_hand and computer_hand !=1:
                player_count = 1 + player_count
                print(player_count)
            elif computer_hand > user_hand and user_hand !=1:
                comp_count = 1 + comp_count


    return times



times = input("How many odd games should be played?:")
print(game(times))
