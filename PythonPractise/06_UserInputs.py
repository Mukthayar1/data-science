# Age checking

personA = input("Please enter your name here : ")
personA_age = int(input(f"{personA}, please enter your age here: "))


personB = input("Please enter your partner name here : ")
personB_age = int(input(f"{personB}, please enter your age here: "))

if personA_age > personB_age :
    print(personA , " you are older then " , personB)
else :
     print(personB , " you are older then " , personA)

# BMI Calculator

Person_Weight = float(input("Please enter your weight in kgs : "))
Person_Weight = float(input("Please enter your height in meters : "))

bmi = (Person_Weight / (Person_Weight ** 2))

print(f"Your BMI is = {bmi:.2f}")