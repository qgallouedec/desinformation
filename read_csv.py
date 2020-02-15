import csv


medias = ["Les journaux ou magazines d'information imprimés",
    "Les journaux ou magazines d'information en ligne",
    "Les réseaux sociaux en ligne et les applications de messagerie",
    "La télévision",
    "La radio"]

countries = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES",
    "FR", "HR", "IT", "CY", "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL",
    "PT", "RO", "SI", "SK", "FI", "SE", "UK"]

answers = ["Totally trust", "Tend to trust", "Tend not to trust",
    "Do not trust at all", "DK/NA", "Total 'Trust'", "Total 'Do not trust'"]

devices = ["Desk Compu-\nter", "Laptop", "Mobile Phone", "Landline phone",
    "Internet connection at home", "Tablet", "At least one device"]

def parse_path(country, media):
    return 'data/brut/fl_464_Volume_C_xls/fl_464_Volume_C_{}/Q1.{}-Tableau 1.csv'.format(country, medias.index(media)+1)


with open('data/brut/fl_464_Volume_C_xls/fl_464_Volume_C_AT/Q1.1-Tableau 1.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    data = list(spamreader)


def find_col(data, device):
    for row in data:
        for i_col, val in enumerate(row):
            if val == device:
                return i_col


def find_row(data, answer):
    for i_row, row in enumerate(data):
        for val in row:
            if val == answer:
                return i_row-1

def get_number_respondants(country, media, answer, device):
    with open(parse_path(country, media)) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data = list(spamreader)
    
    i_row = find_row(data, answer)
    i_col = find_col(data, device)

    return data[i_row][i_col]

def get_total_respondants(country, media, answer):
    with open(parse_path(country, media)) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data = list(spamreader)
    i_row = find_row(data, answer)
    i_col = find_col(data, country)

    return data[i_row][i_col]
rows=[]
for country in countries:
    for media in medias:
        for answer in answers:
            for_devices = []
            tot = int(get_total_respondants(country, media, answer))
            for device in devices:
                for_devices.append(int(get_number_respondants(country, media, answer, device))/tot)
            rows.append([country, media, answer] + for_devices)

with open('data_devices.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['', '', '']+devices)
    for row in rows:
        spamwriter.writerow(row)

