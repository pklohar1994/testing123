<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
 exclude-result-prefixes="o"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:od="urn:schemas-microsoft-com:officedata"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="resultset">
  <dataroot xsi:noNamespaceSchemaLocation="terms-definitions.xsd">
   <xsl:apply-templates/>
  </dataroot>
  </xsl:template>

  <xsl:template match="row">
  <terms-definitions>
   <xsl:apply-templates/>
  </terms-definitions>
  </xsl:template>

  <xsl:template match="field">
   <xsl:element name="{@name}">
    <xsl:value-of select="text()"/>
   </xsl:element>
  </xsl:template>

</xsl:stylesheet>
