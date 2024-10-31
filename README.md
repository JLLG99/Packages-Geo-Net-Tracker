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


## Configuraremos GeoIP
Se requiere la base de datos de GeoLiteCity.Dat, que conseguiremos en: https://github.com/mbcc2006/GeoLiteCity-data
Luego de descargar el archivo se coloca en el mismo directorio que el NetTracker.Py, asi como todos los archivos adjuntos.

Al compilarlo permitira escoger el archivo PCAP a escoger y luego generara el documento test.kml


## KMLTester.py

Este script verifica la validez de archivos KML y puede ser utilizado para comprobar los resultados generados o realizar modificaciones manuales.


## Google Maps

Una vez conseguido el generado el archivo KML, se debe subir en google maps, en `IMPORTAR`, y luego de eso, se podra visualizar el recorrido de los paquetes salidos de la dirección de pruebas.


##Contribuciones
Las contribuciones son bienvenidas. Puedes enviar pull requests o reportar problemas en la sección de Issues.


# English

# NetTracker

NetTracker is a Python script that processes packet capture (PCAP) files and generates KML files to visualize the trace of geolocated IPs in Google Earth or other KML-compatible viewers. 
This project is useful for cybersecurity and network analysis, helping to track communication routes between devices.

## Included Files

- **NetTracker.py**: The main script that analyzes the PCAP file and generates a KML file.
- **KML tester.py**: An additional script to verify the validity of generated KML files.
- **WireSh**: Example file in PCAP format for testing.
- **test.kml**: Sample KML file generated by NetTracker.py.

## Prerequisites

- Python 3.12 or Anaconda
- Required libraries: `dpkt`, `socket`, `pygeoip`, `tkinter`

You can install the necessary libraries by running:
bash:
`pip install dpkt pygeoip`

##GeoIP Configuration
The project requires the GeoLiteCity.dat database, which can be obtained from [here](https://github.com/mbcc2006/GeoLiteCity-data).
Once downloaded, place the file in the same directory as NetTracker.py, along with all additional files.

When you run the script, it will prompt you to select a PCAP file and will then generate the test.kml document.

##KMLTester.py
This script verifies the validity of KML files and can be used to check generated results or make manual modifications.

##Google Maps
Once the KML file is generated, you can upload it to Google Maps under the IMPORT option to visualize the trace of packets sent from the test address.

##Contributions
Contributions are welcome. You can submit pull requests or report issues in the Issues section.


### Notes
Make sure to replace or modify any specific details if required based on the user’s preferences or if additional functionalities are added later. 
Let me know if you need further adjustments!

