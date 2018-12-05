import requests
from bs4 import BeautifulSoup


r = requests.get('https://search.naver.com/search.naver?ie=UTF-8&query=%ED%8C%90%EA%B5%90+%EB%82%A0%EC%94%A8#')
bsObj = BeautifulSoup(r.text, 'html.parser')
current_temperature = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p > span.todaytemp')[0].text + u"\u2103"
info = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(1) > p')[0].text
min_temperature = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(2) > span.merge > span.min > span')[0].text
max_temperature = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(2) > span.merge > span.max > span')[0].text
sensible = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(2) > span.sensible')[0].text

indicator = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(3) > span')[0].text
dust = bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl')[0]
dust = list(dust.children)
fine_particulate_matter = dust[1].text + dust[3].text
ultra_fine_particulate_matter = dust[5].text + dust[7].text
ozone = dust[9].text + dust[11].text

temperature = '{0}/{1} {2}'.format(min_temperature, max_temperature, sensible)
l = [current_temperature, info, temperature, indicator, fine_particulate_matter, ultra_fine_particulate_matter, ozone]
result = '\n'.join(l)
print(result)
'''
week = []
for day in list(bsObj.select('#main_pack > div.sc.cs_weather._weather > div:nth-of-type(2) > div.weather_box > div.weather_area._mainArea > div.table_info.weekly._weeklyWeather > ul:nth-of-type(2)')[0].children)[1::2]:
    week.append([item.text.strip() for item in list(day.children)[1::2]])

print(week)
'''
