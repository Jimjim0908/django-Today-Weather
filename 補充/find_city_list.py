import urllib.request as ur
import json
"""
url = 'https://www.metaweather.com/api/location/'
url_id = url + 'search/?query=' + 'a'
conn_id = ur.urlopen(url_id)
data_id = conn_id.read()
#(conn.getheader('Content-Type'))確認資料為json
py_data_id = json.loads(data_id) #轉回python資料結構
if py_data_id:
    woeid = (py_data_id[0]['woeid'])
#print(data_id)
print(type(py_data_id))
#print(py_data_id)
"""
url='https://www.metaweather.com/api/location/search/?query='
import string
url_lst = [url + i for i in string.ascii_lowercase[:]]

#print(url_lst)
#print(type(url_lst))

def search(url):
    conn_id = ur.urlopen(url)
    data_id = conn_id.read()
    py_data_id = json.loads(data_id)
    if py_data_id:
        return py_data_id

city_lst = []
for i in range(len(url_lst)):
    obj = search(url_lst[i])
    for j in obj:
        city_lst.append(j['title'])
list(set(city_lst)).sort()


