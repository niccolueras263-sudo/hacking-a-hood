is_even(number):
return number % 2 == 0
# quick tests: does it match what we KNOW is true?
print(is_even(4)) # expect True
print(is_even(7)) # expect False
print(is_even(0)) # expect True
calculate_area(radius):
return 3.14 * radius ** 2
print(calculate_area(5)) # 78.5
print(calculate_area(10)) # 314.0
get_positive_number():
while True:
entry = input("Enter a positive whole number: ")
if entry.isdigit() and int(entry) > 0:
return int(entry)
print("Invalid input. Please enter a positive whole number.")
age = get_positive_number()
print("You entered", age)
calculate_area(radius):
area = 3.14 * radius ** 2
breakpoint() # program pauses here
return area
print(calculate_area(5))
calculate_area(radius):
print("DEBUG radius =", radius) # is the input what I expect?
area = 3.14 * radius ** 2
print("DEBUG area =", area) # is the math right?
return area
print(calculate_area(5))
DEBUG radius = 5
DEBUG area = 78.5
78.5
count = 0
while count < 5:
print(count)
count += 1 # this is what eventually ends the loop
print(count)
count = 0
while count < 5:
name = "Charlie"
if name == "Alice" or name == "Bob":
print("Hello, friend!")
else:
print("Hello, stranger!")
# even cleaner:
if name in ("Alice", "Bob"):
print("Hello, friend!")
name = "Charlie"
if name == "Alice" or "Bob":
print("Hello, friend!")
else:
print("Hello, stranger!")
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
print(numbers[i])
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
print(numbers[i + 1])
age = 25
print(age)
person = {"name": "John", "age": 30}
print(person.get("city", "Unknown")) # Unknown
person = {"name": "John", "age": 30}
print(person["city"])
numbers = [1, 2, 3]
print(numbers[2]) # 3 (the last item)
person = {"name": "John", "age": 30}
print(person["city"])
numbers = [1, 2, 3]
print(numbers[2]) # 3 (the last item)
numbers = [1, 2, 3]
print(numbers[3])
age = "25"
total = 30 + int(age)
print(total) # 55
age = "25"
total = 30 + age
FIXED — CHECK BEFORE YOU DIVIDE
divisor = 0
if divisor != 0:
print(10 / divisor)
else:
print("Cannot divide by zero")def greeting(name):
return "Hello, " + name
print(greeting("Alice"))
def greeting(name):
retrun "Hello, " + name
print(greeting("Alice"))
for i in range(5):
print(i)
for i in range(5):
print(i)
if x > 5:
print("x is greater than 5")
if x > 5
print("x is greater than 5")
print("Hello, world!")
Traceback (most recent call last):
File "game.py", line 12, in <module>
print(scores[5])
IndexError: list index out of range
