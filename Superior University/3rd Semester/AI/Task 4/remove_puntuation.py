# Question 02
# Remove punctuation without using remove function from string

string = "Hello!, We are providing different platform for learning dsa and artificial intelligence: *'[AI]'*... Are you interested!!!"
print("The original string is: ","\n", string)
punctuation_list = '''!()-[]{};*:'",<>./?@_~'''
for i in string:
    if i in punctuation_list:
        string = string.replace(i, "")
# Now updated string
print('=============================================================')
print("The string after removing punctuation: ",'\n',string)