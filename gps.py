from os import times


class Gps:
    
    def __init__(self,hrs,latitud,longitud) -> None:
        self.horas = hrs
        self.latitud = latitud
        self.longitud = longitud


    @property
    def getHoras(self):

        return self.horas

    def hrs(self):
        tiempo = self.horas
        hrs = tiempo[:2]
        min = tiempo[2:4]
        sec = tiempo[4:]
        return f"{hrs}:{min}:{sec}"
    
    def getLatitud(self):
        digito = self.latitud["coor"]
        first_number = digito[:2]
        second_numbers = digito[2:]
        latitud_min_sec = float(first_number) + (float(second_numbers)/60.0)
        #latitud_min_sec = float(digito[0:2]) + float((digito[2:]/60))
        return str(latitud_min_sec)
    

    def conversion_grados_min_sec_latitud(self):
         digito = str(self.getLatitud()).split(".")
         print(f"digito: {digito}")
         #obtencion de los grados
         grados = digito[0]

         #calcular minutos
         min = (float("0."+digito[1]) * 60) / 1
         #calcular segundos
         split_min = str(min).split(".")
         sec = (float("0."+str(split_min[1]))*60) /1

         return f"{grados}° {min}' {sec}'' {self.latitud['posi']}"


    def getLongitud(self):
        digito = self.longitud["coor"]
        first_numbers = digito[:3]
        second_numbers = digito[3:]
        longitud_min_sec = float(first_numbers) + (float(second_numbers)/60)
        #logintud_min_sec = int(digito[0:3]) + (digito[3:]/60)
        #print(digito)
        return str(longitud_min_sec)
    
    def conversion_grados_min_sec_longitud(self):
        digito = str(self.getLongitud()).split(".")
        grados = digito[0]

         #calcular minutos
        min = (float("0."+digito[1]) * 60) / 1
        #calcular segundos
        split_min = str(min).split(".")
        sec = (float("0."+str(split_min[1]))*60) /1

        return f"{grados}° {min}' {sec}''{self.longitud['posi']}"
    

    

    def __str__(self) -> str:
        return f'hrs: {self.horas} - latitud: {self.latitud} - longitud: {self.longitud}'
