import urllib.request
from bs4 import BeautifulSoup


################################################################################
############# Core Algorithm for scraping and sorting a given Alexa url page ###
################################################################################

def find_em(url):
    name = url.split('/')[-1]
    final_dict = []
    root = 'https://www.alexa.com'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
    except Exception as e:
        print('\nYou can load the link onto clipboard too.\n')
        print('Error raised : ' + str(e))


    soup = BeautifulSoup(html, 'html5lib')
    mine_topics = soup.find_all('ul', {'class', 'subcategories span3'})
    mine_numbers = soup.find_all('span', {'class', 'small gray'})
    topic = []
    number = []
    link = []

    for x in mine_topics:
        for y in x:
            topic.append(y.a.string)
            link.append(root + y.a['href'])

    for x in mine_numbers:
        number.append(int(x.string.split()[-2].replace(',', '')))


    link_number_zipped = list(zip(link, number))

    dictionary = {}
    for x in range(len(topic)):
        dictionary[topic[x]] = link_number_zipped[x]

    sorted_dictionary = sorted(dictionary, key=lambda k: dictionary[k][1], reverse=True)
    #print(sorted_dictionary)

    for x in sorted_dictionary:
        final_dict.append(dictionary[x])
        #print(dictionary[x])

    return final_dict
