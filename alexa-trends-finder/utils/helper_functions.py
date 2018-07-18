from utils import url_finder


################################################################################
####################### Function calls for type of analysis ####################
################################################################################

def light_analysis(url):
    name = url.split('/')[-1]
    file = open(name +'-root-tree.txt', '+w',  encoding="utf-8")
    a = url_finder.find_em(url)

    for key, value in a:
        print('{:80s} is cited {:10d} times'.format(key, value))
        file.write('{:80s} is cited {:10d} times'.format(key, value))
        file.write('\n')




def in_depth_analysis(url):
    name = url.split('/')[-1]
    file = open(name+'-in-depth.txt', '+w',  encoding="utf-8")

    temp_dict = url_finder.find_em(url)

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
                temp_dict2 = url_finder.find_em(temp_dict[x][0])
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
                    temp_dict3 = url_finder.find_em(temp_dict2[y][0])
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
