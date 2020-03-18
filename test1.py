import pyowm

owm = pyowm.OWM('2082798293e4c7da35d43f11ebce2402', language = "ru")

#from colorama import Fore, Back, Style

#print(Fore.BLACK)
#print(Back.GREEN)

place = input("В каком городе? ")

observation = owm.weather_at_place(place)

w = observation.get_weather()

#print(w)

a = w.get_wind()                  
b = w.get_humidity()              
c = w.get_temperature('celsius')

#print(type(c))

print('Скорость ветра: %d '% a['speed'])
print('Влажность: {}'.format(b ))
print('Температура: %d'% c['temp'])

if c['temp'] > 14:
	print('Заебись, одевай шорты ')
elif c['temp'] > 10:
	print('Тепло, все норм, но в шортах рано')
else:
	print('Холодно, одевайтесь теплее ') 



