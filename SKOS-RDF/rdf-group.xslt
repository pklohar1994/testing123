<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns="http://www.eionet.eu.int/gemet/schema.rdf#"
  version="1.0"
>
<xsl:output method="xml" indent="yes"/>
<xsl:strip-space elements="theme"/>

<xsl:template match="/">
   <rdf:RDF>
   <xsl:apply-templates/>
   </rdf:RDF>
</xsl:template>

<!-- Groups -->
<xsl:template match="group">
   <Group rdf:about="urn:gemet:group:{@group-id}" super-group="urn:gemet:super-group:{@super-group-id}" rdfs:label="{.}"/>
</xsl:template>

<!-- Ignore the rest -->
<xsl:template match="text()|@*"/>

</xsl:stylesheet>
