#-*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import urllib.request as ur
import json
#用城市名搜尋woeid: https://www.metaweather.com/api/location/search/?query=tokyo
#用woeid搜尋氣候資訊: https://www.metaweather.com/api/location/1118370/
def index(request):
    if 'city_name' in request.GET and request.GET['city_name'] !='':
        #從網站擷取woeid
        input = request.GET['city_name']
        url = 'https://www.metaweather.com/api/location/'
        url_id = url + 'search/?query=' + request.GET['city_name']
        conn_id = ur.urlopen(url_id)
        data_id = conn_id.read()
        #(conn.getheader('Content-Type'))確認資料為json
        py_data_id = json.loads(data_id) #轉回python資料結構
        if py_data_id:
            found = True
            woeid = (py_data_id[0]['woeid'])
            #用woeid去擷取氣候資訊
            url_weather = url + str(woeid)
            conn_weather = ur.urlopen(url_weather)
            data_weather = conn_weather.read()
            py_data_weather = json.loads(data_weather)
            #擷取今日氣候
            today_weather = (py_data_weather['consolidated_weather']    [0])
            location = py_data_weather['title']
            timezone = py_data_weather['timezone']
            woied = py_data_weather['woeid']
            date = today_weather['applicable_date']
            weather_state_name = today_weather['weather_state_name']
            weather_state_abbr = today_weather['weather_state_abbr']
            url_pic = "https://www.metaweather.com/static/img/weather/png/{0}.png".format(weather_state_abbr)
            max_temp = "%d" % (today_weather['max_temp'])
            the_temp = "%d" % (today_weather['the_temp'])
            min_temp = "%d" % (today_weather['min_temp'])
            humidity = "%d" % (today_weather['humidity'])
        else:
            error = True    
        return render_to_response('index.html',locals())
    else:
        return render_to_response('index.html',locals())

def city_lst(request):
    city_lst=['Aberdeen', 'Abidjan', 'Addis Ababa', 'Adelaide', 'Ahmedabad', 'Ajaccio', 'Albuquerque', 'Alexandria', 'Amsterdam', 'Anchorage', 'Ankara', 'Athens', 'Atlanta', 'Auckland', 'Austin', 'Baghdad', 'Bakersfield', 'Baltimore', 'Bangalore', 'Bangkok', 'Barcelona', 'Beijing', 'Belfast', 'Berlin', 'Billings', 'Birmingham', 'Blackpool', 'Bogotá', 'Boise', 'Bordeaux', 'Boston', 'Boulder', 'Bournemouth', 'Bradford', 'Brasília', 'Bremen', 'Bridgeport', 'Brighton', 'Brisbane', 'Bristol', 'Brussels', 'Bucharest', 'Budapest', 'Buenos Aires', 'Burlington', 'Busan', 'Cairo', 'Calgary', 'Calvi', 'Cambridge', 'Cape Town', 'Caracas', 'Cardiff', 'Casablanca', 'Charleston', 'Charlotte', 'Chengdu', 'Chennai', 'Cheyenne', 'Chicago', 'Christchurch', 'Cologne', 'Colorado Springs', 'Columbia', 'Columbus', 'Copenhagen', 'Coventry', 'Dallas', 'Damascus', 'Denpasar', 'Denver', 'Derby', 'Des Moines', 'Detroit', 'Dhaka', 'Dongguan', 'Dortmund', 'Dresden', 'Dubai', 'Dublin', 'Dundee', 'Durban', 'Düsseldorf', 'Edinburgh', 'Edmonton', 'El Paso', 'Essen', 'Exeter', 'Falmouth', 'Fargo', 'Fort Worth', 'Frankfurt', 'Fresno', 'Fukuoka', 'Geneva', 'Glasgow', 'Gothenburg', 'Guangzhou', 'Hamburg', 'Hangzhou', 'Hanover', 'Helsinki','Hiroshima', 'Ho Chi Minh City', 'Hong Kong', 'Honolulu', 'Houston', 'Huddersfield', 'Hyderabad', 'Hà Nội', 'Ibadan', 'Indianapolis', 'Ipswich', 'Istanbul', 'Jackson', 'Jacksonville', 'Jakarta', 'Johannesburg', 'Kano', 'Kansas City', 'Karachi', 'Kawasaki', 'Kharkiv', 'Kiev', 'Kingston upon Hull', 'Kinshasa', 'Kirkwall', 'Kitakyushu', 'Kobe', 'Kolkata', 'Kuala Lumpur', 'Kyoto', 'Lagos', 'Lahore', 'Lake Tahoe', 'Las Vegas', 'Leeds', 'Leicester', 'Leipzig', 'Lille', 'Lima', 'Lisbon', 'Little Rock', 'Liverpool', 'London', 'Long Beach', 'Los Angeles', 'Louisville', 'Luton', 'Lyon', 'Madrid', 'Manchester', 'Manila', 'Manukau', 'Maracaibo', 'Marseille', 'Melbourne', 'Memphis', 'Mesa', 'Mexico City', 'Miami', 'Middlesbrough', 'Milan', 'Milwaukee', 'Minneapolis', 'Minsk', 'Mombasa', 'Montréal', 'Moscow', 'Mountain View', 'Mumbai', 'Munich', 'Nagoya', 'Nairobi', 'Naples', 'Nashville', 'New Delhi', 'New Orleans', 'New York', 'Newark', 'Newcastle', 'Nice', 'Northampton', 'Norwich', 'Nottingham', 'Nuremberg', 'Oakland','Oklahoma City', 'Omaha', 'Osaka', 'Oslo', 'Oxford', 'Palm Springs', 'Paris', 'Penzance', 'Perth', 'Philadelphia', 'Phoenix', 'Phuket', 'Plymouth', 'Portland', 'Portsmouth', 'Prague', 'Preston', 'Providence', 'Pune', 'Pyongyang', 'Raleigh', 'Reading', 'Reykjavík', 'Rhyl', 'Richmond', 'Rio de Janeiro', 'Riyadh', 'Rome', 'Sacramento', 'Saitama', 'Salford', 'Salt Lake City', 'Salvador', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose', 'Santa Cruz', 'SantaCruz de Tenerife', 'Santa Fe', 'Santander', 'Santiago', 'Santorini', 'Sapporo', 'Seattle', 'Sendai', 'Seoul', 'Shanghai', 'Sheffield', 'Shenzhen', 'Sidmouth', 'Singapore', 'Sioux Falls', 'Sofia', 'Southend-on-Sea', 'St Ives', 'St Petersburg', 'St. Louis', 'Stockholm', 'Stoke-on-Trent', 'Stuttgart', 'Sunderland', 'Surat', 'Swansea', 'Swindon', 'Sydney', 'São Paulo', 'Taipei', 'Tehrān', 'The Hague', 'Tianjin', 'Tokyo', 'Torino', 'Toronto', 'Toulouse', 'Truro', 'Tucson', 'Vancouver', 'Venice', 'Vienna', 'Virginia Beach', 'Wakefield', 'Warsaw', 'Washington DC', 'Wellington', 'Wichita', 'Wilmington', 'Windhoek', 'Wolverhampton', 'Wuhan', 'Yangon','Yokohama', 'York', 'Zagreb', 'Zurich', 'İzmir'] #scrape from MetaWeather
    return render_to_response('city_list.html',locals())