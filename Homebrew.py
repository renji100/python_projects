import requests
import json
import time
results =[]


'''
    program reads all the installed apps via the Homebrew package manager.
    It will then send individual requests to get analytics data for each of the above app
    Display the results in a sorted format
'''

def read_json_file(fname):
    '''
    read a json file and return the json data
    '''
    with open(fname,'r') as f:
        data = json.load(f)
    return data

def display_analytics(fname,sortcolumn):
    '''
    function displayed the analytics
    '''
    final_data = read_json_file(fname)
    final_data.sort(key = lambda x : x['analytics'][sortcolumn],reverse = True)
    print()
    print('{:>20s} {:>5s} {:>5s} {:>5s}'.format('name','30dcount','90dcount','365dcount'))
    for data in final_data:
        print('{:>20s}  {:>10d} {:>10d} {:>10d} '.format(data['name'],data['analytics']['30d'],data['analytics']['90d'],data['analytics']['365d']))

def json_response(url):
    '''
    function will prepare url requests and return the json response
    '''
    r = requests.get(url)
    pages = r.json()
    return pages

def get_app_analytics(fname,analytics_type):
    data = read_json_file(fname)
    
    for idx,i in enumerate(data):
        app = i['name']
        url = 'https://formulae.brew.sh/api/formula/'+ app+'.json'
        
        
        pages = json_response(url)
        page_dict = {
            'name':app,
            'desc':i['desc'],
            'analytics':{
                '30d':pages['analytics'][analytics_type]['30d'][app],
                '90d':pages['analytics'][analytics_type]['90d'][app],
                '365d':pages['analytics'][analytics_type]['365d'][app],
            }
            }
        results.append(page_dict)
        time.sleep(5)
        
        if idx == 10:
            break

def write_to_file(fname,Obj):
    json_str = json.dumps(Obj,indent = 2)
    f= open(fname,'w')
    print(json_str,file = f)
    f.close()

def save_app_analytics(fname):
    write_to_file(fname,results)
 
def save_app_list(fname,url):
    response_Obj = json_response(url)
    write_to_file(fname,response_Obj)
   


main_url = 'https://formulae.brew.sh/api/formula.json'
main_json_file = 'app_list.json'

analytics_file = 'analytics.json'


while True:
    print('\nq : quit program \n',
           's: save the list of available apps in local file \n',
           'g: save the analytics of each app in local file\n'
           'd: display analytics in the sorting order we want')
    inp_txt = input('\n enter the option a read json from: ')
    if inp_txt == 'q': #quit the program
        break
    if inp_txt == 's':
        save_app_list(main_json_file,main_url) #load main json to file
    if inp_txt == 'g':
        inp_type = 'install'
        inp_type = input('enter analytics type install:install_on_request :')
        get_app_analytics(main_json_file,inp_type) #read the main json file and store in local file
        save_app_analytics(analytics_file)
    if inp_txt == 'd':
        inp_sort = input('enter the sorting option 30d, 90d, 365d: ')
        display_analytics(analytics_file,inp_sort) #sort using 30d or 90d or 365d
