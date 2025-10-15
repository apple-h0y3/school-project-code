import time
import random
#this generates a randomized delay between 1 and 6 seconds
reactp=random.randint(1, 6) 

#this pauses the program to allow the user to prepare
time.sleep(1)
#this lets the user initiate the test
pause1=input("ready?")
print()
#this pulls the randomized delay from line 4 and uses it as the test delay
time.sleep(reactp)
#this starts the timer 
start = time.time()
print("\x1b[38;5;50m GO \033[0m")
# this is the trigger to "stop" the timer
go=input()
#this records the "end" time
end=time.time()
#this gives us the final time
react=end-start
print("your reaction time is:")
print(react,"Seconds") 




