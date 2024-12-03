# Open the file
with open("text.txt", "r") as file1:
    text = file1.readlines()

list1 = []

for line in text:  # Start line numbers from 1
    line = line.strip()  # Remove leading and trailing whitespace
    if not line:  # Skip empty lines
        continue
    dump = list(map(int, line.split(" ")))  # Convert to integers
    list1.append(dump)

def is_safe(element):

    diffs = [element[i + 1] - element[i] for i in range(len(element)-1)]

    if all(1 <= diff <= 3 for diff in diffs):
        return True
    if all(-3 <= diff <= -1 for diff in diffs):
        return True
    return False

def is_safe_with_one_removal(element):
    for i in range(len(element)):
        modified_element = element[:i] + element[i + 1:]
        if is_safe(modified_element):
            return True
    return False

# Iterate through each element
safe_count = 0
for element in list1:
    if is_safe(element) or is_safe_with_one_removal(element):
        safe_count += 1

print("Number of safe elements:", safe_count)
