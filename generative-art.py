import sys
import random

chars = '</>'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: generative-art.py rows columns | eg. python3 generative-art.py 20 30")
    draw(int(sys.argv[1]), int(sys.argv[2]))