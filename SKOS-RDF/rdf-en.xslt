<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns="http://www.eionet.eu.int/gemet/2004/06/gemet-schema.rdf#"
  version="1.0"
>
<xsl:output method="xml" indent="yes"/>

<xsl:template match="/">
   <rdf:RDF>
   <xsl:apply-templates/>
   </rdf:RDF>
</xsl:template>

<!-- SUPER GROUPS -->
<xsl:template match="super-group">
   <SuperGroup rdf:about="urn:gemet:super-group:{@super-group-id}">
   <xsl:apply-templates/>
   </SuperGroup>
</xsl:template>

<xsl:template match="super-group-name">
   <rdfs:label><xsl:value-of select="."/></rdfs:label>
</xsl:template>

<!-- DESCRIPTORS -->
<xsl:template match="descriptor">
   <skos:Concept  rdf:about="urn:gemet:descriptor:{descriptor-term/@desc-id}">
   <xsl:apply-templates/>
  </skos:Concept>
</xsl:template>

<xsl:template match="descriptor-term">
   <rdfs:label><xsl:value-of select="."/></rdfs:label>
</xsl:template>

<xsl:template match="definition">
   <skos:definition><xsl:value-of select="."/></skos:definition>
</xsl:template>


<xsl:template match="broader-term">
   <skos:broader rdf:resource="urn:gemet:descriptor:{@desc-ref-id}"/>
</xsl:template>
<xsl:template match="narrower-term">
   <skos:narrower rdf:resource="urn:gemet:descriptor:{@desc-ref-id}"/>
</xsl:template>

<xsl:template match="theme">
   <theme rdf:resource="urn:gemet:theme:{@theme-id}"/>
</xsl:template>
  
<xsl:template match="group">
   <group rdf:resource="urn:gemet:group:{@group-id}"/>
</xsl:template>

<!-- RELATIONS -->
<xsl:template match="descriptor-related">
 <rdf:Description  rdf:about="urn:gemet:descriptor:{@desc-ref-id}">
 <skos:related rdf:resource="urn:gemet:descriptor:{@rel-desc-ref-id}"/>
 </rdf:Description>
</xsl:template>

<!-- Ignore the rest -->
<xsl:template match="text()|@*"/>

</xsl:stylesheet>
