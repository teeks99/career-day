import time
import sys

class Adder(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.total = 0
        self.complete = False

    def run_to(self, end):
        self.start_timer()
        result = self.add_numbers_to(end)
        self.end_timer()

        self.check(end, result)

        print("Summed numbers up to: " + str(end) + " resulting in: " + str(result) +
              " in: " + str(self.elapsed_seconds()) + " seconds.")

        self.complete = True

    def add_numbers_to(self, end):
        self.total = 0
        number = 1
        while number <= end:
            self.total = self.total + number
            number = number + 1
        return self.total

    def start_timer(self):
        self.start = time.time()

    def end_timer(self):
        self.end = time.time()

    def elapsed_seconds(self):
        if not self.start:
            raise Exception("Run not started")
        elif not self.end:
            return time.time() - self.start
        return self.end - self.start

    def check(self, end, to_check):
        if to_check != self.fast_algorithm(end):
            raise Exception("The value checked: " + str(to_check) +
                            "did not equal the expected value: " +
                            str(self.fast_algorithm(end)))

    def fast_algorithm(self, end):
        if self.is_odd(end):
            return end * ((end//2) + 1)
        return (end * (end//2)) + (end//2)

    def is_odd(self, number):
        return number & 1

if __name__ == "__main__":
    try_number = 130000000

    if len(sys.argv) > 1:
        try_number = int(sys.argv[1])

    adder = Adder()
    adder.run_to(try_number)

