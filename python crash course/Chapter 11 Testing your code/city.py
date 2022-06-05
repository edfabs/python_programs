from city_functions import formatted_city_country

city = input("Enter a city: ")
country = input(f"Enter the contry of the {city}:")

formatted = formatted_city_country(city, country)
print(formatted)
