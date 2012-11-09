<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
    xmlns:exsl="http://exslt.org/common" extension-element-prefixes="exsl"
    exclude-result-prefixes = "exsl"
  >

  <xsl:output method="xml"/>

  <xsl:template match="/">
    <xliff xmlns="urn:oasis:names:tc:xliff:document:1.1" version="1.1">
      <file original="gemet-prefLabel-1"
      product-name="Gemet Extraction"
      product-version="1.0"
      datatype="plaintext"
      source-language="en"
      target-language="uk"
      date="2010-01-01T09:16:22Z">
<!--      <xsl:attribute name="mydate"><xsl:value-of select="exsl:date()"/></xsl:attribute> -->
        <header>
</header>
        <body>
          <xsl:apply-templates/>
        </body>
      </file>
    </xliff>
  </xsl:template>

  <xsl:template match="groups|terms-definitions">
    <trans-unit xmlns="urn:oasis:names:tc:xliff:document:1.1">
      <xsl:attribute name="id">
        <xsl:value-of select="code"/>
      </xsl:attribute>
      <source>
        <xsl:value-of select="english"/>
      </source>
      <target>
        <xsl:value-of select="translation"/>
      </target>
    </trans-unit>
  </xsl:template>
  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>
</xsl:stylesheet>
