from whoosh.index import open_dir
from whoosh.qparser.default import QueryParser
from whoosh.qparser.syntax import OrGroup


def search(index,query):
    index = open_dir("indexdir")
    
    res = []
    
    with index.searcher() as searcher:
        query = QueryParser("content", index.schema, group=OrGroup).parse(unicode(query,"UTF-8"))
        results = searcher.search(query, limit=100)
        for r in results:
            res.append(r["id"])
        
    return res