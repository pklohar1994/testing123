ALTER TABLE `status` CHANGE `description` `description` varchar(50) CHARACTER SET utf8;

ALTER TABLE `concept_group` DROP FOREIGN KEY `concept_group_ibfk_1`;
ALTER TABLE `concept_group` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `scope` DROP FOREIGN KEY `scope_ibfk_2`;
ALTER TABLE `scope` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `scope_history` DROP FOREIGN KEY `scope_history_ibfk_2`;
ALTER TABLE `scope_history` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `term` DROP FOREIGN KEY `term_ibfk_2`;
ALTER TABLE `term` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `term_history` DROP FOREIGN KEY `term_history_ibfk_3`;
ALTER TABLE `term_history` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `theme` DROP FOREIGN KEY `theme_ibfk_1`;
ALTER TABLE `theme` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;

ALTER TABLE `language` CHANGE `langcode` `langcode` varchar(10) CHARACTER SET utf8;
ALTER TABLE `language` CHANGE `language` `language` varchar(255) CHARACTER SET utf8;
ALTER TABLE `language` CHANGE `charset` `charset` varchar(100) CHARACTER SET utf8;
ALTER TABLE `language` CHANGE `alt_langcode` `alt_langcode` char(3) CHARACTER SET utf8;

DELETE FROM `language`;

INSERT INTO `language` VALUES ('bg','Bulgarian','utf8_general_ci','BUL'),('cs','Czech','utf8_czech_ci','CZE'),('da','Danish','utf8_danish_ci','DAN'),('de','German','utf8_general_ci','GER'),('el','Greek','utf8_general_ci','GRE'),('en','English','utf8_general_ci','ENG'),('en-US','English (United States)','utf8_general_ci','USA'),('es','Spanish','utf8_spanish_ci','SPA'),('et','Estonian','utf8_estonian_ci','EST'),('eu','Basque','utf8_general_ci','BAQ'),('fi','Finnish','utf8_general_ci','FIN'),('fr','French','utf8_general_ci','FRE'),('hu','Hungarian','utf8_general_ci','HUN'),('it','Italian','utf8_general_ci','ITA'),('nl','Dutch','utf8_general_ci','DUT'),('no','Norwegian','utf8_general_ci','NOR'),('pl','Polish','utf8_polish_ci','POL'),('pt','Portuguese','utf8_general_ci','POR'),('ru','Russian','utf8_general_ci','RUS'),('sk','Slovak','utf8_slovak_ci','SLO'),('sl','Slovenian','utf8_slovenian_ci','SLV'),('sv','Swedish','utf8_swedish_ci','SVE');

ALTER TABLE `concept_group` ADD CONSTRAINT `concept_group_ibfk_1` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);
ALTER TABLE `scope` ADD CONSTRAINT `scope_ibfk_2` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);
ALTER TABLE `scope_history` ADD CONSTRAINT `scope_history_ibfk_2` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);
ALTER TABLE `term` ADD CONSTRAINT `term_ibfk_2` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);
ALTER TABLE `term_history` ADD CONSTRAINT `term_history_ibfk_3` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);
ALTER TABLE `theme` ADD CONSTRAINT `theme_ibfk_1` FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);