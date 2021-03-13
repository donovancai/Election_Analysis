name = "donovan"
country = "Canada"

age = 29
hourly_wage = 90

satisfied = True 

daily_wage = hourly_wage * 8

print(name + " "+country + " "+ str(age) + str(hourly_wage))

print(f"I got {daily_wage}, \n so \t I am happy: {satisfied}")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")