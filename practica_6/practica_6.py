from pyzipcode import ZipCodeDatabase
from math import pi,sqrt,sin,cos,atan2

zips = ZipCodeDatabase()

def findLoc(zipCode):
    return zips[zipCode]

def findZIP(city, state):
    return zips.find_zip(city,state)

def findDist(fZip,sZip):
    lat1 = zips[fZip].latitude
    long1 = zips[fZip].longitude
    lat2 = zips[sZip].latitude
    long2 = zips[sZip].longitude

    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    mi = 3956 * c
    return [round(km,2),round(mi,2)]

while True:
    command = input("Введите команду ('loc, 'zip', 'dist', 'end') => ")
    if(command.lower() == 'end' ):
        break

    elif(command.lower() == 'loc'):
        try:
            zipCode = input("Введите ZIP код => ")
            out = findLoc(zipCode)
            print(f'ZIP: {out.zip} - {out.city}, {out.state}.')
        except:
            print("Неверно введен ZIP код")

    elif(command.lower() == 'zip'):
        try:
            cityName = input("Введите название города => ")
            stateName = input("Введите название штата => ")
            out = findZIP(cityName,stateName)
            outZips = ""
            for i in out:
                outZips += i.zip + " "
            print(f'ZIP по {cityName} {stateName} : {outZips}')
        except :
            print("Неверно введены данные")


    elif(command.lower() == 'dist'):
        try:
            zipCodeF = input("Введите 1 ZIP код => ")
            zipCodeS = input("Введите 2 ZIP код => ")
            out = findDist(zipCodeF,zipCodeS)
            print(f'Расстояние между {zipCodeF} и {zipCodeS} = {out[0]}км.({out[1]}миль.)')
        except:
            print("Неверно введены ZIP коды")

    else:
        print(f"Неизвестная команда -> '{command}'")