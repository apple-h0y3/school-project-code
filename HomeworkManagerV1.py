homework1=input
date1=input
homework2=input
date2=input
homework3=input
date3=input
homework4=input
date4=input

print("welcome to homework manager")
print("when asked for time, please only enter a number, without any text, in days. ")
print()
print(" please enter the name of your homework")
homework1=input()
print("please enter the length of time you have to finish your homework")
date1=int(input())

print(" please enter the name of your homework")
homework2=input()
print("please enter the length of time you have to finish your homework")
date2=int(input())

print(" please enter the name of your homework")
homework3=input()
print("please enter the length of time you have to finish your homework")
date3=int(input())

print(" please enter the name of your homework")
homework4=input()
print("please enter the length of time you have to finish your homework")
date4=int(input())

print()
print()


if date1<date2 and date1<date3 and date1<date4:
    print("do " + homework1 + " first")
elif date2<date1 and date2<date3 and date2<date4:
    print("do " + homework2 + " first")
elif date3<date1 and date3<date2 and date3<date4:
    print("do " + homework3 + " first")
elif date4<date1 and date4<date3 and date4<date2:
    print("do " + homework4 + " first")
else: 
    print("equal amount of time. do them in whatever order you want")







