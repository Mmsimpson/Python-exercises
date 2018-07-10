def smallest_number(numbers):
    smallest = numbers [0]
    for number in numbers:
        if number < smallest:
            smallest = number 
    return  smallest
print smallest_number([7, 3, 8, 1])