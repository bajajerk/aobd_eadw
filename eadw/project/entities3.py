from datetime import datetime
import re
import time

from py2neo import Graph
from py2neo.packages.httpstream import http


http.socket_timeout = 9999


print "#########################################################"
print "################## ENTITIES PROCESS #####################"
print "#########################################################"

graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")


regexp = r'"(?:[^\\]|(?:\\.))*"'
r_ontology = "http://dbpedia.org/ontology/"
r_name = "http://xmlns.com/foaf/0.1/name"
r_ent = "http://dbpedia.org/resource/"

f = open("entities/entities.nt","r")
lines = f.readlines()


entities = set()
index_query = "CREATE INDEX ON :E(N)"
create_query = "CREATE(n:E{N:{N}})"
relate_query = "MATCH (a:E{N:{A}}),(b:E{N:{B}}) CREATE (a)-[r:`X`]->(b) RETURN r"

graph.cypher.execute(index_query)

tx = graph.cypher.begin()
a=0
p=0

timer = datetime.now().microsecond/1000.0


print "BEGIN"

# create entities
for line in lines:
    m = re.findall ( '<(.*?)>', line, re.DOTALL)
    if len(m)>0:
        from_url = m[0][len(r_ent):].replace("_"," ")      
        toks = m[1].split("/")     
        relation = toks[len(toks)-1]
       
        
        if from_url not in entities:
            tx.append(create_query, {"N": from_url})
            entities.add(from_url)
        fff = from_url
        
        
        name = re.findall ( regexp, line, re.DOTALL)
        if len(name)>0:
            name = name[0]
            name = name[1:len(name)-1]
            
            if name not in entities:
                tx.append(create_query, {"N": name})
                entities.add(name)
            ttt = name
        else:
            if r_ent in m[2]:
                to_url = m[2][len(r_ent):].replace("_"," ")
            else:
                to_url = m[2].replace("_"," ")
                
            if to_url not in entities:                
                tx.append(create_query, {"N": to_url})
                entities.add(to_url)
            ttt = to_url
       
        #print from_id,"|",relation,"|",to_id 
        tx.append(relate_query.replace("X", relation), {"A": fff,"B":ttt,"X":relation})
       
    
        np = (1000 *a)/len(lines)
             
        if p != np:
            p =np   
            tx.process()
            tx.commit()
            tx = graph.cypher.begin()
            
            x = datetime.now().microsecond/1000.0
            perc = p/float(10)
            print str(perc)+"% [" + str((100/perc)*(x-timer)/(60)) + " min]"
    
        a+=1

tx.process()
tx.commit()
f.close()
print "END"