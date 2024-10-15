
goal=input
wage=input
supprt=input
print("input your monetary goal for this month in whole numbers")
goal=int(input())

print("enter your wage per hour")
wage=int(input())

print("add the amount any monetary support you recieve for this goal")
supprt=int(input())

goal2= goal - supprt
hours = goal2 // wage
hrweekly = hours / 4
hrdaily= hrweekly / 6
hrdaily2= round(hrdaily,2)
print("you need to work",hours, " hours monthly to achieve your goal")
print("you need to work" ,hrweekly, " hours per week to achieve your goal")
print("you need to work " ,hrdaily2, " hours per day to achieve your goal. this figure does not include sundays")







