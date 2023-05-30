from bs4 import BeautifulSoup
import requests
import time
import os

url = 'https://www.rcdso.org/find-a-dentist/search-results?Alpha=&City=Hamilton&MbrSpecialty=&ConstitID=&AlphaParent=&Address1=&PhoneNum=&SedationType=&SedationProviderType=&GroupCode=&DetailsCode='
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

results = []

search_results = soup.find('div', {'id': 'dentistSearchResults'})

query_response_elements = search_results.find_all('section')
length = len(query_response_elements)
i = 0
while i < length:
    section = search_results.find_all('section')[i]
    try:
        name_tag = section.find('h2').find('a')
        name = name_tag.text.strip()
        
        reg_num = section.find('dt', text='Registration Number:').find_next_sibling('dd').text.strip()
        primary_practice = section.find('strong', text='Primary Practice')
        
        if primary_practice:
            primary_practice = primary_practice.find_next_sibling('address').text.strip()
        else: 
            primary_practice = ''
        location = primary_practice.split('\n')
        if len(location) > 1:
            primary_practice = location[0] + " - " + location[1]
            ##primary_practice = location[1]
        print(primary_practice)
        
        results.append((name, primary_practice))
        i += 1
        # print(results)
    except Exception as e:
        print('Error: ' + str(e))
        time.sleep(1)
        i += 1

print(results)
with open(os.path.join('parsed_info.txt'), 'w') as file:
    for tuple in results:
        # write each item on a new line
        file.write(repr(tuple))
        file.write('\n')