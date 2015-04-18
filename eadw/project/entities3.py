import re

from py2neo import Graph, rel
from py2neo.core import Node
from py2neo.packages.httpstream import http


http.socket_timeout = 9999


print "#########################################################"
print "################## ENTITIES PROCESS #####################"
print "#########################################################"

graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")


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
        toks = m[1].split("/")     
        relation = toks[len(toks)-1]
       
        
        if from_url not in entities:
            fff = entities[from_url] = Node("E",N=from_url)
            graph.create(fff)
        else:
            fff = entities[from_url]
        
        
        
        name = re.findall ( regexp, line, re.DOTALL)
        if len(name)>0:
            name = name[0]
            name = name[1:len(name)-1]
            ttt =Node("P",N=name)
            graph.create(ttt)
        else:
            to_url = m[2][len(r_ent):]
            if to_url not in entities:
                ttt = entities[to_url] = Node("E",N=to_url)
                graph.create(ttt)
            else:
                ttt = entities[to_url]
       
       
        #print from_id,"|",relation,"|",to_id 
        graph.create(rel(fff, relation,ttt))    
       
    
        np = (1000 *a)/len(lines)
             
        if p != np:
            p =np   
    
            print str(p/float(10))+"%"
    
    
        a+=1



f.close()
print "END"