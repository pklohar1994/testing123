<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xlf="urn:oasis:names:tc:xliff:document:1.1" version="1.0">
  <xsl:output method="text"/>

<!-- Splits texts into prefLabel and altLabel -->

  <xsl:template match="/">
SET NAMES utf8;
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template match="xlf:trans-unit">
    <xsl:call-template name="insertTerms">
      <xsl:with-param name="outputString" select="xlf:target/text()"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="*">
    <xsl:apply-templates />
  </xsl:template>

<!-- Double the apostrophs -->
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

  <xsl:template name="insertTerms">
   <xsl:param name="outputString"/>
    <xsl:choose>
      <xsl:when test="contains($outputString, ';')">
        <xsl:call-template name="insertProperty">
          <xsl:with-param name="outputString" select="substring-before($outputString, ';')"/>
          <xsl:with-param name="property" select="'prefLabel'"/>
        </xsl:call-template>

        <xsl:call-template name="altLabels">
          <xsl:with-param name="outputString" select="substring-after($outputString, ';')"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="insertProperty">
          <xsl:with-param name="outputString" select="$outputString"/>
          <xsl:with-param name="property" select="'prefLabel'"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="insertProperty">
   <xsl:param name="outputString"/>
   <xsl:param name="property"/>
   <xsl:if test="normalize-space($outputString) != ''">
INSERT INTO property VALUES (<xsl:value-of select="substring-after(../../@original,'-')"/>,<xsl:value-of select="@id"/>, '<xsl:value-of select="../../@target-language"/>','<xsl:value-of select="$property"/>','<xsl:call-template name="globalReplace"><xsl:with-param name="outputString" select="normalize-space($outputString)"/></xsl:call-template>', 0);
   </xsl:if>
  </xsl:template>

<!-- Creates altLabels for terms with semicolons -->
  <xsl:template name="altLabels">
    <xsl:param name="outputString" select="."/>
    <xsl:choose>
      <xsl:when test="contains($outputString, ';')">
        <xsl:call-template name="insertProperty">
          <xsl:with-param name="outputString" select="normalize-space(substring-before($outputString, ';'))"/>
          <xsl:with-param name="property" select="'altLabel'"/>
        </xsl:call-template>
        <xsl:call-template name="altLabels">
          <xsl:with-param name="outputString" select="substring-after($outputString, ';')"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
          <xsl:call-template name="insertProperty">
            <xsl:with-param name="outputString" select="$outputString"/>
            <xsl:with-param name="property" select="'altLabel'"/>
          </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>



</xsl:stylesheet>
