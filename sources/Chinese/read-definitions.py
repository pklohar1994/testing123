# -*- coding: utf-8 -*-

FILENAME="GEMET-chinese.txt"

print '''<?xml version="1.0" encoding="UTF-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:1.1" version="1.1">
  <file original="gemet-definition-1"
      product-name="Gemet Extraction"
      product-version="1.0"
      datatype="plaintext"
      source-language="en"
      target-language="zh"
      date="2010-12-17T09:16:22Z">
        <header>
</header>
        <body>'''
f = open(FILENAME)
l = f.readline()
first = True
while l:
    if l[:5] == "Code:":
        if not first:
            print '</trans-unit>'
        print '<trans-unit id="%s">' % l[5:].strip()
        first = False
    elif l[:11] == "Definition:":
        print "  <source>%s</source>" % l[11:].strip()
    elif l[:12] == "Translation:":
        print "  <target>%s</target>" % l[12:].strip()
    l = f.readline()
if not first:
    print '</trans-unit>'
print '''</body>
      </file>
    </xliff>'''
