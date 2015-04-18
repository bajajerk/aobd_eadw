import re

from py2neo import Graph, neo4j, rel
from py2neo.core import Node
from py2neo.packages.httpstream import http


http.socket_timeout = 9999999


print "#########################################################"
print "################## ENTITIES PROCESS #####################"
print "#########################################################"

graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")
batch = neo4j.WriteBatch(graph)


graph.delete_all()

regexp = r'"(?:[^\\]|(?:\\.))*"'
r_ontology = "http://dbpedia.org/ontology/"
r_name = "http://xmlns.com/foaf/0.1/name"
r_ent = "http://dbpedia.org/resource/"


f = open("entities/entities.nt","r")
lines = f.readlines()

a=0
p=0

entities = {}
print "BEGIN"


# create entities
for line in lines:
    m = re.findall ( '<(.*?)>', line, re.DOTALL)
    if len(m)>0:
        from_url = m[0][len(r_ent):]
        relation = m[1]
        
        toks = relation.split("/")     
        relation = toks[len(toks)-1]
        
        if from_url not in entities:
            fff = entities[from_url] = batch.create(Node("E",N=from_url))
        else:
            fff = entities[from_url]
        
        
        
        name = re.findall ( regexp, line, re.DOTALL)
        if len(name)>0:
            name = name[0]
            name = name[1:len(name)-1]
            ttt = batch.create(Node("P",N=name))
        else:
            to_url = m[2][len(r_ent):]
            if to_url not in entities:
                ttt = entities[to_url] = batch.create(Node("E",N=to_url))
            else:
                ttt = entities[to_url]
       
       
        #print from_id,"|",relation,"|",to_id 
        batch.create(rel(fff, relation,ttt))    
       
    
        np = (1000 *a)/len(lines)
             
        if p != np:
            p =np   
            print relation

            print str(p/float(10))+"%"
    
    
        a+=1


batch.submit()
f.close()
print "END"