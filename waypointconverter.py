#!/usr/bin/env python

filename = "test.xml"

import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()

namespace = {"ns" : "http://www.topografix.com/GPX/1/1"}

for waypoint in root.findall('ns:wpt', namespace):
    print waypoint.attrib
