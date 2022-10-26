from functools import cache

class Fibonacci:

    def __init__(self):
        self.iterations = None
        self.fibonacci_list = []

    @cache
    def fibonacci_number(self, n):
        """Generating fibonacci number in sequence position n"""
        self.iterations = n
        if n == 0:
            return 0
        if n == 1: 
            return 1
        else:
            return self.fibonacci_number(n - 1) + self.fibonacci_number(n - 2)

    def is_fibonacci(self, n):
        """Check if n input is in fibonacci sequence"""

        # number input from user
        n = int(n)
        while True:
            for i in range(n + 2):
                fib_number = self.fibonacci_number(i)
                if n == fib_number:
                    return True
                elif fib_number > n:
                    return False

    def fib_array(self, n):
        """Generating fibonacci sequence until n position"""
        for i in range(n):
            self.fibonacci_list.append(self.fibonacci_number(i))


def main():
    fib = Fibonacci()

    print("""
        What do you want to do?
        1. Number of Fibonacci series in n position; 
        2. Fibonacci series until n position;
        3. n is in Fibonacci series
        q. Quit
        """)

    done = False
    while not done:
        choice = str(input('Enter your choice: '))
        if choice == '1':
            position = int(input('Enter n position: '))
            fib_number = fib.fibonacci_number(position - 1)
            print(f'Fibonacci number in position {position} is: {fib_number}')
        elif choice == '2':
            position = int(input('Enter n position: '))
            fib.fib_array(position)
            fib_array = fib.fibonacci_list
            print(f'First {position} series terms are: {fib_array}')
        elif choice == '3':
            number = int(input('Enter number to check: '))
            fib_bool = fib.is_fibonacci(number)
            if fib_bool is True:
                print(f'Number {number} is in Fibonacci series.')
            else:
                print(f'Number {number} is NOT in Fibonacci series.')
        elif choice == 'q':
            done = True
            print('Quitting...')
        else:
            print('Please provide a valid entry. ')


if __name__ == "__main__":
    main()
