# Question 03
# Sort words in alphabetical order without using sort function..

words = ["Zulfiqar", "Shoqat", "Hassan", "Ahasan", "Saleem"]
for i in range(0, len(words)):
    for j in range(0, len(words)):
        if words[j] > words[i]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
print(words)