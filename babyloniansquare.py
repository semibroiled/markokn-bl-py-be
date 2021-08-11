
while True:
   
    wanted_root = int(input('Write an integer: '))

    first = 1
    second = wanted_root
    
    for tries in range(100):
        first = (first + second)/2
        second = wanted_root / first
        print(first, second)
    
    if wanted_root == '':
        break