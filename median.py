"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import statistics

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        #numbers.sort()
        #lnum = len(numbers)
        #midnum = len(numbers) // 2
        #if lnum % 2 == 0:
        #    mednum = (numbers[midnum-1] + numbers[midnum]) / 2
        mednum = statistics.median(numbers)
        #elif lnum % 2 == 1:
        #    mednum = numbers[midnum]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
#print(mednum)z
print(mednum)
