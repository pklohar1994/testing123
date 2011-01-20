#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1"

import sparql
import sys, codecs, time

if __name__ == '__main__':

    querytemplate = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?subj ?redir ?label ?redirwiki ?wiki
WHERE { ?subj rdfs:label "%s"@en .
        OPTIONAL { ?subj <http://dbpedia.org/ontology/wikiPageRedirects> ?redir .
                ?redir rdfs:label ?label .
                ?redir foaf:page ?redirwiki .
                FILTER (LANG(?label) = "en")
        } .
        OPTIONAL { ?subj foaf:page ?wiki }
}
"""
    c = codecs.getwriter("utf-8")
    sys.stdout = c(sys.stdout, 'replace')

    endpoint = "http://dbpedia.org/sparql"
    s = sparql.Service(endpoint)

    gemetfd = open("list-gemet-terms")
    conceptline = gemetfd.readline()
    while conceptline:
        conceptline = conceptline[:-1] # Drop newline
        cid, term = conceptline.split("\t")
        term = term[0].upper() + term[1:]
        print >> sys.stderr, "QueryinG:", term
        conceptline = gemetfd.readline()
        q = querytemplate % term
        result = s.query(q)
        for row in result.values():
            if row[0].find("Category:") >= 0: continue
            if row[1] is None:
                print >> sys.stderr, cid, row[0], row[1]
                print "%s %s\t%s\t%s\t%s" % (cid, row[0], row[0], term, row[4])
            else:
                print >> sys.stderr, cid, row[0], row[0]
                print "%s %s\t%s\t%s\t%s" % (cid, row[0], row[1], row[2], row[3])
#               print cid, "\t".join(map(unicode,row))
        time.sleep(3)

    sys.exit()

