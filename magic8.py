import random
name = "Johny"
question = "Is it going to be a good life?"
if name == "johnny":
  print(name, "asks : " + question)
elif len(question) == 0:
  print("you did not ask a Question! "  )
else:
  print("Question : " + question)

answer = ""
random_number = random.randint(1, 9)
# print("random_number:" + str(random_number))
if random_number == 1 and len(question) != 0:
  answer = "Yes - definitely."
elif random_number == 2 and len(question) != 0:
  answer = "It is decidedly so."
elif random_number == 3 and len(question) != 0:
  answer = "Without a doubt."
elif random_number == 4 and len(question) != 0:
  answer = "Reply hazy, try again."
elif random_number == 5 and len(question) != 0:
  answer ="Ask again later." 
elif random_number == 6 and len(question) != 0:
  answer = "Better not tell you now."
elif random_number == 7 and len(question) != 0:
  answer = "My sources say no"
elif random_number == 8 and len(question) != 0:
  answer = "Outlook not so good"
elif random_number == 9 and len(question) != 0:
  answer = "Very doubtful"
else:
  answer = "Error"


print( "Magic 8-Ball's answer : \n\t" + answer)
