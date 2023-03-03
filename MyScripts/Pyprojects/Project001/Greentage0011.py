#Creating a csv file and writing into it.

from pathlib import Path
import csv

directory = Path(r'C:\Users\KataniMed\MyScripts')
my_file = directory / 'Patients info.txt'
my_file.touch()

with open(r'C:\Users\KataniMed\MyScripts\Patients info.txt', mode='w') as file:
    filenames = ['Date', 'OP Number', 'Gender','Age', 'Name', 'Resident', 'Contacts']
    write_file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    write_file.writerow(['13/06/1999', '9999', 'Male', '24', 'Juggernaut', 'Katani', '0702538306'])