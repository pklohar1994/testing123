CREATE TABLE `definition_sources` (
  `abbr` varchar(10) default '',
  `author` varchar(255) default '',
  `title` varchar(255) default '',
  `url` varchar(255) default '',
  `publication` varchar(255) default '',
  `place` varchar(255) default '',
  `year` varchar(10) default '',

  PRIMARY KEY (`abbr`),
  KEY `author` (`author`),
  KEY `title` (`title`),
  KEY `url` (`url`),
  KEY `publication` (`publication`),
  KEY `place` (`place`),
  KEY `year` (`year`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Contains definition sources';



INSERT INTO `definition_sources` VALUES ('ABDN','- - - - -','- - - - -','http://www.abdn.ac.uk/~pol028/sources/europe.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ACRA','- - - - -','- - - - -','http://www.acra.it/acrateca/glosster.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ADMIN','- - - - -','- - - - -','http://www.admin.ch/buwal/i/themen/umwelt/vielfalt/ik14u05.pdf','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AERG','- - - - -','- - - - -','http://aerg.canberra.edu.au/pub/aerg/davey/iucn','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AGBUS','- - - - -','- - - - -','http://agbusmgt.ag.ohio-state.edu/ae601/glossary/glosse.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AGP','- - - - -','- - - - -','http://frost.ca.uky.edu/agripedia/tagrimai.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AGRENV','- - - - -','- - - - -','http://www.agrenv.mcgill.ca/EXTENSION/ECOMUSE/E...','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AGRIC','- - - - -','- - - - -','http://www.agric.gov.ab.ca/agdex/500/4200009.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AHB','- - - - -','Airline Handbook of the Air Transportation Association','http://www.air-transport.org/handbk/glossary.htm','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('ALL','Allaby, M.','Macmillan Dictionary of the Environment - Third Edition','- - - - -','The Macmillan Press Ltd.','London','1990');

INSERT INTO `definition_sources` VALUES ('ALL2','Allaby, M.','Oxford Dictionary of Ecology','- - - - -','Oxford University Press','Oxford','1994');

INSERT INTO `definition_sources` VALUES ('AMBPIA','Scandurra, E. & Macchi, S.','Ambiente e pianificazione - Lessico per le scienze urbane e territoriali','- - - - -','ETASLIBRI','Roma','1995');

INSERT INTO `definition_sources` VALUES ('AMHER','- - - - -','The American Heritage Dictionary of the English Language - Third Edition','- - - - -','Houghton Mifflin Company','Boston','1996');

INSERT INTO `definition_sources` VALUES ('AMOS2','- - - - -','- - - - -','http://amos2.bus.okstate.edu/cgi-shl/gloss/trm_dspl.pl?term=','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ANBG','- - - - -','- - - - -','http://www.anbg.gov.au/esu/ramsar.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ANT','- - - - -','Anthromorphemics: Anthropology Glossary of the Anthropology Department','http://www.anth.ucsb.edu/glossary/index2.html','University of California at Santa Barbara','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('APCD','- - - - -','- - - - -','http://www.apcd.santa-barbara.ca.us/~apcd/biz/cap.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('APD','Morris, Christopher (Ed.)','Academic Press Dictionary of Science and Technology','- - - - -','Academic Press, Inc.','San Diego, CA','1992');

INSERT INTO `definition_sources` VALUES ('APS','- - - - -','Glossary','http://ace.acadiau.ca/polisci/aa/digagora/agora.html','Department of Political Science, Acadia University','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('AQD','- - - - -','- - - - -','http://www.aqd.nps.gov/grd/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ARCH','- - - - -','- - - - -','http://arch.hku.hk/research/BEER/sustain.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ASPE','- - - - -','- - - - -','http://www.aspe.net/aspe.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ATS','- - - - -','- - - - -','http://ats.orst.edu/','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AWD','- - - - -','Australian Waste Database, Draft National Solid Waste Classification System','http://www.civeng.unsw.edu.au/water/awdb/classn4.htm','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('AWM','- - - - -','Animal Waste Management','http://www.oneplan.state.id.us/cfo/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('AZENP','Environmental Information Centre Dusseldorf','A-Z of Environmental Protection','- - - - -','Dusseldorf Messegesellscaft mbH - NOWEA','Dusseldorf','1991');

INSERT INTO `definition_sources` VALUES ('BENNET','- - - - -','Concise Chemical and Technical Dictionary ? Fourth Edition','- - - - -','Edward Arnold','Miami','1986');

INSERT INTO `definition_sources` VALUES ('BHE','- - - - -','Biffa-HTI Environmental Trust Fund Glossary','http://www.biffa-hti.org.uk/waste/glossary.html','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('BIOHW','- - - - -','- - - - -','http://www.bio.hw.ac.uk/edintox/glossall.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('BIOSAF','- - - - -','- - - - -','http://35.8.104.121/manual/main.htm#Biological Safety and Biosafety Levels','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('BIOTAZ','Bains, W.','Biotechnology from A to Z','- - - - -','Oxford University Press','New York','1995');

INSERT INTO `definition_sources` VALUES ('BIOTGL','Commission of the European Communities Terminology Unit','Biotechnology Glossary','- - - - -','Elsevier Applied Science','Luxembourg','1990');

INSERT INTO `definition_sources` VALUES ('BJGEO','Bates, R.L.; Jackson, J.A.','Glossary of Geology - Third Edition','- - - - -','American Geological Institute','Alexandria, USA','1987');

INSERT INTO `definition_sources` VALUES ('BLACK','Black, H. C.','Blacks''s Law Dictionary. 6th ed.','- - - - -','West Publishing Co.','St. Paul','1991');

INSERT INTO `definition_sources` VALUES ('BLYFRE','Blyth, F. G. H.; DeFreitas, M. H.','A geology for engineers - Seventh Edition','- - - - -','Edward Arnold','London','1984');

INSERT INTO `definition_sources` VALUES ('BRACK','Brackley, P.','Energy and Environmental Terms: A Glossary','- - - - -','Gower','Aldershot, England','1988');

INSERT INTO `definition_sources` VALUES ('BRS','- - - - -','- - - - -','http://www.brs.gov.au/apnrb/landcov/lc_what.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('BULB','- - - - -','- - - - -','http://www.bulb.com/industry/whoweare.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('BUSIN','- - - - -','- - - - -','http://www.business.u-net.com/~lincscc/hemsglos.htm#e','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CAMB','- - - - -','International Dictionary of English','- - - - -','Cambridge University Press','Cambridge','1995');

INSERT INTO `definition_sources` VALUES ('CAMER','- - - - -','- - - - -','http://www.cameron.edu/~julie/creation/guidelines/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CCL','- - - - -','A Glossary of Library Terms','http://www.library.carleton.edu/reference/researching/libgloss.html','Laurence McKinley Gould Library, Carleton College','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('CCRS','- - - - -','- - - - -','http://www.ccrs.nrcan.gc.ca/ccrs/eduref/ref/glosndxe.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CED','- - - - -','Collins English Dictionary','- - - - -','Harper Collins Publishers','Glasgow','1994');

INSERT INTO `definition_sources` VALUES ('CEIS','- - - - -','- - - - -','http://www.epa.gov/ceis/atlas/ohiowaters/resources/lakes%20and%20ponds.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CHSK','Nicolini, N.; Scaioni, U. (Trad.)','Dizionario di Chimica','- - - - -','Sperling & Kupfer Ed.','Milano','1992');

INSERT INTO `definition_sources` VALUES ('CIHUNT','- - - - -','- - - - -','http://www.ci.huntsville.al.us/NatRes/ozonepr.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CLAORG','- - - - -','- - - - -','http://cla.org/eclawbook/ecl_04.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CMKYU','- - - - -','- - - - -','http://www.cm.kyushu-u.ac.jp/introe.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CNIE','- - - - -','- - - - -','http://www.cnie.org/nle/AgGlossary/letter-t.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('COE','- - - - -','The Condition of Education 1998','http://nces.ed.gov/pubs98/condition98/c98010.html','US Department of Education National Center for Education Statistics','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('CONFER','Confer, R. G.; Confer, R. T.','Occupational Health and Safety. Terms, Definitions, and Abbreviations','- - - - -','Lewis Publishers','Boca Raton, U.S.A.','1994');

INSERT INTO `definition_sources` VALUES ('CORBIT','Corbitt, R. A.','Standard Handbook of Environmental Engineering','- - - - -','McGraw-Hill Publishing Company','New York','1990');

INSERT INTO `definition_sources` VALUES ('CORP','- - - - -','- - - - -','http://www.corp.csfb.com/corp/about/html/basicsold.htm#0.3','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CULTER','- - - - -','- - - - -','http://culter.colorado.edu:1030/~aerc/about.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('CURZON','Curzon, L. B.','Dictionary of law - Fourth Edition','- - - - -','Pitman Publishing','London','1996');

INSERT INTO `definition_sources` VALUES ('CWSS','- - - - -','- - - - -','http://cwss.www.de/trilat/brochure.html#anchor263016','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DBMDE','- - - - -','- - - - -','http://db.mde.state.mi.us/reports/inventory/glossary.html#O','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DDGI','- - - - -','- - - - -','http://www.ddgi.es/espais/iposidon.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DDP','Tver, David F.','Dictionary of Dangerous Pollutants, Ecology and Environment','- - - - -','Industrial Press, Inc.','New York','1981');

INSERT INTO `definition_sources` VALUES ('DEE','Pankratz, Thomas M.','Concise Dictionary of Environmental Engineering','- - - - -','CRC Press, Inc.','Boca Raton, FL','1996');

INSERT INTO `definition_sources` VALUES ('DEFRA','de Franchis, F.','Dizionario Giuridico Inglese/Italiano?English/Italian Law Dictionary','- - - - -','Giuffr? editore','Milano','1984');

INSERT INTO `definition_sources` VALUES ('DELFIN','- - - - -','Biologia e Medicina ? Biology & Medicine Dizionario Enciclopedico di Scienze Biologiche e Mediche Inglese-Italiano Italiano-Inglese','- - - - -','Zanichelli','Bologna','1995');

INSERT INTO `definition_sources` VALUES ('DES','Porteous, Andrew','Dictionary of Environmental Science and Technology - Second Edition','- - - - -','John Wiley & Sons, Inc.','West Sussex, UK','1996');

INSERT INTO `definition_sources` VALUES ('DHW','- - - - -','Dealing with Hampshire?s Waste: The Way Forward','http://www.integra.org.uk/about/forward.html','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('DICCHE','Daintith, J. (Ed.)','A dictionary of Chemistry ? Third edition','- - - - -','Oxford University Press','Oxford','1996');

INSERT INTO `definition_sources` VALUES ('DICLAW','Matrin, E. A. (Ed.)','A Dictionary of Law ? Fourth edition','- - - - -','Oxford University Press','Oxford','1997');

INSERT INTO `definition_sources` VALUES ('DIFID','Di Fidio, M.','Dizionario di Ecologia','- - - - -','Pirola','Milano','1986');

INSERT INTO `definition_sources` VALUES ('DIRAMB','Tramontano, L.','Diritto dell''ambiente - ecologia ed educazione ambientale III edizione','- - - - -','Edizioni SIMONE','Napoli','1996');

INSERT INTO `definition_sources` VALUES ('DIZAMB','Gamba, G. & Martignetti, G.','Dizionario dell''Ambiente','- - - - -','ISEDI','Torino','1995');

INSERT INTO `definition_sources` VALUES ('DIZSCT','- - - - -','Dizionario della Scienza e della Tecnica','- - - - -','Istituto Geografico De Agostini','Novara','1995');

INSERT INTO `definition_sources` VALUES ('DMG','O?Leary, P. R., et al.','Decision-Maker?s Guide to Solid Waste Management - Second Edition','- - - - -','U.S. Environmental Protection Agency','Washington, DC','1995');

INSERT INTO `definition_sources` VALUES ('DMGEPA','- - - - -','- - - - -','http://www.epa.gov/epaoswer/non-hw/muncpl/dmg2.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DNR','- - - - -','- - - - -','http://www.dnr.qld.gov.au/water/water_monitor/w_qual.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DOBRIS','Stanners, D.; Bourdeau, P.','Europe''s Environment - The Dobris Assessment','- - - - -','European Environment Agency','Copenhagen','1995');

INSERT INTO `definition_sources` VALUES ('DOCMMU','- - - - -','- - - - -','http://www.doc.mmu.ac.uk/aric/airmonit.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DODERO','Dodero, G.','Glossario di Ecologia, Inquinamento, Igiene ambientale','- - - - -','Edizioni Universitarie Scientifiche','Roma','1983');

INSERT INTO `definition_sources` VALUES ('DOE','- - - - -','Dictionary of Ecology and Environmental Science','- - - - -','- - - - -','- - - - -','1993');

INSERT INTO `definition_sources` VALUES ('DUC','- - - - -','- - - - -','http://www.duc.auburn.edu/~johnspm/gloss-n.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DUHA','- - - - -','- - - - -','http://www.duhaime.org/dict-c.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DUNI','- - - - -','- - - - -','http://www.duni.se/Env97/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DUNSTE','Dunster, J. & Dunster, K.','Dictionary of Natural Resource Management - The comprehensive, single-source guide to natural resource management terms','- - - - -','CAB International','Canada','1996');

INSERT INTO `definition_sources` VALUES ('DWEB','- - - - -','- - - - -','http://dweb.ccrs.nrcan.gc.ca/ccrs/db/glossary','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('DWT','- - - - -','Response to Congress on Use of Decentralized Wastewater Treatment Systems','http://www.epa.gov/docs/owmitnet/scpub.htm','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('DYNAMO','- - - - -','- - - - -','http://dynamo.ecn.purdue.edu/~biehl/SiteFarming/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EARTH1','- - - - -','- - - - -','http://earth1.epa.gov/owowwtr1/NPS/sec6/glossref.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ECEST','- - - - -','Definition of Terms used in ECE Standard Statistical Classifications for the Environment','- - - - -','- - - - -','- - - - -','1995');

INSERT INTO `definition_sources` VALUES ('ECHO1','- - - - -','- - - - -','http://eurodic.echo.lu/cgi-bin/edicbin/expert.pl','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ECHO2','- - - - -','- - - - -','http://www2.echo.lu/cgi/edic/edicnew2.pl','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ECONSK','Barile, G. (Ed.)','Dizionario di Economia','- - - - -','Sperling & Kupfer Ed.','Milano','1993');

INSERT INTO `definition_sources` VALUES ('ECOUK','- - - - -','- - - - -','http://www.eco.uk.com/wastex.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ECSA','- - - - -','- - - - -','http://www.ecsanet.org/EUinfo.htm#3.0','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ECSK','Collin, P. H.','Dizionario di Ecologia','- - - - -','Sperling & Kupfer Ed.','Milano','1994');

INSERT INTO `definition_sources` VALUES ('EED','Lee, C. C.','Environmental Engineering Dictionary','- - - - -','Government Institutes, Inc.','Rockville, MD','1989');

INSERT INTO `definition_sources` VALUES ('EFP','- - - - -','Environmental Finance Program Glossary ? Financial Terms Primarily Related to Infrastructure Financing Using Municipal Securities','http://www.epa.gov/efinpage/glossinf.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EIADOE','- - - - -','- - - - -','http://www.eia.doe.gov/emeu/ipsr/appc.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EJRCF','- - - - -','- - - - -','http://www.ejrcf.or.jp/html_rt03/rt03_c05.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EMBMO','- - - - -','- - - - -','http://www.embmortgage.com/glossary/glossarys.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ENSDK','- - - - -','- - - - -','http://www.ens.dk/9bioconf/abstract/bliste.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ENVAR','Meyers, R. A. (Ed.)','Encyclopedia of environmental analysis and remediation','- - - - -','John Wiley & Sons, Inc.','U.S.A.','1998');

INSERT INTO `definition_sources` VALUES ('ENVAU','- - - - -','- - - - -','http://www.environment.gov.au/portfolio/anca/mpa/iucn.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ENVNEL','- - - - -','- - - - -','http://environment.nelson.com/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EPAGLO','United States Environmental Protection Agency','Terms of Environment ? Glossary, Abbreviation, And Acronyms','- - - - -','EPA','U.S.A.','1993');

INSERT INTO `definition_sources` VALUES ('EPEBE','- - - - -','- - - - -','http://www.epe.be/epe/sourcebook/3.14.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EPW','- - - - -','Environmental Profile for the West Bank ?Chapter 9: Solid Waste','http://www.arij.org/profile/vol3/chapter9.htm','Applied Research Institute','Jerusalem','1995');

INSERT INTO `definition_sources` VALUES ('ERG','Frick, G. William, et al. (Ed.)','Environmental Regulatory Glossary - Fifth Edition','- - - - -','Government Institutes, Inc.','Rockville, MD','1990');

INSERT INTO `definition_sources` VALUES ('ERIB','- - - - -','- - - - -','http://www.erib.uni-hannover.de/...','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ERIN','- - - - -','- - - - -','http://www.erin.gov.au/portfolio/epg/eianet/manual/manual/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ESEPA','- - - - -','- - - - -','http://es.epa.gov/ncerqa/opp/opp1.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ESRI','- - - - -','- - - - -','http://www.esri.com/library/glossary/a_d.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EUEN','- - - - -','- - - - -','http://www.euen.co.uk/feu11.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EURMET','- - - - -','- - - - -','http://euromet.meteo.fr/external/demos/courses/glossary/agricul3.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EUROPA','- - - - -','- - - - -','http://europa.eu.int/comm/life/envir/proj_it.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('EUVOC','AA. VV. European Communities','Thesaurus Eurovoc - Volume 1 - Subject- oriented version - Edition 3 / English Language','- - - - -','Official Journal of the European Communities','Bruxelles','1995');

INSERT INTO `definition_sources` VALUES ('FEMA','- - - - -','- - - - -','http://www.fema.gov/library/radback.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FFD','Stevenson, L. Harold, et al.','Facts on File Dictionary of Environmental Science','- - - - -','Facts on File, Inc.','New York','1991');

INSERT INTO `definition_sources` VALUES ('FKT','- - - - -','- - - - -','http://www.fkt.de/fkt2689.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FLG','- - - - -','A Flagstaff 2020 Glossary','http://www.flagstaff.az.us/Flagstaff_2020/flag5.html','Arizona Chamber of Commerce','Flagstaff','1997');

INSERT INTO `definition_sources` VALUES ('FLGISA','Floccia, M.; Gisotti, G.; Sanna, M.','Dizionario dell''inquinamento. Cause, effetti, rimedi, normativa','- - - - -','NIS, La Nuova Italia Scientifica','Roma','1985');

INSERT INTO `definition_sources` VALUES ('FORGOV','- - - - -','- - - - -','http://WWW.FOR.GOV.BC.CA/PAB/PUBLCTNS/GLOSSARY/M.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FORUMT','- - - - -','- - - - -','http://www.forestry.umt.edu/courses/FOR503/TERMS-1.HTM','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FREEAD','- - - - -','- - - - -','http://www.freeadvice.com/law/635us.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FUNKE','- - - - -','- - - - -','http://www.funke-biochemietechnik.de/oelfre.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('FUT','- - - - -','The Futures Study Centre''s Glossary','http://www.futures.austbus.com/glossall.htm','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('GEMAIR','- - - - -','- - - - -','http://www.gemair.com/~usechem/frchem5term.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GEOG','- - - - -','- - - - -','http://www.geog.buffalo.edu/~naumov/TA/GEO483-553/Lab_handouts/Lab6.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GILP','Gilpin, A.','Dictionary of environmental terms','- - - - -','Routledge end Kegan Paul ltd.','London','1976');

INSERT INTO `definition_sources` VALUES ('GILP96','Gilpin, A.','Dictionary of Environment and sustainable development','- - - - -','John Wiley & Sons','Chichester','1996');

INSERT INTO `definition_sources` VALUES ('GIS','- - - - -','GIS Glossary','http://www.env.gov.bc.ca:8000/','British Columbia Ministry of Environment, Lands & Parks','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GLOCHA','- - - - -','- - - - -','http://www.globalchange.org/glossall/glossp-r.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GMR','- - - - -','Glossary of Materials Recycling Terms','http://www.recyclingdata.com/GLOSSARM.HTML','ARM Annual Directory / Reference Manual','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GOOD','Goodall, B.','Dictionary of Human Geography','- - - - -','Penguin Books','London','1987');

INSERT INTO `definition_sources` VALUES ('GOUD','Goudie, A.','The Human Impact on the Natural Environment','- - - - -','Basil Blackwell','Oxford','1988');

INSERT INTO `definition_sources` VALUES ('GRAHAW','Grant & Hawkins (Ed.s)','Concise lexicon of Envrionmental Terms','- - - - -','John Wiley & Sons, Inc.','Chichester','1995');

INSERT INTO `definition_sources` VALUES ('GREENW','Greenwald, D. et al.','The McGraw-Hill Dictionary of Modern Economics - II Ed.','- - - - -','McGraw-Hill','New York','1973');

INSERT INTO `definition_sources` VALUES ('GREMES','Jones, G.; Robertson, A.; Forbes, J.; Hollier, G.','Dizionario Collins dell''ambiente','- - - - -','Gremese','Roma','1994');

INSERT INTO `definition_sources` VALUES ('GRN','- - - - -','- - - - -','http://grn.com/grn/library/gloss-t.htm#Refuse','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GRT','- - - - -','Glossary of Recycling Terms','http://grn.com/grn/library/gloss.htm','Global Recycling Network','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GSFC','- - - - -','- - - - -','http://spsosun.gsfc.nasa.gov/Newgloss.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('GSW','Patrick, P. K. (Ed.)','Glossary of Solid Waste','- - - - -','World Health Organization','Copenhagen','1980');

INSERT INTO `definition_sources` VALUES ('GUNN','Gunn, S. W. A.','Multilingual Dictionary of Disaster Medicine and International Relief','- - - - -','Kluwer Academic Publishers','Dordrecht','1990');

INSERT INTO `definition_sources` VALUES ('HARRIS','Harris, C. M.','Dictionary of Architecture & Construction - Second Edition','- - - - -','McGraw-Hill, Inc.','New York','1993');

INSERT INTO `definition_sources` VALUES ('HELIOS','- - - - -','- - - - -','http://helios.emse.fr/~brodhag/projelev/osd31.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('HGD','- - - - -','Humber Estuary Management Strategy (HEMS) Glossary and Definitions','http://www.personal.u-net.com/~lincscc/hemsglos.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('HMD','Coleman, Ronny J.','Hazardous Materials Dictionary - Second Edition','- - - - -','Technomics Publishing Co., Inc.','Lancaster, PA','1994');

INSERT INTO `definition_sources` VALUES ('HMH','Allegri, Theodore H.','Handling and Management of Hazardous Materials and Waste','- - - - -','Chapman and Hall','New York','1986');

INSERT INTO `definition_sources` VALUES ('ICBT','- - - - -','- - - - -','http://www.icbtgroup.com/icbt/gb/activites/parachimie/parachimie_1.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('IEAP','- - - - -','- - - - -','http://www.ieap.uni-kiel.de/atom+plasmaphysik/ag_piel/intro_e/lexikon_e.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('IFSE','- - - - -','- - - - -','http://ifse.tamu.edu/ifse/irradiationarticle.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('IISD','- - - - -','- - - - -','http://iisd1.iisd.ca/didigest/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('INDEDU','- - - - -','- - - - -','http://www.indiana.edu/~ipe/glossry.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('INDMER','- - - - -','The Index Merck ? An Encyclopedia of Chemicals and Drugs ? Ninth Edition','- - - - -','Merck & Co., Inc.','U.S.A.','1976');

INSERT INTO `definition_sources` VALUES ('INFOAB','- - - - -','- - - - -','http://info.abdn.ac.uk/~pol028/sources/europe.htm#SEA2','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('INFREG','- - - - -','- - - - -','http://www.inforegio.cec.eu.int/wbover/overglo/L_EN.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('INW','- - - - -','Industrial Wastes Page','http://mecaniza.sestud.uv.es/open/mambiente/industwas.htm','Universitat de Valencia','Valencia','- - - - -');

INSERT INTO `definition_sources` VALUES ('ISEP','ISEP','- - - - -','- - - - -','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ISOCH','- - - - -','- - - - -','http://www.iso.ch/infoe/intro.htm#What are standards','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('IUCN','- - - - -','- - - - -','http://www.iucn.org/themes/ramsar/key_ris_guide_f.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('JBFENV','- - - - -','- - - - -','http://www.jbfenv.com/orc.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('JCU','- - - - -','- - - - -','http://www.jcu.edu.au/school/law/ev2002/html/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('JEFF','- - - - -','- - - - -','http://co.jefferson.co.us/dpt/gis/glos/term/gis/pixel.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('JJK','King, J. J.','The Environmental Dictionary and Regulatory Cross-Reference Third edition','- - - - -','John Wiley & Sons, Inc.','New York','1994');

INSERT INTO `definition_sources` VALUES ('JMU','- - - - -','- - - - -','http://www.jmu.edu/psyc/peer/env.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('JON','- - - - -','J.4 Glossary','http://www.usdoj.gov/jmd/pss/jcon/jcon_j04.htm','US Department of Justice Consolidated Office Network','- - - - -','1996');

INSERT INTO `definition_sources` VALUES ('KINGST','- - - - -','- - - - -','http://www1.kingston.net/~gforbes/EN081/Glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('KOREN','Koren, H.; National Environmental Health Association','Illustrated Dictionary of Environmental Health & Occupational Safety','- - - - -','Lewis Publishers','Boca Raton, U.S.A.','1996');

INSERT INTO `definition_sources` VALUES ('KSW','- - - - -','- - - - -','http://www.ksw.org.uk/atmosphere/pages/struct01.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('LANDY','Landy, M.','Environmental Impact Statement Glossary. A Reference Source for EIS Writers, Revuewers, and Citizens.','- - - - -','IFI/Plenum Publishing Corporation','New York','1979');

INSERT INTO `definition_sources` VALUES ('LAROUS','- - - - -','Dizionario Francese Italiano - Italiano Francese','- - - - -','Sansoni Editore','Firenze','1981');

INSERT INTO `definition_sources` VALUES ('LBC','Lincoln, R. J.; Boxshall, G. A.; Clark, P. F.','A Dictionary of Ecology, Evolution and Systematics','- - - - -','Cambridge University Press','Cambridge','1982');

INSERT INTO `definition_sources` VALUES ('LBL','- - - - -','- - - - -','http://www.lbl.gov/NABIR/info_5.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('LEE','Lee, C. C. (Ed.)','Environmental Engineering Dictionary ? Second edition','- - - - -','Government Institutes, Inc.','Maryland ? U.S.A.','1992');

INSERT INTO `definition_sources` VALUES ('LFS','- - - - -','Fact Sheet - Interlibrary Loan','http://www.ala.org/library/fact8.html','American Library Assocation (ALA), LARC (Library and Research Center)','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('LOGIE','Logie, G.','Glossary of land resources, International planning glossaries 4, English-French-Italian-Dutch-German-Swedish','- - - - -','Elsevier','Amsterdam','1984');

INSERT INTO `definition_sources` VALUES ('LWW','- - - - -','Lake and Water Word Glossary','http://www.nalms.org/glossary/a-z.htm','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('MAFF','- - - - -','- - - - -','http://www.maff.gov.uk/fish/fish-ind.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MANCOS','- - - - -','Manuale del costruttore e del geometra - materiali, ecologia, geotecnica, urbanistica, strutture, impianti interni, strade, costruzioni idrauliche, cantiere, topografia, agronomia, economia, estimo.','- - - - -','Zanichelli/ESAC','Roma','1997');

INSERT INTO `definition_sources` VALUES ('MDM','- - - - -','Michigan (Department of State) Dealer Manual','http://sos.state.mi.us/bar/dealer/manual/title1.html','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('MED','- - - - -','Medical Dictionary from Merriam-Webster, Medscape','http://www.medscape.com/mw/medical.htm','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('MGH','- - - - -','McGraw-Hill Zanichelli Dizionario Enciclopedico Scientifico e Tecnico Inglese-Italiano Italiano-Inglese','- - - - -','Zanichelli','Bologna','1998');

INSERT INTO `definition_sources` VALUES ('MGHME','- - - - -','McGraw-Hill Dictionary of Modern Economics, 3rd edition','- - - - -','- - - - -','- - - - -','1983');

INSERT INTO `definition_sources` VALUES ('MHD','Parker, Sybil P. (Ed.)','McGraw-Hill Dictionary of Scientific and Technical Terms - Fourth Edition','- - - - -','McGraw-Hill, Inc.','New York','1989');

INSERT INTO `definition_sources` VALUES ('MICH','- - - - -','- - - - -','http://www.mich.com/~buffalo/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MIIS','- - - - -','- - - - -','http://cns.miis.edu/cns/inventory96/acronyms.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MLK','- - - - -','A Glossary of Nonviolence','http://www.thekingcenter.com/glossary.html','The Martin Luther King, Jr. Center for Nonviolent Social Change','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MOBAR','- - - - -','- - - - -','http://www.mobar.org/press/gloss.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MOBIL','- - - - -','- - - - -','http://www.mobil.com/cgi-bin/bld_frameset.cgi?CONTENT=/this/globalad/doublehull/doublehull.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MOND','- - - - -','- - - - -','http://ci.mond.org/9521/952101.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MORON','Moroni, A.; Faranda, F.','Ecologia','- - - - -','Piccin Editore','Padova','1993');

INSERT INTO `definition_sources` VALUES ('MOSGOV','- - - - -','- - - - -','http://www.mos.gov.pl/mos/komorki/dlopik_eng.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MSTF','- - - - -','- - - - -','http://www.mstf.org/~meaqua/Shellfish.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('MUCK','- - - - -','- - - - -','http://muck.soils.ufl.edu/primer/gloss.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NALMS','- - - - -','- - - - -','http://www.nalms.org/glossary/lkword_i.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NATURE','- - - - -','- - - - -','http://www.natureef.com/trace.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NDECON','De Luca, G.; Minieri, S. & Verrilli, A.','Nuovo Dizionario di Economia','- - - - -','Edizioni SIMONE','Napoli','1998');

INSERT INTO `definition_sources` VALUES ('NDGIUR','Del Giudice, F (Ed.)','Nuovo Dizionario Giuridico - V edizione totalmente rifatta - Corredato da riferimenti legislativi e confronti interdisciplinari','- - - - -','Esselibri Simone','Napoli','1998');

INSERT INTO `definition_sources` VALUES ('NDN','CNR-RRDA','No definition needed','- - - - -','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NECTAR','- - - - -','- - - - -','http://www.nectar.org/reposit/mirti/5.2/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NERIS','- - - - -','- - - - -','http://neris.mii.lt/aa/an95/adir45.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NGT','- - - - -','Glossary of Terms and Definitions Used in the AMEPP Series, 1st edition','http://www.nato.int/ccms/swg12/docs/amepp7.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NHQ','- - - - -','- - - - -','http://www.nhq.nrcs.usda.gov/NRI/documentation/1992/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NPL','- - - - -','- - - - -','http://www.npl.co.uk/npl/environment/index.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NRCAN','- - - - -','- - - - -','http://www.nrcan.gc.ca/mms/school/env/restofr.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('NWF','- - - - -','- - - - -','http://www.nwf.org/nwf/international/trade/tandefact.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('OCEAN','- - - - -','- - - - -','http://www-ocean.tamu.edu/~baum/paleo/paleogloss/paleogloss.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ODE','- - - - -','Oxford (Paperback Reference): A Dictionary of Economics','- - - - -','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('OED','Oxford University Press','Oxford English Dictionary on Compact Disc - Second Edition','- - - - -','Oxford University Press','Oxford, UK','1995');

INSERT INTO `definition_sources` VALUES ('OER','- - - - -','Oak Ridge Reservation Annual Site Environmental Report for 1995','http://www.ornl.gov/Env_Rpt/aser95/apph.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('OLIN','- - - - -','- - - - -','http://ww2.olinbiocides.com/Marine/algaecides.asp','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ONE','- - - - -','"What is the animal rights movement?" One Struggle','http://members.aol.com/onestruggl/','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('OPPTIN','- - - - -','- - - - -','http://www.epa.gov/opptintr/cbep/actlocal/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('OX','- - - - -','STAND-BY','- - - - -','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PAENS','Paenson, I.','Environment in key word ? A multilingual Handbook of the Environment','- - - - -','Pergamon Press','Great Britain','1990');

INSERT INTO `definition_sources` VALUES ('PALIM','- - - - -','- - - - -','http://palimpsest.stanford.edu/don/dt/dt3403.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PARCOR','Parker, S. P. & Corbitt, R. A.','McGraw-Hill Encyclopedia of Environmental Science & Engineering - Third Edition','- - - - -','McGraw-Hill, Inc.','USA','1993');

INSERT INTO `definition_sources` VALUES ('PASTU','- - - - -','- - - - -','http://pasture.ecn.purdue.edu/~agenhtml/agen521..','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PATHUL','Patton-Hulce V. R.','Environment and the Law - A Dictionary','- - - - -','ABC-CLIO','Santa Barbara','1995');

INSERT INTO `definition_sources` VALUES ('PENEL','- - - - -','- - - - -','http://www-penelope.drec.unilim.fr/penelope/LIbrary/Libs/EURO/85337/85337_s.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PGE','- - - - -','Principles and Guidelines for Environmental Labelling and Advertising','http://strategis.ic.gc.ca/SSG/cp01029e.html','- - - - -','- - - - -','1993');

INSERT INTO `definition_sources` VALUES ('PHC','Collin, P. H.','Dictionary of ecology and the environment - 3rd edition','- - - - -','Peter Collin Publishing','Teddington','1995');

INSERT INTO `definition_sources` VALUES ('PHYMAC','- - - - -','- - - - -','http://www.phymac.med.wayne.edu/facultyprofile/penney/COHQ/coproperties.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PITT','Pitt, V. H. (Ed.)','The Penguin Dictionary of Physics','- - - - -','Penguin Books','Great Britain','1978');

INSERT INTO `definition_sources` VALUES ('POPTEL','- - - - -','- - - - -','http://www.poptel.org.uk/mante/glossary/g147.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PORT','Porteous, A.','Dictionary of Environmental Science and Technology - Second Edition','- - - - -','John Wiley & Sons','Chichester','1996');

INSERT INTO `definition_sources` VALUES ('PPB','- - - - -','PPBI (Private and Public Businesses, Inc.) Glossary','http://www.ppbi.org/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('PPP','Joan E. Canfield','Progress in Plant Protection','http://www.fws.gov/r9endspp/esb/96/plants.html','Endangered Species Bulletin XXI/4','- - - - -','1996');

INSERT INTO `definition_sources` VALUES ('PUE','- - - - -','Purdue University and EPA Region 5 Glossary','http://muextension.missouri.edu/dldc/HHWP_Awareness/waste/src/glossary1.htm','- - - - -','- - - - -','1996');

INSERT INTO `definition_sources` VALUES ('PZ','Pfaffin, J. R. & Ziegler, E. N.','Encyclopedia of Environmental Science and Engineering - Third Edition, Volume 1 A-I + Volume 2 J-Z','- - - - -','Gordon and Breach Science Publishers','USA','1992');

INSERT INTO `definition_sources` VALUES ('QUOTE','- - - - -','- - - - -','http://quote.yahoo.com.au/finance/glossary/glossary-m.html#9','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('RAMADE','Ramade, F.','Dictionnaire Encyclop?dique de l''Ecologie et des Sciences de l''Environnement','- - - - -','Ediscience International','Paris','1993');

INSERT INTO `definition_sources` VALUES ('RAU','Rau, G. J. & Wooten, D. C.','Environmental Impact Analysis Handbook','- - - - -','McGraw-Hill','U.S.A.','1990');

INSERT INTO `definition_sources` VALUES ('RBGKEW','- - - - -','- - - - -','http://www.rbgkew.org.uk/BGCI/hagemann.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('RDB','- - - - -','- - - - -','http://rdb.eaurmc.fr/glossaire/html/Napallu.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('REVEG','- - - - -','- - - - -','http://www.revegetation.com/','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('RFA','- - - - -','- - - - -','http://www.rfa.gov.au/nfps/gloss.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('RHW','Random House','Random House Webster?s Unabridged Dictionary - Second Edition','- - - - -','Random House, Inc.','New York','1997');

INSERT INTO `definition_sources` VALUES ('RRDA','CNR-RRDA','- - - - -','- - - - -','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('RSG','- - - - -','Remote Sensing Glossary, Virtual Nebraska','http://www.casde.unl.edu/vn/glossary/intro.htm','Consortium for the Application of Space Data to Education','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SALINF','- - - - -','- - - - -','http://www.saltinfo.com/prod1.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SASW','- - - - -','- - - - -','http://sasw.chass.ncsu.edu/s&a/socpsy.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SCHNET','- - - - -','- - - - -','http://www.schoolnet.ca/collections/arctic/glossary/ecogloss.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SCIFRI','- - - - -','- - - - -','http://www.sciencefriday.com/pages/1996/Mar/hour1_030196.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SCRUZ','- - - - -','- - - - -','http://www.scruz.net/~kangaroo/glossarydi.htm#debt','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SFRC','- - - - -','- - - - -','http://www.sfrc.ufl.edu/Laboratories/GIS/','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SHELL','- - - - -','- - - - -','http://www.shell.com/b/b1_01d15.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SHG','- - - - -','Sustainable Hospitals Glossary, Sustainable Hospitals','http://www.uml.edu/centers/LCSP/hospitals/HTMLSrc/Glossary.html','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('SHOOX','- - - - -','The New Shorter Oxford English Dictionary on Historical Principles','- - - - -','Clarendon Press','Oxford','1993');

INSERT INTO `definition_sources` VALUES ('SKENE','- - - - -','- - - - -','http://www.skene.be/RW/dgatlpnew/PRQ%20CLAS','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('SOC','Alex Thio','Sociology 5e','http://longman.awl.com/thio/glossary_u.htm','- - - - -','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('SOCIOL','Mashall, G.','The Concise Oxford Dictionary of Sociology','- - - - -','Oxford University Press','Oxford','1996');

INSERT INTO `definition_sources` VALUES ('SRD','Serge Moscovici','Definition of the concept of social representation','http://socpsych.jk.uni-linz.ac.at/SocReps/PSR.html','Introduction a la psychologie sociale','- - - - -','1998');

INSERT INTO `definition_sources` VALUES ('STEDMA','- - - - -','Stedman Medical Dictionary illustrated ? Twenty-second Edition','- - - - -','The William & Wilkins Company','Baltimore','1972');

INSERT INTO `definition_sources` VALUES ('TCPCO','- - - - -','- - - - -','http://homepages.pcp.co.uk/~carling/een/cc/cc_31/c31_4160.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TDH','- - - - -','- - - - -','http://www.tdh.state.tx.us/ech/rad/PAGES/GLOSSARY.HTM','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TEA','- - - - -','- - - - -','http://www.tea.state.tx.us/resources/ssced/teks/glossecon.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TECHBA','- - - - -','- - - - -','http://www.techbase.co.nz/applications/conf/paper2.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TELFO','- - - - -','- - - - -','http://t-telford.co.uk/pu/ocbk009.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TEX','Social Studies Center for Educator Development (SSCED)','TEKS - World Geography Glossary,','- - - - -','Texas Education Agency','U.S.A.','1997');

INSERT INTO `definition_sources` VALUES ('TOE','- - - - -','Terms of Environment, Revised','http://www.epa.gov/OCEPAterms/','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('TOLGAR','- - - - -','- - - - -','http://www.tolgar-b.com/commercial/Information.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TOURIS','- - - - -','- - - - -','http://www.tourism.co.cr/monte.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TRADEP','- - - - -','- - - - -','http://www.tradeport.org/ts/refs/gloss/i.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TUBERL','- - - - -','- - - - -','http://www.tu-berlin.de/fb6/itu/stud/stinst.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('TWI','- - - - -','The Whole Internet: User?s Guide & Catalog','- - - - -','- - - - -','- - - - -','1994');

INSERT INTO `definition_sources` VALUES ('UBADE','- - - - -','- - - - -','http://www.umweltbundesamt.de/uba-info-daten-e/daten-e/federal-immission-control-act.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UEEU','- - - - -','- - - - -','http://ue.eu.int/en/info/frame1.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UIB','- - - - -','- - - - -','http://www.uib.es/ciencia/42/Art.-llarg.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UNEP','- - - - -','- - - - -','http://www.unep.ch/t&e/harm1.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UNESCO','- - - - -','- - - - -','http://www.unesco.org/culture/worldreport/html_eng/wcr5.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UNION','- - - - -','- - - - -','http://www.union-fin.fr/natcog/lexique/lexique_r.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UNM','- - - - -','- - - - -','http://www.unm.edu/~libinfo/Libraries/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UNTERM','U.N. Office of Conference Services; Translation Division; Documentation, Reference and Terminology Section','Terminology Bullettin N.344 Vol.I - Vol.II (indexes)','- - - - -','United Nations Publication - Secretariat','New York','1992');

INSERT INTO `definition_sources` VALUES ('UNUN','International Environmental Education Programme','Glossary of Environmental Education Terms','- - - - -','Unesco-Unep','Hungary','1983');

INSERT INTO `definition_sources` VALUES ('USC','- - - - -','- - - - -','http://www.usc.edu/dept/puad/apex/eqagloss.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('USDA','- - - - -','- - - - -','http://www.usda.gov/gipsa/progser/inspwgh/pest.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('USERS','- - - - -','- - - - -','http://www.users.bigpond.com/nswb/glossary.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('USIA','- - - - -','- - - - -','http://www.usia.gov../topical/econ/language/ad-gloss.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UST','- - - - -','- - - - -','http://www.ust.hk/~webceng/','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('UVAROV','Uvarov, E. B. & Isaac, A.','Dictionary of Science','- - - - -','Penguin Books','London','1993');

INSERT INTO `definition_sources` VALUES ('VALAMB','Gisotti, G.; Bruschi, S.','Valutare l''ambiente. Guida agli studi d''impatto ambientale','- - - - -','NIS, La Nuova Italia Scientifica','Roma','1990');

INSERT INTO `definition_sources` VALUES ('VCDS','- - - - -','- - - - -','http://www.vcds.dnd.ca/vcds/dgsp/dpg/dpg97/gloss_e.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('VCN','- - - - -','- - - - -','http://vcn.bc.ca/wcel/otherpub/6140.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('VIRPUR','- - - - -','- - - - -','http://www.virginpure.com/tec/glossary.html#P','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('VISMA','Vismara, R.','Ecologia Applicata - Inquinamento e salute umana - Criteri di protezione dell''aria, delle acque, del suolo - Valutazione di impatto ambientale - Esempi di calcolo - II Edizione','- - - - -','U. Hoepli Editore','Milano','1992');

INSERT INTO `definition_sources` VALUES ('WASCH','- - - - -','- - - - -','http://www.waschpark.de/tankstelle/main.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WATER','- - - - -','- - - - -','http://water.eng.mcmaster.ca/pages/air.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WEATHE','- - - - -','- - - - -','http://www.weathervane.rff.org/glossary/index.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WEBSTE','- - - - -','Webster?s Third New International Dictionary of the English Language','- - - - -','Merriam-Webster INC, Publishers','Springfield, U.S.A.','1993');

INSERT INTO `definition_sources` VALUES ('WECK','Weck, J.','Dictionary of Forestry','- - - - -','Elsevier Science Publishers','Amsterdam','1996');

INSERT INTO `definition_sources` VALUES ('WESTM','Westman E. Walter','Ecology, Impact Assessment, and Environmental Planning','- - - - -','John Wiley & Sons','U.S.A.','1994');

INSERT INTO `definition_sources` VALUES ('WESTS','- - - - -','West?s Law & Commercial Dictionary','- - - - -','Zanichelli/West','Bologna','1996');

INSERT INTO `definition_sources` VALUES ('WHC','- - - - -','Mission Statement of the World Heritage Committee of UNESCO','http://www.unesco.org/whc/1mission.htm#debut','- - - - -','- - - - -','1996');

INSERT INTO `definition_sources` VALUES ('WHIT','Whittow, J.','Dictionary of Physical Geography','- - - - -','Penguin Books','London','1984');

INSERT INTO `definition_sources` VALUES ('WIC','- - - - -','- - - - -','http://whatis.com/default.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WILDLA','- - - - -','- - - - -','http://www.wildlands.org/corridor/what_are_corr.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WILKES','- - - - -','- - - - -','http://wilkes1.wilkes.edu/~eqc/corrosion.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WINDOW','- - - - -','- - - - -','http://www.windows.umich.edu/comets/','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WMA','- - - - -','Glossary of Terms','http://www.taiga.net/wmac/researchplan/terms.html','Wildlife Management Advisory Council - Yukon North Slope','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WPR','Union of International Association','Encyclopedia of World Problems and Human Potential - 4th Edition - Vol.1: World Problems','- - - - -','K.G. Saur','Munchen','1994');

INSERT INTO `definition_sources` VALUES ('WQA','- - - - -','Water Quality Association Glossary of Terms','http://www.wqa.org/Glossary/index.html','- - - - -','- - - - -','1997');

INSERT INTO `definition_sources` VALUES ('WRES','The World Resources Institute','World Resources 1994-95','- - - - -','Oxford University Press','New York','1994');

INSERT INTO `definition_sources` VALUES ('WRIGHT','- - - - -','The Environment Encyclopedia and Directory','- - - - -','Europa Publications Ltd.','London','1994');

INSERT INTO `definition_sources` VALUES ('WSU','- - - - -','- - - - -','http://www.wsu.edu/~dee/GLOSSARY/LEGIT.HTM','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('WWC','Joint Editorial Board','Glossary: Water and Wastewater Control Engineering - Third Edition','- - - - -','American Public Health Assoc.','Washington, DC','1981');

INSERT INTO `definition_sources` VALUES ('YORK','- - - - -','- - - - -','http://www.yorkwatershed.org/glossary.htm','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('YOUNG','Young, P.','Environmental Sistems','- - - - -','Pergamon Press','Oxford','1993');

INSERT INTO `definition_sources` VALUES ('Z2Z','- - - - -','- - - - -','http://www.z2z.com/itglos04.html','- - - - -','- - - - -','- - - - -');

INSERT INTO `definition_sources` VALUES ('ZINZAN','- - - - -','Lo Zingarelli 1998 ?Vocabolario della lingua italiana ? dodicesima edizione','- - - - -','Zanichelli','Bologna','1998');
