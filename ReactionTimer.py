import time
import random
reactp=random.randint(1, 10) #gives us a random time for the reactions
reactp2=random.randint(1, 10)
reactp3=random.randint(1, 10)
def reaction_timer():
 time.sleep(1)
print("Prepare for test. press enter when you see the word \x1b[38;5;50m GO \033[0m")

time.sleep(1)
pause1=input("ready?")
time.sleep(reactp)#randomized pause to help us measure accurately
start = time.time()
print("     \x1b[38;5;50m GO \033[0m")
go=input()# this is the trigger to "stop" the timer
end=time.time()
react=end-start #this gives us the final value
print("your reaction time is:")
print(react,"Seconds") 

#start test 2
ready2=input("start test 2?")
time.sleep(reactp2)#randomized pause to help us measure accurately
start2 = time.time()
print("     \x1b[38;5;1m GO \033[0m")
go2=input()
end2=time.time()
react2=end2-start2#gives us the final value
print("your reaction time is:")
print(react2,"Seconds") 

ready3=input("start test 3?")
time.sleep(reactp3)#randomized pause to help us measure accurately
start3 = time.time()
print("     \x1b[38;5;190m GO \033[0m")
go3=input()
end3=time.time()
react3=end3-start3#gives us the final value
print("your reaction time is:")
print(react3,"Seconds") 
print()
print()
reactAve = (react+react2+react3)/3
print("Final count:")
print("Test 1 -----",react)
print("Test 2 -----",react2)
print("Test 3 -----",react3)
print("average reaction time:")
print(reactAve,"seconds")
