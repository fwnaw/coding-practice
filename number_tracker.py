numbers = []

while True:
    user_input = input("Enter a number or done: ")
    if user_input == "done":
        break
    numbers.append(int(user_input))

highest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
print(f"{highest} is the highest score")
    
lowest = numbers[0]
for number in numbers:
    if number < lowest:
        lowest = number
print(f"{lowest} is the lowest score")
    
total = 0
for number in numbers:
    total = total + number
print(f"mean score = {total / len(numbers)}")

