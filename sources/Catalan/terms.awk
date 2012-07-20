BEGIN { FS = "\t" }
{
  printf ("INSERT INTO property VALUES (1,%d,'ca','prefLabel',\"%s\",0);\n",$1,$2);
}
