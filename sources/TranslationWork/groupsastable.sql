SELECT le.id_concept code, namespace.heading as ns, le.value english ,de.value definition, se.value scopenote, ls.value spanish, "" AS translation
FROM property AS le
JOIN namespace ON le.ns = namespace.id_ns
LEFT JOIN property AS de on le.ns=de.ns AND le.id_concept=de.id_concept AND de.langcode="en" AND de.name="definition"
LEFT JOIN property AS se on le.ns=se.ns AND le.id_concept=se.id_concept AND se.langcode="en" AND se.name="scopeNote"
LEFT JOIN property AS ls on le.ns=ls.ns AND le.id_concept=ls.id_concept AND ls.langcode="es" AND ls.name="prefLabel"
WHERE le.ns in (2,3,4) AND le.langcode="en" AND le.name="prefLabel"
ORDER BY le.ns, le.id_concept
