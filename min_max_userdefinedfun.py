number_of_numbers = int(input("how many numbers do you want to enter : "))

max = 0

def max_num(value, max):

    val = max
    if value > val:
        val = value
    return val

def min_num(value, min):

    if value < min:
        min = value
    return min 


for i in range(0,number_of_numbers):
    num = int(input(f"enter the {i+1} value : "))
    if i == 0:
        min = num
    min = int(min_num(num, min))
    max = int(max_num(num, max))

print("the maximum value is : " + str(max))
print("the minimum value is : " + str(min))
