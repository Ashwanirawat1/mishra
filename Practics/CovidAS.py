from csv import reader,DictReader
from enum import unique

def read_csv():
    with open("D:\pythonD\covid-data.csv")as f:
        records = []
        rows = DictReader(f)
        for row in rows:
            records.append(row)
    return records
# covid = read_csv()
# print(covid)


def total_cases():
    total = 0
    data = read_csv()
    for item in data:
        total = total + int(item['new_cases'])
    return total
#total_no_of_case = total_cases()
#print(total_no_of_case)

def total_cases_by_country():
    by_country = {}
    data = read_csv()
    for item in data:
        country = item['location']
        cases = int(item['new_cases'])
        if country in by_country:
            by_country[country] += cases
        else:
            by_country[country] = cases
    return by_country

#total_country_cases = total_cases_by_country()
#print(total_country_cases)

def countries():
    _countries = []
    data = read_csv()
    for item in data:
        _countries.append(item['location'])
    unique_countries = set(_countries)
    return unique_countries
#list_of_unique_countries = countries()
#print(list_of_unique_countries)
#print(len(list_of_unique_countries))

def countries():
    data = read_csv()
    return{item['location']for item in data}
#list_of_coun = countries()
#print(list_of_coun)


def countries():
    data = read_csv()
    return{item['location'] for item in data}
#list_country_compre = countries()
#print(list_country_compre)

def countries_less_10k():
    less_10k = {}
    by_country = total_cases_by_country()
    for country,case in by_country.item():
        if case <=1000:
            less_10k[country] = cases
    return less_10k
#countries_les = countries_less_10k()
#print(countries_les)
def countries_less_10k():
    by_country = total_cases_by_country()
    return{country:cases for country,cases in by_country.items() if cases<=1000}
country_less_ = countries_less_10k()
print(country)