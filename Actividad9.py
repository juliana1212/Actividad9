from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
# Variables para los promedios
        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_viento_x = 0
        total_viento_y = 0

#  dirección a grados
        direccion_a_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }


        with open(self.nombre_archivo, 'r') as archivo: #Abrir archivo
            for linea in archivo:
                if "Temperatura:" in linea:
                    temperatura = float(linea.split(":")[1])
                    total_temperatura += temperatura
                elif "Humedad:" in linea:
                    humedad = float(linea.split(":")[1])
                    total_humedad += humedad
                elif "Presion:" in linea:
                    presion = float(linea.split(":")[1])
                    total_presion += presion
                elif "Viento:" in linea:
                    viento_abreviatura = linea.split(":")[1].split(",")[1]
                    viento_grados = direccion_a_grados.get(viento_abreviatura, 0)
                    viento_x = viento_grados
                    viento_y = 1  # Magnitud fija para dirección del viento
                    total_viento_x += viento_x
                    total_viento_y += viento_y

        num_registros = sum(1 for _ in open(self.nombre_archivo))
        temperatura_promedio = total_temperatura / num_registros  #Calcular los promedios
        humedad_promedio = total_humedad / num_registros
        presion_promedio = total_presion / num_registros
        viento_promedio_grados = (180 / 3.141592) * (math.atan2(total_viento_y, total_viento_x))
        
        
        viento_promedio_abreviatura = None
        for abreviatura, grados in direccion_a_grados.items():
            if viento_promedio_grados >= (grados - 11.25) and viento_promedio_grados <= (grados + 11.25):
                viento_promedio_abreviatura = abreviatura
                break

        return (temperatura_promedio, humedad_promedio, presion_promedio, viento_promedio_grados, viento_promedio_abreviatura)

archivo_datos = "DatosMeteorologicos.txt"
datos = DatosMeteorologicos(archivo_datos)
temperatura_promedio, humedad_promedio, presion_promedio, viento_promedio_grados, viento_promedio_abreviatura = datos.procesar_datos()


print(f"La temperatura promedio es : {temperatura_promedio:.1f}°C") #Imprimir y mostrar tempraturas 
print(f"La humedad promedio es: {humedad_promedio:.1f}%")
print(f"La presión promedio es: {presion_promedio:.1f} hPa")
print(f"La velocidad promedio del viento: {viento_promedio_grados:.1f} grados ({viento_promedio_abreviatura})")
