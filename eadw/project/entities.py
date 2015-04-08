import os
import re
from whoosh.fields import Schema, TEXT
from whoosh.index import exists_in, create_in, open_dir


print "#########################################################"
print "################## ENTITIES PROCESS #####################"
print "#########################################################"

base_url ="http://pt.wikipedia.org/wiki/"

files={}
files["entities/persons.txt"]="p", 
files["entities/locations.txt"]="l", 
files["entities/organizations.txt"]="o"


if not os.path.exists("entities"):
    os.makedirs("entities")

# do query for new entities
entities_index = None
if not exists_in("entities"):
    schema = Schema(url=TEXT(stored=True), name=TEXT(stored=True),opt=TEXT(stored=True),type=TEXT(stored=True))
    entities_index = create_in("entities", schema)
else:
    entities_index = open_dir("entities")

entities_writer = entities_index.writer()

for file in files:
    f = open(file,"r")
    for line in f.read().splitlines():
        url = line
        name = line.split(base_url).pop().replace("_"," ")
        opt = re.search(r"\([^)]*\)", name)
        if opt is None:
            opt = ""
        else:
            opt = opt.group()
            opt = opt[1:len(opt)-1].strip(" ")
        name = re.sub(r'\([^)]*\)', '', name).strip(" ")
               
               
        print name,"|",opt
        entities_writer.add_document(url=url.decode("utf-8"),
                                     name=name.decode("utf-8"),
                                     opt= opt.decode("utf-8"),
                                     type=unicode(files[file]))
    f.close()
        
entities_writer.commit()
print "DONE"