# Question 01 
# Luhn algorithm
class Luhn:
    def __init__(self, card_number):
        self.card_number = card_number  
    # removing the last charater from the number
    def remove(self):
        self.e = self.card_number.pop()
        print("The check digit is", self.e)
    # reversing the card_number
    def reverse(self):
        self.card_number.reverse()
        print("Reverse digits is:", self.card_number)
    # even indexing 
    def even_indexing(self):
        for i in range(len(self.card_number)):
            if i%2==0:
                self.card_number[i]*=2
                if self.card_number[i]>9:
                    self.card_number[i]-=9
        print("Even-index digits is ", self.card_number)
    # checking the validity of the card_number 
    def check_valid(self):
        total = sum(self.card_number) + self.e
        if total%10 == 0:
            print("valid")
        else:
            print("Invalid")

card = Luhn([3,3,4,0,1,0,5,5,2,2,4,5,9])
card.remove()
card.reverse()
card.even_indexing()
card.check_valid()

