from py2neo import cypher
from py2neo import neo4j
from py2neo.core import Graph


graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")


tx = graph.cypher.begin()
tx.append("START beginning=node(415583), end=node(415584) MATCH p = shortestPath(beginning-[*..500]-end) RETURN p")
print tx.process()


tx = graph.cypher.begin()
tx.append("MATCH (beginning {N:'Albert Einstein'}), (end {N:'Hadrian'}) MATCH p = shortestPath(beginning-[*..10]-end) RETURN p")
print tx.process()