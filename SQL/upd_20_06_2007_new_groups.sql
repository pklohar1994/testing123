-- #TODO: All this new groups must be associated to a Super-group

INSERT INTO `concept_group` VALUES (13547, 'en', 'PERSONNEL');
INSERT INTO `concept_group` VALUES (13548, 'en', 'ACTS');
INSERT INTO `concept_group` VALUES (13549, 'en', 'PROGRAMMES');
INSERT INTO `concept_group` VALUES (15028, 'en', 'NOT ACCEPTED TERMS');

UPDATE `concept_group` SET description="КАДРЫ" WHERE id_group=13547 and langcode='ru';
UPDATE `concept_group` SET description="ДОКУМЕНТЫ" WHERE id_group=13548 and langcode='ru';
UPDATE `concept_group` SET description="ПРОГРАММЫ" WHERE id_group=13549 and langcode='ru';
UPDATE `concept_group` SET description="НЕПРИНЯТЫЕ ТЕРМИНЫ" WHERE id_group=15028 and langcode='ru';
