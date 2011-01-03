<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
     version="1.0">
  <xsl:output method="text"/>

  <xsl:template match="/">
SET NAMES utf8;
DELETE FROM property WHERE ns=1 AND langcode='zh-CN' AND name='prefLabel';
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template match="terms">
INSERT INTO cproperty VALUES (1,<xsl:value-of select="id_concept"/>, 'zh-CN','prefLabel','<xsl:call-template name="globalReplace"><xsl:with-param name="outputString" select="chinese/text()"/></xsl:call-template>', 0);
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
