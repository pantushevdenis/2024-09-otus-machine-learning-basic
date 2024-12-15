import sys
count = 0
for line in sys.stdin:
    count += 1

sys.stdout.write(str(count))