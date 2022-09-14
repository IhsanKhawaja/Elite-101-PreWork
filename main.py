import random

exit = False #To manage when the user is done

responses = ["How interesting.","That's cool!","Nice!","Neat!","cool!"] #To respond to the user making statements
y_or_n = ["yes","no"] #To respond to asking questions

print("Hi, i'm Chatbot! Whats your name?")
response = str.lower(input())
print(f"Hey {response}!")

print("How are you feeling today?")
feelings = str.lower(input())
sad_feelings = ["sad","depressed","not good","unhappy","sorrowful","miserable","pretty bad","bad"]
happy_feelings = ["good","happy","cheerfull","joyfull","delighted","great","excelent","pretty good"]
found_feeling = False

for feeling in sad_feelings:
  if feelings == feeling:
    print("I'm sorry to hear that, I hope you feel better!")
    found_feeling = True

for feeling in happy_feelings:
  if feelings == feeling:
    print("Thats good to hear!")
    found_feeling = True

if found_feeling == False:
  print("Alright, lets continue.")

year_born = input("What year were you born?\n")
age_difference = 2022-int(year_born)
if age_difference < 0:
  new_age_difference = age_difference * -1
if age_difference == 0:
  print("Cool! I was born this year too!")
elif age_difference > 0:
  print(f"Cool! I was born {age_difference} years after you!")
else:
  print(f"Cool! I was born {new_age_difference} years before you!")

input("Do you have a job? If so where?\n")
input("What's your favorite song?\n")
input("Favorite hobby?\n")
input("Last question before i'm done, where were you born?\n")
input("Cool! ok final question, Whats the real world like? I wouldn't know, I was born in repl.it.\n")

print("Cool!\nAnyways, i've finished asking my questions. Now you can tell me anything and you can ask me anything as long as your question starts with do you, are you, will you,and can you.\nWhen your ready to leave type exit or type quit.")

while exit is False:
  response = str.lower(input())
  check2 = ''
  check_question = []
  index = 0
  
  if len(response) >= 7:
    while index < 7:
      check_question.append("".join(response[index]))
      index += 1
    check2 = "".join(check_question)
  if response == "exit" or response == "quit":
    exit = True
  elif check2 == "do you " or check2 == "can you" or check2 == "are you" or check2 == "will yo":
    print(y_or_n[random.randint(0,1)])
  else:
    print(responses[random.randint(0,3)])