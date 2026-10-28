# Task 4: If Condition

# 1. BMI Category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# 2 & 3. City-country lookup
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city_country = {}
for country, cities in countries.items():
    for city in cities:
        city_country[city.lower()] = country

city = input("Enter a city name: ").strip()
country = city_country.get(city.lower())

if country:
    print(f"{city} is in {country}")
else:
    print("City not found in the given list.")

first = input("Enter the first city: ").strip()
second = input("Enter the second city: ").strip()

country1 = city_country.get(first.lower())
country2 = city_country.get(second.lower())

if country1 and country2 and country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
