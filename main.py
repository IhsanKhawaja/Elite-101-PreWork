import random

exit = False #To manage when the user is done

responses = ["How interesting.","That's cool!","Nice!","Neat!","cool!"] #To respond to the user making statements
y_or_n = ["yes","no"] #To respond to asking questions

print("Hey, i'm chatbot!\nYou can tell me anything and you can ask me anything as long as your question starts with do you, are you, and can you.\nWhen your ready to leave type exit.")

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