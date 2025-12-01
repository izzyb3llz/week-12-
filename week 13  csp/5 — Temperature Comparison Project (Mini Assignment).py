# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.
temperature = int(input("What is todays temperature?"))

if temperature <= 50:
    print("It is cold.")
elif temperature >= 80:
    print("It is not.")
else:
 print("It is warm.")
 if temperature <= 10 or temperature >= 100:
    print("Extreme weather warning.")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

