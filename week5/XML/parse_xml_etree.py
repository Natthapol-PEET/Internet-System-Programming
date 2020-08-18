from xml.etree.ElementTree import parse

# counter CD in USA element ?

doc = parse('cd_catalog.xml')

elem = doc.find("CATALOG")

count_USA = 0

for elem in doc.findall("CD/COUNTRY"):
    if elem.text == 'USA':
        print(elem.text)
        count_USA += 1
    
print('count_USA = ', count_USA)