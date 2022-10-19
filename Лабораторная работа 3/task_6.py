list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maxnumber = list_numbers[0]
maxindex = 0

for n in range((len(list_numbers))):
    if list_numbers[n] > maxnumber:
        maxnumber = list_numbers[n]
        maxindex = n

list_numbers[maxindex], list_numbers[-1] = list_numbers[-1], list_numbers[maxindex]
# TODO Оформить решение

print(list_numbers)
