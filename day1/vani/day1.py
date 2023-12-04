file_path = "./input.txt"

def part_one(line):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    r, l = 0, len(line) - 1
    left = False
    right = False

    while not left or not right:
        if not right:
            if line[r] in numbers:
                right = True
            else:
                r += 1

        if not left:
            if line[l] in numbers:
                left = True
            else:
                l -= 1

    return int(line[r] + line[l])

def part_two(line):
    numeric_mapping = {
        "eight": "eight8eight",
        "two": "two2two",
        "one": "one1one",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "nine": "nine9nine",
    }
    modified_string = line
    for word, numeric_value in numeric_mapping.items():
        modified_string = modified_string.replace(word, numeric_value)
    return (part_one(modified_string))

with open(file_path, 'r') as file:
    sum_pt1 = 0
    sum_pt2 = 0
    for line in file:
        one_line = line.strip()
        sum_pt1 += part_one(one_line)
        sum_pt2 += part_two(one_line)

    print(f"part 1: {sum_pt1}")
    print(f"part 2: {sum_pt2}")

# part 1: 54634
# part 2: 53855