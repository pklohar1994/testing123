.SUFFIXES: .xml .rdf

all: gemet-skoscore.rdf gemet-backbone.rdf gemet_ENG.rdf

gemet-backbone.rdf: gemet_ENG.xml rdf-backbone.xslt
	xsltproc -o $@ rdf-backbone.xslt gemet_ENG.xml

gemet-skoscore.rdf: gemet_ENG.xml rdf-gemet-skoscore.xslt
	xsltproc -o $@ rdf-gemet-skoscore.xslt gemet_ENG.xml

gemet-supergroup.rdf: gemet_ENG.xml rdf-supergroup.xslt
	xsltproc -o $@ rdf-supergroup.xslt gemet_ENG.xml

.xml.rdf: rdf-light.xslt
	@$(RM) $@
	xsltproc -o $@ rdf-light.xslt $<
	@echo Remember to set the language code on the RDF file

clean:
	-rm gemet-supergroup.rdf gemet-skoscore.rdf gemet-backbone.rdf gemet_ENG.rdf
