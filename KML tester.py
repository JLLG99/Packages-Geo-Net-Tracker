import xml.etree.ElementTree as ET


def validar_kml(kml_string):
    try:
        # Analiza el KML
        root = ET.fromstring(kml_string)

        # Verifica que el KML tenga el espacio de nombres correcto
        if root.tag != '{http://www.opengis.net/kml/2.2}kml':
            return "Error: El archivo KML no tiene el espacio de nombres correcto."

        # Verifica la existencia del elemento Document
        document = root.find('{http://www.opengis.net/kml/2.2}Document')
        if document is None:
            return "Error: No se encontró el elemento <Document>."

        # Verifica que contenga al menos un Placemark
        placemarks = document.findall('{http://www.opengis.net/kml/2.2}Placemark')
        if len(placemarks) == 0:
            return "Error: No se encontraron elementos <Placemark>."

        # Verifica la estructura básica de los Placemark
        for placemark in placemarks:
            name = placemark.find('{http://www.opengis.net/kml/2.2}name')
            coordinates = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates')
            if name is None or coordinates is None:
                return "Error: Un <Placemark> no tiene un <name> o <coordinates>."

        return "El archivo KML es válido."

    except ET.ParseError as e:
        return f"Error: El archivo KML no es válido. {str(e)}"


# Ejemplo de uso
kml_string = """TEXTO KML"""

resultado = validar_kml(kml_string)
print(resultado)
