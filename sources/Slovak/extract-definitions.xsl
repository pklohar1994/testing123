<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
xmlns:c="urn:schemas-microsoft-com:office:component:spreadsheet"
xmlns:html="http://www.w3.org/TR/REC-html40"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
xmlns:x2="http://schemas.microsoft.com/office/excel/2003/xml"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:owl="http://www.w3.org/2002/07/owl#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
version="1.0">
  <xsl:output method="xml"/>

  <xsl:template match="/">
    <dataroot>
          <xsl:apply-templates select="ss:Workbook/ss:Worksheet/ss:Table/ss:Row"/>
    </dataroot>
  </xsl:template>

  <xsl:template match="ss:Workbook/ss:Worksheet/ss:Table/ss:Row">
    <xsl:if test="ss:Cell[4]/ss:Data !=''">
      <Concept>
      <url><xsl:value-of select="ss:Cell[2]/@ss:HRef"/></url>
      <term><xsl:value-of select="ss:Cell[4]/ss:Data"/></term>
      <definition><xsl:value-of select="ss:Cell[6]/ss:Data"/></definition>


      </Concept>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
