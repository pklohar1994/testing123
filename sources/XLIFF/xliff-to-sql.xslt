<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xlf="urn:oasis:names:tc:xliff:document:1.1" version="1.0">
  <xsl:output method="text"/>

  <xsl:template match="/">
SET NAMES utf8;
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template match="xlf:trans-unit">
INSERT INTO property VALUES (<xsl:value-of select="substring-after(../../@original,'gemet-prefLabel-')"/>,<xsl:value-of select="@id"/>, '<xsl:value-of select="../../@target-language"/>','prefLabel','<xsl:call-template name="globalReplace"><xsl:with-param name="outputString" select="xlf:target/text()"/></xsl:call-template>');
  </xsl:template>

  <xsl:template match="*">
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template name="globalReplace">
    <xsl:param name="outputString"/>
    <xsl:choose>
      <xsl:when test='contains($outputString,"&apos;")'>
        <xsl:value-of select='concat(substring-before($outputString,"&apos;"),"&apos;&apos;")'/>
        <xsl:call-template name="globalReplace">
          <xsl:with-param name="outputString" select='substring-after($outputString,"&apos;")'/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$outputString"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
