import ThesFacility 
#import ThesLogger
#import ThesAccess

def initialize(registrar):
   """ initialize the Thesaurus Product suite """

   registrar.registerClass( ThesFacility.ThesaurusFacility,
      constructors=(ThesFacility.addForm, ThesFacility.addFunction),
      icon='www/thes.gif')

   registrar.registerHelp()
