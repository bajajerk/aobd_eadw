
import BaseHTTPServer
import datetime
import json
import os
import shutil
import sys
import time
import urlparse

from dateutil import parser
from py2neo.core import Graph
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser.default import MultifieldParser
from whoosh.qparser.syntax import OrGroup
from whoosh.scoring import BM25F, TF_IDF


graph = Graph("http://neo4j:qazokm@localhost:7474/db/data/")


__version__ = "0.6"

__all__ = ["MyHttpServer"]

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class OurWeight(scoring.WeightingModel):        
    class Scorer(scoring.BaseScorer):
        def __init__(self, idfScorer,bm25Scorer):
            self.idfScorer = idfScorer
            self.bm25Scorer = bm25Scorer
       
        def score(self, matcher):
            s = (self.bm25Scorer.score(matcher)*0.5+self.idfScorer.score(matcher)*0.5)
            return s
        


    def scorer(self, searcher, fieldname, text, qf=1):
        # BM25
        bm25Scorer = BM25F().scorer(searcher, fieldname, text, qf) 
        tfidfScorer = TF_IDF().scorer(searcher, fieldname, text, qf)
        return self.Scorer(tfidfScorer,bm25Scorer)

class TimeWeight(scoring.WeightingModel):        
    class Scorer(scoring.BaseScorer):
        def __init__(self, searcher):
            self.searcher = searcher
    
        def score(self, matcher):
            obj = self.searcher.stored_fields(matcher.id())
            t = time.mktime(parser.parse(obj["time"]).timetuple())
            n = time.mktime(datetime.datetime.now().timetuple())
            return t-n
        


    def scorer(self, searcher, fieldname, text, qf=1):
        return self.Scorer(searcher)


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "SimpleHTTP/" + __version__

    def do_GET(self):
        o = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(o.query)
     
           
        """Serve a GET request."""
        if self.path.startswith("/search"):
            f = self.search(query)
        elif self.path.startswith("/relation"):
            f = self.relation(query)            
        elif self.path == "/":
            f = self.getFile("search.html")
        else:
            f = self.getFile(self.path[1:])
        
        if f:
            try:
                shutil.copyfileobj(f,  self.wfile)
            finally:
                f.close()

    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.list_directory()
        if f:
            f.close()

    def relation(self, query):
        if "f" in query.keys():
            fff = query["f"][0]
        else:
            fff =""  
        if "t" in query.keys():
            ttt = query["t"][0]
        else:
            ttt =""  
    
        print fff,"VS",ttt
        
        res = []
        for record in graph.cypher.execute("MATCH (x:E) WHERE x.N='"+fff+"' MATCH (y:E) WHERE y.N='"+ttt+"' MATCH p = allShortestPaths(x-[*..20]-y) RETURN p"):
           one = []
           for row in record:
               for col in row:
                   one.append(str(col))
           res.append(one)
           break

            
        f = StringIO()   
        f.write(json.dumps(res,indent=4))
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f   
    
    def search(self, query):
        ix = open_dir("news")
        if "s" in query.keys():
            s = query["s"][0]
        else:
            s =""    
    
        if "w" in query.keys():
            if query["w"]=="c":
                w = scoring.TF_IDF()
            elif query["w"]=="b":
                w = scoring.BM25F()
            else:
                w = TimeWeight()
        else:
            w = OurWeight()    
    
        ret = {"r":[],"s":{}}
        with ix.searcher() as searcher:
            
            parser = MultifieldParser(["t","d"], ix.schema, group=OrGroup).parse(unicode(s,"UTF-8"))
            results = searcher.search(parser, limit=100)
            for r in results:
             
                ret["r"].append({"t":r["t"],"d":r["d"],"p":r["time"],"l":r["link"],"e":r["tags"],"r":r["tags"]})
        
        
            corrector = searcher.corrector("d")
            for m in s.split():
                sug = corrector.suggest(m, limit=3)
                for s in sug:
                    if m not in ret["s"].keys():
                        ret["s"][m] = []
                    ret["s"][m].append(s)        
        
            print ret["s"]
        f = StringIO()   
        f.write(json.dumps(ret,indent=4, separators=(',', ': ')))
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f     
   
    def getFile(self,fpath):
        if fpath == "favicon.ico":
            return None     
        f = open(fpath,"r")        
        f.seek(0, os.SEEK_END)        
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

def test(HandlerClass = RequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
