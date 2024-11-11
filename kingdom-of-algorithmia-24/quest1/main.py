def count_potions(filename: str):
    count = 0
    with open(filename) as f:
        input = f.readline().strip()

        for ch in input:
            if ch == 'B':
                count += 1
            elif ch == 'C':
                count += 3
            else:
                continue
                
    return count

def count_potions_pairs(filename: str):

    values = {
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5,
        'x': 0,
        }
    
    count = 0

    with open(filename) as f:
        input = f.readline().strip()

        for i in range(0, len(input) - 1, 2):
            pair = (input[i], input[i+1])
            # if either one of the elements is an x, the base potion value is not modified 
            if pair[0] == 'x' or pair[1] == 'x':
                count += values.get(pair[0])
                count += values.get(pair[1])
            else:
                count += values.get(pair[0]) + 1
                count += values.get(pair[1]) + 1
    
    return count

def count_potions_thruples(filename: str):

    values = {
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5,
        'x': 0,
        }
    
    count = 0

    with open(filename) as f:
        input = f.readline().strip()

        for i in range(0, len(input) - 2, 3):
            thruple = (input[i], input[i+1], input[i+2])
            # determine if thruple is actually a thruple, a pair, or single attack, based on number of x's
            count_x = thruple.count('x')

            # a single attack, base values
            if count_x == 2:
                count += values.get(thruple[0])
                count += values.get(thruple[1])
                count += values.get(thruple[2])
            # pair attack, values + 1
            elif count_x == 1:
                if thruple[0] != 'x':
                    count += values.get(thruple[0]) + 1
                if thruple[1] != 'x':
                    count += values.get(thruple[1]) + 1
                if thruple[2] != 'x':
                    count += values.get(thruple[2]) + 1
            # if xxx do nothing
            elif count_x == 3:
                continue
            # triple threat, values + 2
            else:
                if thruple[0] != 'x':
                    count += values.get(thruple[0]) + 2
                if thruple[1] != 'x':
                    count += values.get(thruple[1]) + 2
                if thruple[2] != 'x':
                    count += values.get(thruple[2]) + 2
                
    return count


if __name__ == "__main__":
    input_path = "./everybody_codes_e2024_q01_p1.txt"
    input_path2 = "./everybody_codes_e2024_q01_p2.txt"
    input_path3 = "./input3.txt"
    print("Result: ")
    # print(count_potions(input_path))
    # print(count_potions_pairs(input_path2))
    print(count_potions_thruples(input_path3))