import xml.etree.ElementTree as ET


txt = open('output/out.txt','w')
tree = ET.parse('item.xml')
items = tree.getroot()

illness_o=''

count = 0
for item in items:
    for child in item:
        if child.tag=='illness':
            for value in child:
                illness_o = value.text
        elif child.tag == 'name':
            for value in child:
                count = count + 1
                #if count>=1000 :
                print illness_o+'   '+value.text


print count
