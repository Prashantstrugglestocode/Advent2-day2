import re

# Patterns
pattern = re.compile(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)")
pattern2 = re.compile(r"mul\([0-9]+,[0-9]+\)")
pattern3 = re.compile(r"[0-9]+")


list1 = []
list2 = []
list3 = []


def read_all_muls(textFile: str):
    for i, line in enumerate(open(textFile)):
        for match in re.findall(pattern, line):
            list1.append(match)
read_all_muls("text.txt")
print("List1:", list1)


def read_the_numbers(list1):
    state = True
    for i, item in enumerate(list1):
        print(i, item)
        if 'do()' in item:
            state = True
        elif "don't()" in item:
            state = False

        if state:
            for match in re.findall(pattern2, item):
                list2.insert(i, match)
    return list2

read_the_numbers(list1)
print("List2:", list2)


def change_numbers_to_int(list2):
    for item in list2:
        for match in re.findall(pattern3, item):
            list3.append(int(match))

change_numbers_to_int(list2)
print("List3:", list3)


value = 0
for i in range(0, len(list3) - 1, 2):
    value += list3[i] * list3[i + 1]

print("Value:", value)
