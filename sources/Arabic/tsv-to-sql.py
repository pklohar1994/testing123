import csv

filename="Definitions_ARABIC_FINAL.tsv"
namespace=1
langcode = "ar"

print "SET NAMES utf8;"

f = open(filename, 'rb')
fpin = csv.reader(f, delimiter='\t', quotechar='"')
row = fpin.next() # ignore 1st line
for row in fpin:
    if row[4] != '':
        print """INSERT INTO property VALUES (%d, '%s', '%s','definition','%s',0);""" % (namespace, row[0], langcode, row[4])
    #print row[3]

