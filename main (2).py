#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator") 
bill_total=int(input("What was the total bill?: "))
bill_percentage=int(input("what percentage tip would you like to give:10,12, or 15: "))
people_divide=int(input("how many people to split the bill: "))
check=bill_total/people_divide*(1+bill_percentage/100)
print(f"Each person should pay:{check:.2f}")

print(type(bill_percentage))