-- This script creates a table with 6 columns: code, english term, english definition, english scope note, spanish term and empty column
-- It does not provide the Spanish definitions
SELECT le.id_concept AS code,
	le.value AS english,
	de.value AS definition,
	se.value AS scopenote,
	ls.value AS lang2term,
	ds.value AS lang2def,
	GROUP_CONCAT(alt.value SEPARATOR ';') AS alternatives
FROM property AS le
LEFT JOIN property AS de ON le.ns=de.ns AND le.id_concept=de.id_concept AND de.langcode="en" AND de.name="definition"
LEFT JOIN property AS se ON le.ns=se.ns AND le.id_concept=se.id_concept AND se.langcode="en" AND se.name="scopeNote"
LEFT JOIN property AS ls ON le.ns=ls.ns AND le.id_concept=ls.id_concept AND ls.langcode="hr" AND ls.name="prefLabel"
LEFT JOIN property AS ds ON le.ns=ds.ns AND le.id_concept=ds.id_concept AND ds.langcode="hr" AND ds.name="definition"
LEFT JOIN property AS alt ON le.ns=alt.ns AND le.id_concept=alt.id_concept AND alt.langcode="hr" AND alt.name="altLabel"
WHERE le.ns=1 AND le.langcode="en" AND le.name="prefLabel"
GROUP BY code
ORDER BY le.id_concept
