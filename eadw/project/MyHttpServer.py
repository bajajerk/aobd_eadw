
import BaseHTTPServer
import json
import os
import shutil
import sys
import urlparse

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser.default import MultifieldParser
from whoosh.qparser.syntax import OrGroup
from whoosh.scoring import BM25F, TF_IDF


__version__ = "0.6"

__all__ = ["MyHttpServer"]

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO



client = MongoClient('localhost', 27017)
db = client['eadw_proj']
news = db['news']




class TimeWeight(scoring.WeightingModel):        
    class TimeScorer(scoring.BaseScorer):
        def __init__(self, idfScorer,bm25Scorer,searcher):
            self.idfScorer = idfScorer
            self.bm25Scorer = bm25Scorer
            self.searcher = searcher
    
        def score(self, matcher):
            obj = self.searcher.stored_fields(matcher.id())
            # print obj
            s = self.bm25Scorer.score(matcher)*0.5+self.idfScorer.score(matcher)*0.5
            return s
        


    def scorer(self, searcher, fieldname, text, qf=1):
        # BM25
        bm25Scorer = BM25F().scorer(searcher, fieldname, text, qf) 
        tfidfScorer = TF_IDF().scorer(searcher, fieldname, text, qf)
        return self.TimeScorer(tfidfScorer,bm25Scorer,searcher)


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "SimpleHTTP/" + __version__

    def do_GET(self):
        o = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(o.query)
     
        
        """Serve a GET request."""
        if self.path.startswith("/search"):
            f = self.search(query)
        else:
            f = self.getPage()
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

     
    def search(self, query):
        ix = open_dir("news")
        if "s" in query.keys():
            s = query["s"][0]
        else:
            s =""
    
    
        ret = {"r":[],"s":[]}
        with ix.searcher(weighting=TimeWeight()) as searcher:
            
            parser = MultifieldParser(["t","d"], ix.schema, group=OrGroup).parse(unicode(s,"UTF-8"))
            results = searcher.search(parser, limit=100)
            for r in results:
                
                post = news.find_one({"_id":ObjectId(r["id"])})
                ret["r"].append({"t":post["t"],"d":post["d"],"p":post["p"],"l":post["l"],"e":r["tags"]})
        
        
            corrector = searcher.corrector("d")
            for m in s.split():
        
                ret["s"].append(corrector.suggest(m, limit=3))        
        
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
    
     
    def getPage(self):
        f = open("search.html","r")        
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
