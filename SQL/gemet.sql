CREATE DATABASE `GEMET`
  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `GEMET`;


#
#  General structure of the database
#

CREATE TABLE `concept` (
  `id_concept` int(11) default '0',
  `id_group` int(11) default '0',
  `id_status` varchar(1) default '',
  `datent` datetime default '0000-00-00 00:00:00',
  `datchg` datetime default '0000-00-00 00:00:00',
  PRIMARY KEY  (`id_concept`),
  KEY `id_group` (`id_group`),
  KEY `id_status` (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Contains all terms';

CREATE TABLE `language` (
  `langcode` varchar(10) default '',
  `language` varchar(255) default '',
  `charset` varchar(10) default '',
  `alt_langcode` varchar(5) default '',
  PRIMARY KEY  (`langcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Dictionary table for languages';

CREATE TABLE `rel_type` (
  `id_type` varchar(2) default '',
  `description` varchar(255) default '',
  PRIMARY KEY  (`id_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Dictionary table for types of relations among concepts';

CREATE TABLE `relation` (
  `id_concept` int(11) default '0',
  `id_relation` int(11) default '0',
  `id_type` varchar(2) default '',
  PRIMARY KEY  (`id_concept`,`id_relation`),
  KEY `id_concept` (`id_concept`),
  KEY `id_relation` (`id_relation`),
  KEY `id_type` (`id_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Defines relations among the concepts: narrower, broader and related';

CREATE TABLE `scope` (
  `id_concept` int(11) default '0',
  `langcode` varchar(10) default '',
  `scope_note` text,
  `definition` text,
  PRIMARY KEY  (`id_concept`,`langcode`),
  KEY `langcode` (`langcode`),
  KEY `id_concept` (`id_concept`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Holds scope notes for concepts';

CREATE TABLE `status` (
  `id_status` varchar(1) default '',
  `description` varchar(50) default '',
  PRIMARY KEY  (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Dictionary table for concepts statuses: new, changed, delete';

CREATE TABLE `concept_group` (
  `id_group` int(11) default '0',
  `langcode` varchar(10) default '',
  `description` text,
  PRIMARY KEY  (`id_group`,`langcode`),
  KEY `id_group` (`id_group`),
  KEY `langcode` (`langcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Group definitions table, one of ways to categorise concepts';

CREATE TABLE `super_group` (
  `id_group` int(11) NOT NULL default '0',
  `id_super_group` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id_group`,`id_super_group`),
  KEY `id_group` (`id_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Contains the super-groups ids';

CREATE TABLE `scope_history` (
  `id_scope_history` int(11) auto_increment,
  `id_concept` int(11) default '0',
  `record` text,
  `langcode` varchar(10) default '',
  `author` text,
  `record_type` char(2) default '',
  `id_status` varchar(1) default '',
  `datchg` datetime default '0000-00-00 00:00:00',
  PRIMARY KEY  (`id_scope_history`),
  UNIQUE KEY `id` (`id_scope_history`),
  KEY `langcode` (`langcode`),
  KEY `id_concept` (`id_concept`),
  KEY `id_status` (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='History table for scopes';

CREATE TABLE `term` (
  `id_concept` int(11) default '0',
  `name` text,
  `langcode` varchar(10) default '',
  PRIMARY KEY  (`id_concept`,`langcode`),
  KEY `id_concept` (`id_concept`),
  KEY `langcode` (`langcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Main table for terms, each record storing the term and its description';

CREATE TABLE `term_history` (
  `id_term_history` int(11) auto_increment,
  `id_concept` int(11) default '0',
  `name` text,
  `langcode` varchar(10) default NULL,
  `author` text,
  `id_status` varchar(1) default '',
  `datchg` datetime default '0000-00-00 00:00:00',
  PRIMARY KEY  (`id_term_history`),
  KEY `langcode` (`langcode`),
  KEY `id_concept` (`id_concept`),
  KEY `id_status` (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='History of terms modifications';

CREATE TABLE `theme` (
  `id_theme` int(11) default '0',
  `accronym` varchar(50) default '',
  `langcode` varchar(10) default '',
  `description` text,
  PRIMARY KEY  (`id_theme`,`langcode`),
  KEY `langcode` (`langcode`),
  KEY `id_theme` (`id_theme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Theme descriptions';

CREATE TABLE `concept_theme` (
  `id_concept` int(11) default '0',
  `id_theme` int(11) default '0',
  PRIMARY KEY  (`id_concept`,`id_theme`),
  KEY `id_theme` (`id_theme`),
  KEY `id_concept` (`id_concept`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Theme relations';

CREATE TABLE `source` (
  `id_source` int(11) auto_increment,
  `id_concept` int(11) default '0',
  `description` text,
  PRIMARY KEY (`id_source`),
  KEY `id_concept` (`id_concept`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Source descriptions';


#
#  Foreign keys for table concept
#

ALTER TABLE `concept`
  ADD FOREIGN KEY (`id_status`) REFERENCES `status` (`id_status`),
  ADD FOREIGN KEY (`id_group`) REFERENCES `concept_group` (`id_group`);

ALTER TABLE `concept_theme`
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`),
  ADD FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id_theme`);

ALTER TABLE `concept_group`
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);

ALTER TABLE `relation`
  ADD FOREIGN KEY (`id_type`) REFERENCES `rel_type` (`id_type`),
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`);

ALTER TABLE `scope`
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`),
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);

ALTER TABLE `scope_history`
  ADD FOREIGN KEY (`id_status`) REFERENCES `status` (`id_status`),
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`),
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`);

ALTER TABLE `source`
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`);

ALTER TABLE `super_group`
  ADD FOREIGN KEY (`id_group`) REFERENCES `concept_group` (`id_group`);

ALTER TABLE `term`
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`),
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);

ALTER TABLE `term_history`
  ADD FOREIGN KEY (`id_status`) REFERENCES `status` (`id_status`),
  ADD FOREIGN KEY (`id_concept`) REFERENCES `concept` (`id_concept`),
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);

ALTER TABLE `theme`
  ADD FOREIGN KEY (`langcode`) REFERENCES `language` (`langcode`);


#
#  Default data
#

##  Load relation types
INSERT INTO `rel_type` VALUES ('nt', 'Narrower concept');
INSERT INTO `rel_type` VALUES ('rt', 'Related concept');
INSERT INTO `rel_type` VALUES ('bt', 'Broader concept');
INSERT INTO `rel_type` VALUES ('tc', 'Top concept');

##  Load status types
INSERT INTO `status` VALUES ('n', 'New');
INSERT INTO `status` VALUES ('d', 'Deleted');