def gtin_check (gtin):

    gtin_unchecked = input('Write the GTIN: ')

    gtin_checksum = int(gtin_unchecked[-1]) 

    gtin_wocheck = list(gtin_unchecked)

    gtin_wocheck.pop(-1)
    
    print(gtin_wocheck is gtin_checksum)
    
    print(gtin_wocheck)

    sum_digits = 0

    for i in range(len(gtin_wocheck)):

        digit= gtin_wocheck[-i-1]
        value = int(digit)

        if i%2 == 0:
            value *=3
        sum_digits += value
    final = abs(10-(sum_digits%10))

    print(f'Is {final} the same as {gtin_checksum}?')

    return final 

gtin_check(gtin=1)

