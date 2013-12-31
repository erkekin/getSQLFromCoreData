# Copyright (c) 2013 erkekin <erkekin at gmail.com> www.erkekin.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
import os

from xml.dom import minidom

if sys.argv[1].find("xcdatamodeld") != -1:
    path = "%s/%s.xcdatamodel/contents" % (sys.argv[1], os.path.splitext(os.path.basename(sys.argv[1]))[0])
else:
    path = "%s/contents" % (sys.argv[1])

xmldoc = minidom.parse(path)

entity = xmldoc.getElementsByTagName('entity')

string = ''

for tablename in entity:

    columns = tablename.getElementsByTagName('attribute')
    string += 'CREATE TABLE '
    string += tablename.attributes['name'].value
    string += ' ('

    for column in columns:

        string += column.attributes['name'].value

        if column.attributes['attributeType'].value == 'Float':
            string += ' float'
        elif column.attributes['attributeType'].value == 'Boolean':
            string += ' boolean'
        elif column.attributes['attributeType'].value == 'Integer 16':
            string += ' smallint'
        elif column.attributes['attributeType'].value == 'Integer 32':
            string += ' int'
        elif column.attributes['attributeType'].value == 'Integer 64':
            string += ' bigint'
        elif column.attributes['attributeType'].value == 'Decimal':
            string += ' decimal'
        elif column.attributes['attributeType'].value == 'Double':
            string += ' double'
        elif column.attributes['attributeType'].value == 'Binary':
            string += ' binary'
        elif column.attributes['attributeType'].value == 'Transformable':
            string += ' blob'
        elif column.attributes['attributeType'].value == 'Date':
            string += ' date'
        elif column.attributes['attributeType'].value == 'String':
            string += ' varchar(250)'

        if columns[len(columns)-1] != column:
            string += ','

    string += ');\n'

fo = open("create.sql", "wb")

fo.write(string)

fo.close()
