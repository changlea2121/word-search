import string

with open("text.txt", "r") as f:
   lines = f.readlines()

for line_number, line in enumerate(lines):
   print(line_number, line)

index = {}
for line_number, line in enumerate(lines):
   words = line.split()
   for word in words:
      word = word.strip(string.punctuation)
      word = word.lower()

      if word in index:
         if line_number not in index[word]:
            index[word].append(line_number)
      else:
         index[word] = [line_number]

print(index)

print("Which word you want to know its row number?")
print("Enter 'quit' if you want to quit.")

user_input = input()

while (user_input != "quit"):

   if user_input in index:
      print(index[user_input])
   else:
      print("There is no such word.")

   user_input = input()
