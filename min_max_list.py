number_of_numbers = int(input("how many numbers do you want to enter : "))

values = []

for i in range(0,number_of_numbers):
    num = int(input(f"enter the {i + 1} value : "))
    values.append(num)

min = values[0]
max = 0

for i in range(0, number_of_numbers - 1):
    if min > values[i]:
        min = values[i]
    if max < values[i]:
        max = values[i]    

print(min, max)
