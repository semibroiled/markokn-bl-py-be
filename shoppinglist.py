shop_lst = []
trigger = input('Enter an item or press enter to quit:\n')

while True:
    shop_lst.append(trigger)
    trigger = input('Enter an item or press enter to quit\n:')
    if trigger == int:
        pass
    elif trigger =='':
        break

print(f'Your shopping list is:\n{shop_lst}')

