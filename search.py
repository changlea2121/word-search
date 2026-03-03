import string

with open("text.txt", "r") as f:
   text = f.read()

words = text.split()

count = {}
for word in words:
   word = word.strip(string.punctuation)
   word = word.lower()

   if word in count:
      count[word] += 1
   else:
      count[word] = 1

print(count)


print("Which word you want to count?")
print("Enter 'quit' if you want to quit.")

user_input = input()

while (user_input != "quit"):

   if user_input in count:
      print(count[user_input])
   else:
      print("There is no such word.")

   user_input = input()




