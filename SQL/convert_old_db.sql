ALTER TABLE `scope` CHANGE `scope_note` `scope_note` BLOB;
ALTER TABLE `scope` CHANGE `scope_note` `scope_note` text CHARACTER SET utf8;

ALTER TABLE `scope` CHANGE `definition` `definition` BLOB;
ALTER TABLE `scope` CHANGE `definition` `definition` text CHARACTER SET utf8;

ALTER TABLE `concept_group` CHANGE `description` `description` BLOB;
ALTER TABLE `concept_group` CHANGE `description` `description` text CHARACTER SET utf8;

ALTER TABLE `scope_history` CHANGE `record` `record` BLOB;
ALTER TABLE `scope_history` CHANGE `record` `record` text CHARACTER SET utf8;

ALTER TABLE `scope_history` CHANGE `author` `author` BLOB;
ALTER TABLE `scope_history` CHANGE `author` `author` text CHARACTER SET utf8;

ALTER TABLE `term` CHANGE `name` `name` BLOB;
ALTER TABLE `term` CHANGE `name` `name` text CHARACTER SET utf8;

ALTER TABLE `term_history` CHANGE `name` `name` BLOB;
ALTER TABLE `term_history` CHANGE `name` `name` text CHARACTER SET utf8;

ALTER TABLE `term_history` CHANGE `author` `author` BLOB;
ALTER TABLE `term_history` CHANGE `author` `author` text CHARACTER SET utf8;

ALTER TABLE `theme` CHANGE `description` `description` BLOB;
ALTER TABLE `theme` CHANGE `description` `description` text CHARACTER SET utf8;

ALTER TABLE `source` CHANGE `description` `description` BLOB;
ALTER TABLE `source` CHANGE `description` `description` text CHARACTER SET utf8;