from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://en.wikipedia.org/wiki/Historical_components_of_the_Dow_Jones_Industrial_Average').text
with open('simple.html') as html_file:

    soup = BeautifulSoup(source, 'html.parser')

csv_file = open('dow30.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Firm'])

company_list = []
bankrupt_list = []

for td in soup.find_all('td'):

    try:

        company = td.a.text
        if company in company_list or company == "":
            pass
        else:
            source2 = requests.get('https://www.google.com/search?q='+company).text

            soup2 = BeautifulSoup(source2, 'html.parser')

            for stock in soup2.find_all('span'):
                try:
                    name = stock.text
                    print(name)
                    if 'bankrupt' in name:
                        if company in bankrupt_list:
                            pass
                        else:
                            bankrupt_list.append(company)
                except:
                    pass

            company_list.append(company)

    except AttributeError:
        company = None


print(company_list)
print(len(company_list))
print(bankrupt_list)
print(len(bankrupt_list))

for company in company_list:
    csv_writer.writerow([company])

csv_writer.writerow([""])
csv_writer.writerow([""])

for company in bankrupt_list:
    csv_writer.writerow([company])
csv_file.close()
