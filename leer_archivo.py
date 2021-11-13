
from gps import Gps
f = open('Datos_GPS_UPCH.txt','r')

gpgga = []
gps = f.readlines()

for linea in gps:
    
    gpgga_linea = linea.split(",")
    if gpgga_linea[0] == "$GPGGA":
        hrs = gpgga_linea[1]
        latitud = {
            "coor": gpgga_linea[2],
            "posi": "Norte" if gpgga_linea[3] == "N" else "Sur" 
        }
        longitud = {
            "coor": gpgga_linea[4],
            "posi": "Oeste" if gpgga_linea[5] == "W" else "Este"
        }
        gpgga.append(Gps(hrs,latitud,longitud))
    
f.close()


