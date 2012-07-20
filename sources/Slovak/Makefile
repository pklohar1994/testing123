all: sk-definitions.sql sk-preflabels.sql

sk-preflabels.sql: sql-terms.xsl GEMET-revised_terms.xml
	xsltproc sql-terms.xsl GEMET-revised_terms.xml >sk-preflabels.sql
sk-definitions.sql: sql-definitions.xsl DEFINITIONS_final.xml
	xsltproc sql-definitions.xsl DEFINITIONS_final.xml >sk-definitions.sql
