def get_bmi():
    name = input("Enter your name: ")
    cm = float(input("Enter your height in centimeters: "))
    kg = float(input("Enter your weight in kilograms: "))

    #formula
    m = cm / 100
    bmi = kg / (m ** 2)

    print(f"{name}, your BMI is {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("Your weight is normal")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")

get_bmi()