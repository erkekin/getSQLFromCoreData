import sys
import os
from xml.dom.minidom import parseString
from xml.dom import minidom

if sys.argv[1].find("xcdatamodeld") != -1:
	path = "%s/%s.xcdatamodel/contents" % (sys.argv[1],os.path.splitext(os.path.basename(sys.argv[1]))[0])
else:
	path = "%s/contents" % (sys.argv[1])
#print path
xmldoc = minidom.parse(path)
itemlist = xmldoc.getElementsByTagName('attribute') 
entity = xmldoc.getElementsByTagName('entity') 

#CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20)
string  = 'CREATE TABLE '
string += entity[0].attributes['name'].value
string += ' ('

for s in itemlist :
	#print s.attributes['attributeType'].value
	
	string += s.attributes['name'].value
	if s.attributes['attributeType'].value == 'Float':
		
		string += ' float'
	elif 	s.attributes['attributeType'].value == 'Boolean':
		string += ' boolean'
	elif 	s.attributes['attributeType'].value == 'Integer 16':
		string += ' smallint'
	elif 	s.attributes['attributeType'].value == 'Integer 32':
		string += ' int'
	elif 	s.attributes['attributeType'].value == 'Integer 64':
		string += ' bigint'
	elif 	s.attributes['attributeType'].value == 'Decimal':
		string += ' decimal'
	elif 	s.attributes['attributeType'].value == 'Double':
		string += ' double'
	elif 	s.attributes['attributeType'].value == 'Binary':
		string += ' binary'
	elif 	s.attributes['attributeType'].value == 'Transformable':
		string += ' blob'
		
	if s != itemlist[len(itemlist)-1]:
		string += ','
string += ')'	

print string
   # print s.attributes['name'].value, s.attributes['attributeType'].value