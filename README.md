# NetTracker

NetTracker es un script en Python que procesa archivos de captura de paquetes (PCAP) y genera archivos KML para visualizar el rastro de IPs geolocalizadas en Google Earth u otros
visualizadores compatibles con KML. Este proyecto es útil para la ciberseguridad y análisis de redes, ayudando a rastrear las rutas de comunicación entre dispositivos.

## Archivos incluidos

- **NetTracker.py**: El código principal que analiza el archivo PCAP y genera un archivo KML.
- **KML tester.py**: Un script adicional para verificar la validez de archivos KML generados.
- **WireSh**: Archivo de ejemplo en formato PCAP para realizar pruebas.
- **test.kml**: Archivo KML de ejemplo generado por NetTracker.py.

## Requisitos previos

- Python 3.12 o Anaconda
- Librerías necesarias: `dpkt`, `socket`, `pygeoip`, `tkinter`

Puedes instalar las librerías necesarias ejecutando:
bash:
`pip install dpkt pygeoip`


#Configuraremos GeoIP
Se requiere la base de datos de GeoLiteCity.Dat, que conseguiremos en: https://github.com/mbcc2006/GeoLiteCity-data
Luego de descargar el archivo se coloca en el mismo directorio que el NetTracker.Py, asi como todos los archivos adjuntos.

Al compilarlo permitira escoger el archivo PCAP a escoger y luego generara el documento test.kml


##KMLTester.py

Este script verifica la validez de archivos KML y puede ser utilizado para comprobar los resultados generados o realizar modificaciones manuales.


##Google Maps

Una vez conseguido el generado el archivo KML, se debe subir en google maps, en `IMPORTAR`, y luego de eso, se podra visualizar el recorrido de los paquetes salidos de la dirección de pruebas.


##Contribuciones
Las contribuciones son bienvenidas. Puedes enviar pull requests o reportar problemas en la sección de Issues.
