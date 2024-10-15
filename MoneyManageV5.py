
ftuition=input
fcost1=input
fcost2=input
fcost3=input
fcost4=input
fcost5=input
fcost6=input
fcost7=input
fcost8=input
moneytype=input
wagehour=input

print("Welcome to Money Manage")
print("Please follow the instructions")
print()
print("please enter your currency type. eg. Canadian dollars, Japanese Yen, Euros")
moneytype=input()
print("please round all of your amounts up to the nearest whole number. eg. $1.80 = $2.00")
print()
print("enter your monthly tuition expenses")
ftuition=int(input())
print("enter your monthly food expenses")
fcost1=int(input())
print("enter your monthly bill expenses. do not include cell phone or internet")
fcost2=int(input())
print("enter your monthly cell phone bill")
fcost3=int(input())
print("enter your monthly internet cost")
fcost4=int(input())
print("enter your monthly rent")
fcost5=int(input())
print("enter your average monthly clothing and hobby expenses")
fcost6=int(input())
print("enter your average monthly expenses for parties or gifts")
fcost7=int(input())
print("enter any costs not mentioned above")
fcost8=int(input())
print("enter your hourly wage")
wagehour=int(input())
total=ftuition+fcost1+fcost2+fcost3+fcost4+fcost5+fcost6+fcost7+fcost8
print()
print()
print("all expenses in",moneytype)
print("Thank you for inputting all needed values")
print("tuition  ",ftuition,"")
print("food  ",fcost1,"")
print("bills  ",fcost2,"")
print("cell phone  ",fcost3,"")
print("internet  ",fcost4,"")
print("rent  ",fcost5,"")
print("clothing and hobby  ",fcost6,"")
print("treats ",fcost7,"")
print("other",fcost8,"")

print("total:")
print(total,moneytype)

hrMonth=total//wagehour
hrweek=hrMonth//4
if hrweek >=40:
    print("you need to work 40 hours a week to sustain this. consider cutting back on treat, hobby, and other costs")
elif:
    print("you need to work ",hrweek," hours per week to pay your bills")

print("thank you for using Money Manage")



