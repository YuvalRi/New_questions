# Task 1 - Basics

# 1
def right_angle():
    for i in range(1, 6):
        print("X "*i)

# 2
def isosceles_triangle():
    for i in range(7, 0, -2):
        spaces = "  " * ((7 - i) // 2)
        print(spaces + "X " * i)

# 3 
def triangle():
    right_angle()
    for i in range(4, 0, -1):
        print("X "* i)

# 4
def steps_to_n(n: int):
    if n <= 0:
        raise ValueError("Error! Input must be a natural number")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end =' ')
        print()

# 5
def odd_and_even_sequence(n: int):
    if n <= 0:
        raise ValueError("Error! Input must be a natural number")
    for i in range(1, n+1):
        for j in range(1, i+1):
            if (i % 2 != 0):
                print(2*j-1, end =' ')
            else:
                print(2*j, end =' ')
        print()

if __name__ == "__main__":
    right_angle()
    isosceles_triangle()
    triangle()
    steps_to_n(n=0)
    steps_to_n(n=5)
    odd_and_even_sequence(n=7)