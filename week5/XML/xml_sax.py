import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startDocument(self):
        print('Document start')

    def startElement(self, name, attrs):
        print('Start: ', name)

    def characters(self, text):
        print('Characters: ', text)

    def endElement(self, name):
        print('End: ', name)

hand = MyHandler()

xml.sax.parse("cd_catalog.xml", hand)