import csv

filename="terms.tsv"
namespace=1
langcode = "az"

print "SET NAMES utf8;"

f = open(filename, 'rb')
fpin = csv.reader(f, delimiter='\t', quotechar='"')
row = fpin.next() # ignore 1st line
for row in fpin:
    print """INSERT INTO property VALUES (%d, '%s', '%s','prefLabel','%s',0);""" % (namespace, row[0], langcode, row[3])
    #print row[3]

