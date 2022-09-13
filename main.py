import random

exit = False #To manage when the user is done

responses = ["How interesting.","That's cool!","Nice!","Neat!","cool!"] #To respond to the user making statements
y_or_n = ["yes","no"] #To respond to asking questions

print("Hi, i'm Chatbot! Whats your name?")
response = str.lower(input())
print(f"Hey {response}!")

print("How are you today?")
feelings = str.lower(input())
sad_feelings = ["sad","depressed","not good","unhappy","sorrowful","miserable","pretty bad"]
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

print("You can tell me anything and you can ask me anything as long as your question starts with do you, are you, and can you.\nWhen your ready to leave type exit.")

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
  if response == "exit":
    exit = True
  elif check2 == "do you " or check2 == "can you" or check2 == "are you":
    print(y_or_n[random.randint(0,1)])
  else:
    print(responses[random.randint(0,3)])