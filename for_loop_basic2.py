##Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
##Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def positive(list):
    for i in range (len(list)):
        if list[i] > 0:
            list[i] = 'big'
    return list
print(positive([-1, 3, 4, 5, -5]))


##Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def countPositive(list):
    count = 0
    for i in range (len(list)):
        if list[i]> 0:
            count += 1
    list[len(list)-1]= count
    return list
print(countPositive([-1,2,2,2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sumTotal([1,2,3,4]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for i in range(len(list)):
        sum+= list[i]
    return (sum/len(list))
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(list):
    return (len(list))
print(length([37,2,1,-9,5]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(list):
    minVal = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i]< minVal:
            minVal = list[i]
    return minVal
print(minimum([37,2,1,-9]))


# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    maxVal = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i]> maxVal:
            maxVal = list[i]
    return maxVal
print(maximum([37,2,1,-9]))
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimateAnalysis(list):
    dict = {
    'sumtotal': 0,
    'average': 0,
    'minimum': 0,
    'maximum': 0,
    'length': len(list)}
    for i in range(len(list)):
        dict['sumtotal'] += list[i]
        dict['average'] = (dict['sumtotal']/len(list))
        if list[i]> dict['maximum']:
            dict['maximum'] = list[i]
        if list[i]< dict['minimum']:
            dict['minimum'] = list[i]
    return dict
print(ultimateAnalysis([37,2,1,-9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse(list):
    for i in range ((len(list)//2)):
        temp = list[i]
        list[i] = list[(len(list)-1)-i]
        list[(len(list)-1)-i] = temp
    return list
print(reverse([37,2,1,-9]))
