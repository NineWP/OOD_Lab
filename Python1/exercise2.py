# classification the wind speed 

print(" *** Wind classification ***")
wind_speed = float(input("Enter wind speed (km/h) : "))
classific = ''

if wind_speed >= 209 :
    classific = 'Super Typhoon'
elif wind_speed >= 102 :
    classific = 'Typhoon'
elif wind_speed >= 56 :
    classific = 'Tropical Storm'
elif wind_speed >= 52 : 
    classific = 'Depression'
else :
    classific = 'Breeze'

print("Wind classification is {}.".format(classific))