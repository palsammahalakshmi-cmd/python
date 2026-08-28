years=int(input("enter years of servies"))
salary=float(input("enter salary :"))
rating=input("enter performance rating(excellent/good/poor):")
Bonus = 0
if years == 5:
    if rating == "excellent":
        Bonus = salary * 0.20
    elif rating == "good":
        Bonus = salary * 0.10
    elif rating == "poor":
        Bonus = salary * 0.05
else:
    if rating == "excellent":
        Bonus = 0

print("total salary:", salary + Bonus)