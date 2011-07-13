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
  <xsl:output method="text"/>

  <xsl:template match="/">
          <xsl:apply-templates select="ss:Workbook/ss:Worksheet/ss:Table/ss:Row"/>
  </xsl:template>

  <xsl:template match="ss:Workbook/ss:Worksheet/ss:Table/ss:Row">
    <xsl:if test="ss:Cell[4]/ss:Data !=''">
      INSERT INTO property VALUES (5, XX ,"ca","prefLabel", "<xsl:value-of select="normalize-space(ss:Cell[3]/ss:Data)"/>",0);
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
