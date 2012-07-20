BEGIN { FS = "\t" }
{
  if ($2 == "Groups") { ns = 3; }
  if ($2 == "Super groups") { ns = 2; }
  if ($2 == "Themes") { ns = 4; }
  printf ("INSERT INTO property VALUES (%d,%d,'ca','prefLabel',\"%s\",0);\n",ns,$1,$3);
}
