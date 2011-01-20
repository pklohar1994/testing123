#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sparql
import sys, codecs, time

if __name__ == '__main__':


    endpoint = "http://dbpedia.org/sparql"
    s = sparql.Service(endpoint)

    gemetfd = open("dbpedia-results")
    row = gemetfd.readline()
    print "SET NAMES UTF8;"

    while row:
        row = row[:-1] # Drop newline
        res = row.split("\t")
        cid, orgurl = res[0].split(" ")
        print """INSERT IGNORE INTO foreign_relation VALUES (1,%s,"%s","hasWikipediaArticle","%s",1);""" % (cid, res[3],res[2])
        if orgurl.lower() != res[1].lower():
            idType = "relatedMatch"
        else:
            idType = "closeMatch"
        print """INSERT IGNORE INTO foreign_relation VALUES (1,%s,"%s","%s","%s",0);""" % (cid, res[1],idType,res[2])
        row = gemetfd.readline()

    sys.exit()

