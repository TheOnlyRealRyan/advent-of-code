with open("./strings.txt") as strings:
    # print(strings.read())
    Lines = strings.readlines()
    answer_sum = 0
    count = 0
    # Strips the newline character
    for line in Lines:
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(int(char))
        print(f"Numbers - {numbers}")
        answer = int(str(numbers[0]) + str(numbers[-1]))
        answer_sum += answer
        print(f"answer - {answer}")# count += 1
        # print(f"Line{count}: {line}")
    print(answer_sum)