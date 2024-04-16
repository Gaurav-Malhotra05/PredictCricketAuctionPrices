import urllib
import bs4 as bs
import re
import numpy as np
import pandas as pd

#sheet = pd.read_excel('2019FinalOutput.xlsx')
Country = []
array1 = []
initial = 0
number = len(sheet)
#for item in sheet['Player Name'][initial:number]:
# for item in ['AB de Villiers', 'Abhishek Sharma']:
#     array1 = np.append(array1, item)


# for player in
for player in ["AB de Villiers", "Abhishek Sharma"]:
    print(player)
    while True:
        try:
            source = urllib.request.urlopen("https://en.wikipedia.org/wiki/" + ('_'.join(str(player).split())))
            break
        except Exception as e:
            print(e, 'Trying again...')
            break

    soup = bs.BeautifulSoup(source, 'lxml')

    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text

    arr = text.split()

    for i in range(len(arr)):
        if 'cricketer' in arr[i]:
            final = arr[i-2:i]
            text1 = ' '.join(final)
            break

    Country = np.append(Country, text1)

print(Country)
#sheet['Country'][initial:number] = Country

#sheet.to_excel('2019FinalOutput.xlsx')
