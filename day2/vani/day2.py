file_path = "./input.txt"

all_stats = {}

def part_one(line, r_max, g_max, b_max):
    initial_parse = line.split(": ")
    game_key = initial_parse[0].split()[-1]
    game_stats = [x.split("; ") for x in initial_parse[1:]]

    red = True
    green = True
    blue = True

    for rnd in game_stats[0]:
        for data in rnd.split(", "):
            stats = data.split()
            num = int(stats[0])  
            color = stats[1]

            if color == "red" and num > r_max:
                red = False
            if color == "green" and num > g_max:
                green = False
            if color == "blue" and num > b_max:
                blue = False

    return int(game_key) if red and green and blue else 0


def part_two(line):
    initial_parse = line.split(": ")
    game_stats = [x.split("; ") for x in initial_parse[1:]]

    red = 0
    green = 0 
    blue = 0 

    for rnd in game_stats[0]:
        for data in rnd.split(", "):
            stats = data.split()
            num = int(stats[0])  
            color = stats[1]

            if color == "red":
                red = max(red, num)
            if color == "green":
                green = max(green, num)
            if color == "blue":
                blue = max(blue, num)

    return red*green*blue

with open(file_path, 'r') as file:
    sum_pt1 = 0
    sum_pt2 = 0
    for line in file:
        one_line = line.strip()
        sum_pt1 += part_one(one_line, 12, 13, 14)  # Max values for red, green, and blue
        sum_pt2 += part_two(one_line)
    print(f"part 1: {sum_pt1}")
    print(f"part 2: {sum_pt2}")
