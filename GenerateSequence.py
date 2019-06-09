import matplotlib.pyplot as plt

# begin list; first list is counting the frequency of the number in the second list
frequency = [1]
numbers = [1]
new_numbers = [1]
pair_plot = [[1], [1]]

# create a loop that will generate the sequence for some number of input iterations
for iterations in range(int(input("How many iterations of the sequence would you like to run? "))):

    # first need to search for new numbers in frequency and, if there are any, add to new numbers list
    for i in frequency:
        if i not in new_numbers:
            new_numbers.append(i)
            pair_plot[0].append(i)
            pair_plot[1].append(numbers[frequency.index(i)])
    new_numbers.sort()  # you can leave unsorted if you want to see the order the new numbers appear in

    # now need to calculate new frequencies
    new_frequency = new_numbers.copy()  # just so it's the right length; we'll replace each entry in the following loop
    for x in new_numbers:
        if x in numbers:
            new_frequency[new_numbers.index(x)] = frequency.count(x) + numbers.count(x) + frequency[numbers.index(x)]
        else:
            new_frequency[new_numbers.index(x)] = frequency.count(x) + numbers.count(x)

    frequency = new_frequency.copy()
    numbers = new_numbers.copy()

print(frequency)
print(numbers)
plt.plot(pair_plot[0], pair_plot[1], 'ro')
plt.show()
