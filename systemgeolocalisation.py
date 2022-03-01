
#fonction de conversion
def conversion(d, m, s):
#variable
    degre = d
    minute = m/60
    seconde = s/3600
    dd = degre + minute + seconde
    return dd



#Fonction d'une distance entre un point spécifique et le POLE_NORD
def distance(longitude, latitude):

    longitude_pole_nord = 86
    latitude_pole_nord = 172

    diff_longitude = (longitude - longitude_pole_nord)**2 
    diff_latitude = (latitude - latitude_pole_nord)**2
    distance_des_deux_point = pow(diff_longitude + diff_latitude, 0.5)
    return distance_des_deux_point
#longitude des donnee qu'il faut prendre
longitude = conversion(2, 34, 95)
#latitude des donnee qu'il faut prendre
latitude = conversion(4, 59, 59)
print(longitude, latitude)

resultat = distance(longitude, latitude)

print(resultat)
