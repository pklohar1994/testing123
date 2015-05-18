import csv

filename="groups-themes.tsv"
namespace=1
langcode = "az"

print "SET NAMES utf8;"

nsMap = {'Super groups':2,
      'Groups':3,
      'Themes':4 
  }
f = open(filename, 'rb')
fpin = csv.reader(f, delimiter='\t', quotechar='"')
row = fpin.next() # ignore 1st line
for row in fpin:
    conceptid = row[0]
    term = row[3].strip()
    namespace = nsMap[row[1]]
    print """INSERT INTO property VALUES (%d, '%s', '%s','prefLabel','%s',0);""" % (namespace, conceptid, langcode, term)
    #print row[4]

