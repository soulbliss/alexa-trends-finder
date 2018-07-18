from bs4 import BeautifulSoup
import urllib.request


################################################################################
############# Algorithm for scraping and sorting a given Alexa url page ########
################################################################################

def find_em(url):
    name = url.split('/')[-1]
    final_dict = []
    root = 'https://www.alexa.com'
    with urllib.request.urlopen(url) as response:
        html = response.read()

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

################################################################################
####################### Function call of find_em ###############################
################################################################################

def call_one_only(url):
    name = url.split('/')[-1]
    file = open(name +'-root-tree.txt', '+w')
    a = find_em(url)

    for key, value in a:
        print('{:80s} is cited {:10d} times'.format(key, value))
        file.write('{:80s} is cited {:10d} times'.format(key, value))
        file.write('\n')


################################################################################
################################ The Main Method ###############################
################################################################################

def main(url):
    name = url.split('/')[-1]
    file = open(name+'-in-depth.txt', '+w',  encoding="utf-8")

    temp_dict = find_em(url)

    #loops over the first five categories
    for x in range(5):
        try:
            print(temp_dict[x][0])
            file.write(temp_dict[x][0])
            file.write('\n')
        except Exception as e:
            print('there are less than '+str(x+1) +'categories')
            file.write('there are less than ' + str(x + 1) + ' expected categories')
            file.write('\n')

        #extracts links of the first five categories for each of the parent link.
        for y in range(5):
            try:
                temp_dict2 = find_em(temp_dict[x][0])
                print(temp_dict2[y][0])
                file.write(temp_dict2[y][0])
                file.write('\n')
            except Exception as e:
                print('there are less than ' + str(x+1) + ' categories')
                file.write('there are less than ' + str(x + 1) + ' expected categories')
                file.write('\n')

            #scrapes details of the first five categories of the last branch in the tree.
            for z in range(5):
                try:
                    temp_dict3 = find_em(temp_dict2[y][0])
                    print(temp_dict3[z][0])
                    file.write(temp_dict3[z][0])
                    file.write('\n')
                except Exception as e:
                    print('there are less than ' + str(x+1) + ' categories')
                    file.write('there are less than '+ str(x+1) +' expected categories')
                    file.write('\n')

            print('*' * 10)
            file.write('*********************')
            file.write('\n')

        print('*' * 20, '\n')
        file.write('**************************************')
        file.write('\n')



if __name__ == '__main__':
    call_one_only('https://www.alexa.com/topsites/category/Top/Computers/Artificial_Intelligence')
    main(url)
