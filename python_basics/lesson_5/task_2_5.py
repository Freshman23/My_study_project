with open('task_2_5.txt', 'r') as file_read:
    for num, line in enumerate(file_read):
        print(f"In {num + 1} line: {len(line.split(' '))} words")
    print(f"Totally {num + 1} lines in file: {file_read.name}")
