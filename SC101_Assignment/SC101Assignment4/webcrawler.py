"""
File: webcrawler.py
Name: 皓暄
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')
        female_sum = 0
        male_sum = 0
        # <tr>像是列 <td>是一個一個值
        for tag in tags:  # 先處理 <tr><tr/>
            rows = tag.find_all('tr')  # <td>Noah</td> <td>183,172</td> <td>Emma</td> <td>194,917</td></tr>
            for row in rows:  # Skip the first row <tr><td>1</td>
                value = row.find_all('td')
                if len(value) >= 4:  # boy's name / number / girl's name / number
                    male = value[2]  # boy number <td>19,010</td>
                    female = value[4]  # girl number <td>16,032</td>

                    male = male.text.strip()  # get text remove ""
                    female = female.text.strip()  # get text remove ""

                    male = male.replace(',', "")  # replace "," as ""
                    female = female.replace(',', "")  # replace "," as ""

                    male_sum += int(male)
                    female_sum += int(female)
        print('Male Number:', male_sum)
        print('Female Number:', female_sum)


if __name__ == '__main__':
    main()
