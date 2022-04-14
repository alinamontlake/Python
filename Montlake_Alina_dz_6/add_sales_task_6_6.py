import sys

if len(sys.argv) != 2:
    print('type sales')
    exit(1)
    with open('bakery.csv', 'a', encoding='utf8') as f:
        print(f'{sys.argv[1]:10}', file=f)
