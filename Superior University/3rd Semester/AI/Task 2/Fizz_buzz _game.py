# Question 01
# FizzBuzz Game
import random
class FizzBuzz:
    def __init__(self, num):
        self.num = num
        self.score = 0
    # creating the logic for the game 
    def game_structure(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "fizzbuzz"
        elif num % 3 == 0:
            return "fizz"
        elif num % 5 == 0:
            return "buzz"
        else: 
            return ""
        
    # playing the game
    def start_game(self):
        print("..................Welcome in the Fizz_Buzz game.................. \n")
        previous_num = 0
        while True:
            random_number = random.randint(1, self.num)
            total = previous_num + random_number
            print(f"The number is : {previous_num}, {random_number} = {total}")
            user_input = input("Enter the answer is: ").strip().lower()
            check_answer = self.game_structure(total)
            if user_input == check_answer:
                print("Congragulation! Your answer is correct. Continue the game...")
                self.score += 1
                previous_num = random_number
            else:
                print(f"Wrong answer! The correct answer is {check_answer}...")
                print("Your total score is:", self.score)
                print("Game Over....")
                break

game = FizzBuzz(100)
game.start_game()