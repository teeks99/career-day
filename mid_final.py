import datetime

def check(number, to_check):
    actual = 0
    if number % 2 == 0:
        # Even
        actual = (number * number//2) + (number//2)
    else:
        # Odd
        actual = number * ((number//2) + 1)

    if actual != to_check:
        raise Exception("Actual and checked values do not match!")


start = datetime.datetime.now()

total = 0
number = 1
end = 100

while number <= end:
    total = total + number
    number = number + 1

finish = datetime.datetime.now()
elapsed = finish - start

check(number, total)

print("Time: " + str(elapsed.total_seconds()))
print("Total: " + str(total))


