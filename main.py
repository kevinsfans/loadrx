import extramodule as rx
import sys


# file naming and checking extension; only .csv supported so it was hardcoded in
filename = input('Enter a filename to store to: ').lower()
for i in range(len(filename)):
    if filename[i] == '.':
        extension = filename[i:]
    else:
        pass
if '.' not in filename:
    filename += '.csv'
else:
    pass


# just making sure the user didn't open this on accident, remove if too redundant
choice = input('What would you like to do? If you would like to enter a new'
               '\nmedication entry, hit the enter button. Otherwise, hit any'
               '\nother key: ')



if choice == '':
    print('You have chosen to make a new entry into the master list of'
          '\nmedications. Continuing now...')
else:
    sys.exit()


# storing all relevant paramters for the Prescriptions class in local variables
def load():
    temp_name = input('Enter the name of the medication, including the brand: ')
    temp_rx = input('Enter the prescription number (Rx): ')
    temp_date = input('Enter the date of prescription in DD-MMM-YYYY format: ').upper()
    temp_dur = input('Enter the expected number of days: ')
    temp_dose = input('Enter the dosage (in mg) of the medication: ')
    temp_doc = input('Enter the surname (ONLY) of prescribing doctor: ').upper()
    return temp_name, temp_rx, temp_date, temp_dur, temp_dose, temp_doc


# writing to file
outfile = open(filename, 'a', encoding='utf-8')
check = True
while check:
    load_name, load_rx, load_date, load_dur, load_dose, load_doc = load()
    double_check = input('Do you want to make any further entries? Click the enter key to continue: ').lower()
    prescription = rx.Prescriptions(load_name, load_rx, load_date, load_dur, load_dose, load_doc)
    temp_prescription = prescription.unpack()
    for i in range(len(temp_prescription)):
        if temp_prescription[i] == temp_prescription[-1]:
            outfile.write(f'{temp_prescription[i]}\n')
        else:
            outfile.write(f'{temp_prescription[i]},')
    if double_check == '':
        continue
    else:
        print('See you next time, exiting code now...')
        sys.exit()
