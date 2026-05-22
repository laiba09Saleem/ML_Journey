# 1. Create a list of 5 cities you know

cities = ["Pakistan", "India", "Turkey", "Saudia", "Iran"]

# 2. Print only the first 3 cities using slicing
print(cities[:3])

# 3. Add a new city to the list
cities.append("Asia")
print(cities)

#4. Use a loop to print each city with its number
   #like: "1. Karachi"  "2. Lahore" etc
   
'''for i in range(len(cities)):
    print(f"{i+1}. {cities[i]}")
'''
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")

# 5. Use list comprehension to make a new list
   # of city names that have more than 5 letters
long_cities = [city for city in cities if(len(city) > 5)]
print(long_cities)