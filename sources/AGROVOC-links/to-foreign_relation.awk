BEGIN { FS = "\t" }
{
  printf ("INSERT INTO foreign_relation VALUES (1,%d,'%s','%s','AGROVOC: %s',1);\n",$5,$1,$3,$2);
}
