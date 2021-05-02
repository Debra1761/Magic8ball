import random

print("""
                ___
               |_?_|
                @
            *  @  *
          *  *_ *_* _*    
           *| O   O |*
            |_  -  _|
              |   |
   
      -->    FIRST TELL ME WHO ARE YOU BUDDY ? 
      -->    I WOULD LIKE a NAME PLEASE?   

""")
name = input(" Please say your name:  ")
print("\n\n\n")

if len(name) == 0:
  print("--> no name? \n -->FINE \n -->I am going to call you my mine : " )
else:
  print("-->Let me guess, your name is Gorgeous!!  \n  --> OOPS!! I mean Hello " +name+ "\n\n --> and welcome to my MAGIC 8 BALL")
print("""
            
               
                
            *  *  *
          *  *_ *_* _*    
           *| -   - |*
            |_  -  _|
              |   |


          -->ARE YOU READY!!      

""")

question = input("ASk your Question ? ")
print("\n\n\n")

if len(question) == 0:
  print("--> you did not ask a Question dumbass <3 ! ")
else:
  print("\n\n\n\n -->Seriously " +name+ " \n\n--> Is that the best you can do ? \n\n\n -->next time come up with a better Q " )
print("\n\n\n")
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
  answer = "DUMBASS!!  \n  You dint even ask me anything!"

print("""
              
                            *  *  *
                          * *_ *_* _*    
                          * |"-   -"|*
                            |_  o  _|
                              |   |

  -->YOUR DUMMER THAN YOU THINK IF A MAGIC BALL CAN SOLVE YOUR WEIRD MYSTERY LIFE 


      -->But anyways hun, here you go!    

""")

print( "Magic 8-Ball's fortune teller  : \n\n\n\n" + answer)


print("""
              
                            *  *  *
                          * *_ *_* _*    
                          * |"-   -"|*
                            |_  >  _|
                              |   |

                -->  HOPE you liked it! THATS WHAT I THOUGHT :) 

                     -->   BYE BYE BIRDIE 
                  
                                  /\   /\
                                 /  \ /  \
                                /         \
                                \         /
                                 \       /
                                  \     /
                                   \   /
                                    \ /
                         

                 --> NOW STOP ANNOYING ME WITH YOUR Qs    

""")
