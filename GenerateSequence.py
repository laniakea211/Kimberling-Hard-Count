# begin list; first list is counting the number in the second list
frequency = [1]
numbers = [1]

# create a loop that will generate the sequence for some number of input iterations
for iterations in range(int(input("How many iterations of the sequence would you like to generate? "))):

    # first need to search for new numbers in frequency and, if there are any, add to numbers list
    new_numbers = numbers.copy()
    for i in frequency:
        if i not in new_numbers:
            new_numbers.append(i)
    new_numbers.sort()

    # now need to calculate new frequencies
    new_frequency = new_numbers.copy()
    for number in new_numbers:
        if number in numbers:
            new_frequency[new_numbers.index(number)] = frequency.count(number) + numbers.count(number) + frequency[numbers.index(number)]
        elif number not in numbers:
            new_frequency[new_numbers.index(number)] = frequency.count(number) + numbers.count(number)

    frequency = new_frequency.copy()
    numbers = new_numbers.copy()

print(frequency)
print(numbers)
