SET @secondlang = 'ru';

SELECT le.id_concept code, namespace.heading as ns, le.value AS english,
    ls.value AS lang2term,
    "" AS translation
FROM property AS le
JOIN namespace ON le.ns = namespace.id_ns
LEFT JOIN property AS ls on le.ns=ls.ns AND le.id_concept=ls.id_concept AND ls.langcode=@secondlang AND ls.name="prefLabel"
WHERE le.ns in (2,3,4) AND le.langcode="en" AND le.name="prefLabel"
ORDER BY le.ns, le.id_concept + 0
