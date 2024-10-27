import dpkt
import socket
import pygeoip
from tkinter import Tk
from tkinter.filedialog import askopenfilename

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('TU IP PUBLICA')
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
                  '<Placemark>\n'
                  '<name>%s</name>\n'
                  '<extrude>1</extrude>\n'
                  '<tessellate>1</tessellate>\n'
                  '<styleUrl>#transBluePoly</styleUrl>\n'
                  '<LineString>\n'
                  '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
                  '</LineString>\n'
                  '</Placemark>\n'
              ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''


def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts += KML
        except:
            pass
    return kmlPts


def main():
    # Abrir el explorador de archivos
    Tk().withdraw()  # Ocultar la ventana Tkinter
    filepath = askopenfilename(title="Selecciona el archivo pcap", filetypes=[("Archivos pcap", "*.pcap")])

    if not filepath:
        print("No se seleccionó ningún archivo.")
        return

    with open(filepath, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                    '<Style id="transBluePoly">' \
                    '<LineStyle>' \
                    '<width>1.5</width>' \
                    '<color>501400E6</color>' \
                    '</LineStyle>' \
                    '</Style>'
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

    # Guardar el resultado en un archivo test.kml
    with open('test.kml', 'w') as kmlfile:
        kmlfile.write(kmldoc)
    print("Archivo test.kml generado exitosamente.")


if __name__ == '__main__':
    main()
