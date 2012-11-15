all: uk-definitions.sql uk-terms.sql

uk-definitions.sql: ../TranslationWork/xliff-to-sql.xslt definitions.xliff
	xsltproc ../TranslationWork/xliff-to-sql.xslt definitions.xliff >uk-definitions.sql

uk-terms.sql: ../TranslationWork/xliff-to-sql.xslt terms.xliff
	xsltproc ../TranslationWork/xliff-to-sql.xslt terms.xliff >uk-terms.sql

definitions.xliff: dataroot-to-xliff-defs.xslt terms-definitions.xml
	xsltproc dataroot-to-xliff-defs.xslt terms-definitions.xml >definitions.xliff 

terms.xliff: dataroot-to-xliff-terms.xslt terms-definitions.xml
	xsltproc dataroot-to-xliff-terms.xslt terms-definitions.xml >terms.xliff 
