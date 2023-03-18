feet = float(input("Enter distance in feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print(f"{feet} feet is equal to {inches} inches.")
print(f"{feet} feet is equal to {yards:.2f} yards.")
print(f"{feet} feet is equal to {miles:.8f} miles.")
