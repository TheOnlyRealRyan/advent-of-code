numbers_strings = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

with open("./strings.txt") as strings:
    Lines = strings.readlines()
    
    for line in Lines:
        print(line)
        numbers = {}    
        line_count = 0
        for char in line:
            line_count +=1
            if char.isdigit():
                numbers[char] = line_count
        
        # print(list(numbers.keys())[0] + list(numbers.keys())[-1])
        # print(list(numbers.values())[0], list(numbers.values())[-1])
        
        # TODO: search through the line forwards and backwards
        
        print(numbers)