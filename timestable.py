#get an input for which timestable we have to do

timestable_no = int(input('Enter an integer whose timestable you\'d like to see:\n'))
timestable_range = int(input('Specify a range:\n'))

#Get the timetable with a counting for loop

for i in range(timestable_range):
    multiplied = i*timestable_no
    print(f'{timestable_no} x {i} = {multiplied}')