# /*******************************************************************************
#  * Title: Python Data Analysis Script
#  * Author: apple-h0y3
#  * Date: October 14, 2025
#  * Code version: v1.3
#  * Availability: 
#  ******************************************************************************/


import time
import random
#randomized delay
reactp=random.randint(1, 6) #gives us a random time for the reactions
reactp2=random.randint(1, 6)
reactp3=random.randint(1, 6)
reactp4=random.randint(1, 6)
reactp5=random.randint(1, 6)
reactp6=random.randint(1, 6)
reactp7=random.randint(1, 6)
reactp8=random.randint(1, 6)
reactp9=random.randint(1, 6)
reactp10=random.randint(1, 6)


print("Prepare for test. press enter when you see the word \x1b[38;5;50m GO \033[0m")

time.sleep(1)
pause1=input("ready?")
print()
time.sleep(reactp)#randomized pause to help us measure accurately
start = time.time()
print("\x1b[38;5;50m GO \033[0m")
go=input()# this is the trigger to "stop" the timer
end=time.time()
react=end-start #this gives us the final value
print("your reaction time is:")
print(react,"Seconds") 

#start test 2
ready2=input("start test 2?")
time.sleep(reactp2)#randomized pause to help us measure accurately
start2 = time.time()
print("\x1b[38;5;1m GO \033[0m")
go2=input()
end2=time.time()
react2=end2-start2#gives us the final value
print("your reaction time is:")
print(react2,"Seconds") 

ready3=input("start test 3?")
time.sleep(reactp3)#randomized pause to help us measure accurately, eliminates repetition in the tests
start3 = time.time()
print("\x1b[38;5;190m GO \033[0m")
go3=input()
end3=time.time()
react3=end3-start3#gives us the final value
print("your reaction time is:")
print(react3,"Seconds") 
print()
print()

ready4=input("start test 4?")
time.sleep(reactp4)#randomized pause to help us measure accurately
start4 = time.time()
print("\x1b[38;5;60m GO \033[0m")
go4=input()
end4=time.time()
react4=end4-start4#gives us the final value
print("your reaction time is:")
print(react4,"Seconds") 

time.sleep(1)
pause1=input("ready for test 5?")
time.sleep(reactp5)#randomized pause to help us measure accurately
start5 = time.time()
print("\x1b[38;5;10m GO \033[0m")
go5=input()# this is the trigger to "stop" the timer
end5=time.time()
react5=end5-start5 #this gives us the final value
print("your reaction time is:")
print(react5,"Seconds") 

time.sleep(1)
pause1=input("ready for test 6?")
time.sleep(reactp6)#randomized pause to help us measure accurately
start6 = time.time()
print("\x1b[38;5;164m GO \033[0m")
go6=input()# this is the trigger to "stop" the timer
end6=time.time()
react6=end6-start6 #this gives us the final value
print("your reaction time is:")
print(react6,"Seconds") 

time.sleep(1)
pause1=input("ready for test 7?")
time.sleep(reactp7)#randomized pause to help us measure accurately
start7 = time.time()
print("\x1b[38;5;46m GO \033[0m")
go7=input()# this is the trigger to "stop" the timer
end7=time.time()
react7=end7-start7 #this gives us the final value
print("your reaction time is:")
print(react7,"Seconds") 

time.sleep(1)
pause8=input("ready for test 8?")
time.sleep(reactp8)#randomized pause to help us measure accurately
start8 = time.time()
print("\x1b[38;5;208m GO \033[0m")
go8=input()# this is the trigger to "stop" the timer
end8=time.time()
react8=end8-start8 #this gives us the final value
print("your reaction time is:")
print(react8,"Seconds") 

time.sleep(1)
pause10=input("ready for test 9?")
time.sleep(reactp9)#randomized pause to help us measure accurately
start9 = time.time()
print("\x1b[38;5;238m GO \033[0m")
go9=input()# this is the trigger to "stop" the timer
end9=time.time()
react9=end9-start9 #this gives us the final value
print("your reaction time is:")
print(react9,"Seconds") 

time.sleep(1)
pause10=input("ready for test 10?")
time.sleep(reactp10)#randomized pause to help us measure accurately
start10 = time.time()
print("\x1b[38;5;27m GO \033[0m")
go10=input()# this is the trigger to "stop" the timer
end10=time.time()
react10=end10-start10 #this gives us the final value
print("your reaction time is:")
print(react10,"Seconds") 

reactTot =(react+react2+react3+react4+react5+react6+react7+react8+react9+react10)
reactAve=(reactTot/10)

print("Final count:")
print("Test 1 -----",react)
print("Test 2 -----",react2)
print("Test 3 -----",react3)
print("Test 4 -----",react4)
print("Test 5 -----",react5)
print("Test 6 -----",react6)
print("Test 7 -----",react7)
print("Test 8 -----",react8)
print("Test 9 -----",react9)
print("Test 10 -----",react10)
print("Total time:  ", reactTot)
print("average reaction time:")
print(reactAve,"seconds")