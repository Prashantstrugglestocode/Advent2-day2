# Open the file
with open("text.txt", "r") as file1:
    text = file1.readlines()

list1 = []
count = 0
for line in text:
    line = line.strip()
    if not line:  # Skip empty lines
        continue
    dump = list(map(int, line.split(" ")))  # Convert to integers
    list1.append(dump)


def is_safe(element):
    diff = [element[i + 1] - element[i] for i in range(len(element) - 1)]
    difft = map(int, element)
    if (3 >= difft >= 1 for diffs in diff):
        return True
    if (-3 <= difft <= -1 for diffs in diff):
        return True
    return False


def if_safe_after_one_removal(element):
    for i in range(len(element)):
        new_element = element[:i] + element[i + 1:]
        if is_safe(new_element):
            return True
        return False


for element in list1:
    if is_safe(element) or if_safe_after_one_removal(element):
        count += 1

print(count)
