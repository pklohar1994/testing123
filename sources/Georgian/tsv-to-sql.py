import csv

filename="terms.tsv"
namespace=1
langcode = "ka"

print "SET NAMES utf8;"

f = open(filename, 'rb')
fpin = csv.reader(f, delimiter='\t', quotechar='"')
row = fpin.next() # ignore 1st line
for row in fpin:
    conceptid = row[0]
    term = row[3].strip()
    print """INSERT INTO property VALUES (%d, '%s', '%s','prefLabel','%s',0);""" % (namespace, conceptid, langcode, term)
    #print row[3]

