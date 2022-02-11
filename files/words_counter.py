file = open('input.txt', 'r')

lines = file.readlines()

counter = {}
total_cnt = 0

for line in lines:
    words = line.split()

    total_cnt += len(words)
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
print(f'File contains {total_cnt} words')
print(f'Words statistic:')       
print(counter)

