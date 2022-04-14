import sys

if len(sys.argv) > 3:
    print('Только два параметра допустимы')
    exit(1)

start = int(sys.argv[1])-1 if len(sys.argv) > 1 else 0
end = int(sys.argv[2])-1 if len(sys.argv) > 2 else None

with open('bakery.csv', 'r', encoding='utf8') as f:
    f.seek(11*start)
    curline = start
    for line in f:
        if end is None or curline <= end:
            print(line, end='')
            curline += 1
        else:
            break
