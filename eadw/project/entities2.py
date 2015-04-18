import re

from py2neo import Graph, Path, neo4j, node, rel
from py2neo.core import Node
from py2neo.packages.httpstream import http


http.socket_timeout = 9999

graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")
graph.delete_all()
statement = "MERGE (n:Entity {url:{U}}) RETURN n"


print "#########################################################"
print "################## ENTITIES PROCESS #####################"
print "#########################################################"

base_url ="http://pt.wikipedia.org/wiki/"

f = open("entities/entities.nt","r")
lines = f.readlines()

a=0
p=0
tx = graph.cypher.begin()


     
# create entities
for line in lines:
    m = re.findall ( '<(.*?)>', line, re.DOTALL)
    if len(m)>0:
        entity = m[0]        
        fff = tx.append(statement, {"U": entity})
        tx.process()
    np = (100 *a)/len(lines)
         
    if p != np:
        p =np
        print str(p)+"%"
        tx.commit()
        tx = graph.cypher.begin()

    
    a+=1
    
tx.commit()
          


        
# relate entities
for line in lines:
    m = re.findall ( '<(.*?)>', line, re.DOTALL)
    if len(m)>0:
        entity = m[0]
        relation = m[1]
        
        regexp = r'"(?:[^\\]|(?:\\.))*"'
        name = re.findall ( regexp, line, re.DOTALL)
        if len(name)>0:
            name = name[0]
            name = name[1:len(name)-1]
        
        ontology = "http://dbpedia.org/ontology/"
        
        fff = tx.append(statement, {"U": entity})
        tx.process()


        
        if relation == "http://xmlns.com/foaf/0.1/name":
            #n = batch.create(node(N=name))
            
            print p, name    
            #path = batch.create(rel(fff, "name",n))

        
        elif relation.startswith(ontology):
            relation = relation[len(ontology):]
            
            #if len(m)==3 :
            #    ttt = batch.get_or_create(node("Entity",U=m[2]))
            #    path = batch.create(rel(fff, relation,ttt))
            #else:
            #    path = batch.create(rel(fff, relation,name))
            
            
            #print entity ,"|",relation,"|",m[2] if len(m)==3 else name
         
    np = (100 *a)/len(lines)
         
    if p != np:
        p =np
        print str(p)+"%"
        tx.commit()
        tx = graph.cypher.begin()

    
    a+=1
    
tx.commit()
          
                
f.close()
print "DONE"


