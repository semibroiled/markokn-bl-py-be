def fibonacci (x):
    f_1 = 0
    f_2 = 1
    fibonacci = [f_1, f_2]

    for i in range(x-2):

        f_new = f_1+f_2

        fibonacci.append(f_new)

        f_1 = f_2

        f_2 = f_new

    print(fibonacci)

fibonacci(100)