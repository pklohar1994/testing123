<!DOCTYPE xsl:stylesheet [
        <!ENTITY gemetns "http://www.eionet.eu.int/gemet/">
]>

<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns:gemet="http://www.eionet.eu.int/gemet/2004/06/gemet-schema.rdf#"
  version="1.0"
>
<xsl:output method="xml" indent="yes"/>

<xsl:template match="/">
   <rdf:RDF>
   <xsl:apply-templates/>
   </rdf:RDF>
</xsl:template>

<!-- DESCRIPTORS -->
<xsl:template match="descriptor">
   <rdf:Description  rdf:about="&gemetns;concept/{descriptor-term/@desc-id}">
   <xsl:apply-templates/>
  </rdf:Description>
</xsl:template>

<xsl:template match="theme">
   <gemet:theme rdf:resource="&gemetns;theme/{@theme-id}"/>
</xsl:template>
  
<xsl:template match="group">
   <gemet:group rdf:resource="&gemetns;group/{@group-id}"/>
</xsl:template>

<!-- Ignore the rest -->
<xsl:template match="text()|@*"/>

</xsl:stylesheet>
