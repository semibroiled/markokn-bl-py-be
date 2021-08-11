
lst = []
while False:
    modul  = {  'name' : 'name',
                'credit_points':'some number',
                'uebung': 'decision',
                'vorrechenuebung': 'decision',
                'hue_bonuspunkte':'decision',
                'vorlesung':'decision'}
    x = input('Name of Subject: ')
    y = input('Number of credit points: ')
    z = input('Gibt es Uebungen bzw. Vorrechenuebungen dazu? ')
    modul['name'] = x 
    modul['credit_points'] = y
    modul['uebung'] = modul['vorrechenuebung'] = z
    lst.append(modul)
    print(lst)

tup = (2020, 11, 28)

tup = list(tup)

print(tup)
