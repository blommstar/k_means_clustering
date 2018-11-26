import csv

with open('blogdata.txt', mode='r') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            # print('No lines to read')
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
           #  print(f'{row[0]} är data från första raden och row2: {row[1]}')
           )
            line_count += 1
    # print(f'Skrev ut {line_count} rader')
    print(f'Processed {line_count} lines.')

def getData():
    return csv_reader
