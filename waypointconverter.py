#!/usr/bin/env python

filename = "test.xml"

import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()

namespace = {"ns" : "http://www.topografix.com/GPX/1/1"}

newfile = open("output.js", "w")
newfile.write("var target = UIATarget.localTarget();\n")
newfile.write("var mainWindow = target.frontMostApp().mainWindow();\n")
newfile.write("var points = [\n")

for waypoint in root.findall("ns:wpt", namespace):
    latlong = waypoint.attrib
    lat = latlong["lat"]
    lon = latlong["lon"]
    print(lat)
    print(lon)

    pointstring = "{{ location : {{ latitude : {0}, longitude : {1} }}, \n options: {{speed:8, altitude:200, horizontalAccuracy:10, verticalAccuracy:15}} }},"
    formattedPoint = pointstring.format(lat, lon)
    print formattedPoint

    newfile.write(formattedPoint)
    newfile.write("\n")

newfile.write("];")
newfile.close()

print("all done!")
