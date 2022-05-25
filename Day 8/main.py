# Creating a simple function
def greet():
    print("Hello good evening.")
    print("How are you today?")
    print("Hope you have eaten?\n")


# Calling a simple function
greet()


# Creating a function with an input
# "name" is parameter
def greet2(name):
    print(f"Hello good evening {name}")
    print(f"{name} how are you today?")
    print("Hope you have eaten?\n")


# Calling a function with an input
# "Hillary" is argument
greet2("Hillary")


# Creating a function with more than one  input
def greet3(name, location, weather):
    print(f"Hello good evening {name}")
    print(f"How is {location} today?")
    print(f"Is it {weather} over there?")


# Calling a function with more than one input
# Positional argument
greet3("Hillary", "Port Harcourt", "rainy")


# Creating a function with more than one  input
def greet4(name, location, weather):
    print(f"Hello good evening {name}")
    print(f"How is {location} today?")
    print(f"Is it {weather} over there?")


# Calling a function with more than one input
# Keyword argument
greet4(location="Port Harcourt", weather="rainy", name="Hillary")
