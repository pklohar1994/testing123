<!DOCTYPE xsl:stylesheet [
        <!ENTITY gemetns "http://www.eionet.eu.int/gemet/">
]>

<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
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
   <skos:Concept  rdf:about="&gemetns;concept/{descriptor-term/@desc-id}">
   <xsl:apply-templates/>
  </skos:Concept>
</xsl:template>

<xsl:template match="broader-term">
   <skos:broader rdf:resource="&gemetns;concept/{@desc-ref-id}"/>
</xsl:template>

<xsl:template match="narrower-term">
   <skos:narrower rdf:resource="&gemetns;concept/{@desc-ref-id}"/>
</xsl:template>

<!-- RELATIONS -->
<xsl:template match="descriptor-related">
 <rdf:Description  rdf:about="&gemetns;concept/{@desc-ref-id}">
 <skos:related rdf:resource="&gemetns;concept/{@rel-desc-ref-id}"/>
 </rdf:Description>
</xsl:template>

<!-- Ignore the rest -->
<xsl:template match="text()|@*"/>

</xsl:stylesheet>
