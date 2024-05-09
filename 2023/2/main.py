numbers_strings = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}


with open("./strings.txt") as strings:
    # print(strings.read())
    
    Lines = strings.readlines()
    answer = 0
    answer_sum = 0
    count = 0
    # Strips the newline character
    for line in Lines:
        dict={}
        numbers = []
        print(line)
        min_num_pos = 10000
        max_num_pos = -1
        minimum = 10000
        maximum = -1
        for number in numbers_strings:
            
            if line.find(number) != -1:
                dict[number] = line.find(number)
        
        for char in line:
            if char.isdigit():
                
                numbers.append(int(char))
                
                # answer = int(str(numbers[0]) + str(numbers[-1]))
                min_num_pos = line.find(str(numbers[0]))
                max_num_pos = line.find(str(numbers[-1]))
                min_num = numbers[0]
                max_num = numbers[-1]
        # print(min_num_pos, max_num_pos)
                
        if len(dict) > 0:
            
            minimum = min(dict.values())
            maximum = max(dict.values())
            
            minimum_word = [key for key in dict if dict[key] == minimum]
            maximum_word = [key for key in dict if dict[key] == maximum]

            lowest_num = int(str(numbers_strings.get(minimum_word[0])))
            highest_num = int(str(numbers_strings.get(maximum_word[0])))
            
            # print(lowest_num, highest_num)

        if minimum >= min_num_pos:
            lowest_num = min_num
        if maximum <= max_num_pos:
            highest_num = max_num

        print(lowest_num, highest_num)
        answer = int(str(lowest_num) + str(highest_num))
        # print(lowest_num, highest_num)
        print(answer)
        answer_sum += answer
        
        
        # print(answer_sum)
        
        print(answer_sum)
        # print(dict)

    # print(answer_sum)
