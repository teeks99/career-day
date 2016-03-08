import time

start = time.time()

total = 0
number = 1
end = 70000000

while number <= end:
    total = total + number
    number = number + 1

finish = time.time()
elapsed = finish - start

print("Time: " + str(elapsed))
print("Total: " + str(total))

