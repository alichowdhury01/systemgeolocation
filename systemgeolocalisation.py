
#fonction de conversion
def conversion(d, m, s):
#variable
    degre = d
    minute = m/60
    seconde = s/3600
    dd = degre + minute + seconde
    return dd

#longitude des donnee qu'il faut prendre
longitude = conversion(2, 34, 95)
#latitude des donnee qu'il faut prendre
latitude = conversion(4, 59, 59)
print(longitude and latitude )