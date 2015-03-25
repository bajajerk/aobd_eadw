from whoosh import scoring
from whoosh.analysis.analyzers import SimpleAnalyzer
from whoosh.analysis.filters import LowercaseFilter, StopFilter
from whoosh.analysis.tokenizers import SpaceSeparatedTokenizer
from whoosh.fields import NUMERIC, TEXT, Schema
from whoosh.index import open_dir, create_in
from whoosh.qparser.default import QueryParser
from whoosh.qparser.syntax import OrGroup


def index(dir,lines):
    schema = Schema(id = NUMERIC(stored=True), content=TEXT)
    ix = create_in(dir, schema)
    writer = ix.writer()
    for line in lines:
        
        partition = line.split(' ',1)
        i = int(partition[0])
        c = partition[1]

        
        
        writer.add_document(id=i,content=unicode(c,"UTF-8"))
    writer.commit()
    return ix

def indexNoStopWords(dir,lines):
    schema = Schema(id = NUMERIC(stored=True), content=TEXT)
    ix = create_in(dir, schema)
    writer = ix.writer()
    for line in lines:
        
        partition = line.split(' ',1)
        i = int(partition[0])
        c = partition[1]
        writer.add_document(id=i,content=unicode(stop(unicode(c,"UTF-8")),"UTF-8" ))
    writer.commit()
    return ix

def searchBM25(dir,index,query,lim):
    index = open_dir(dir)
    
    res = []
    
    with index.searcher() as searcher:
        query = QueryParser("content", index.schema, group=OrGroup).parse(unicode(query,"UTF-8"))
        results = searcher.search(query, limit=lim)
        for r in results:
            res.append(r["id"])
        
        
    return res


def searchCOS(dir,index,query,lim):
    index = open_dir(dir)
    
    res = []
    
    with index.searcher(weighting=scoring.TF_IDF()) as searcher:
        query = QueryParser("content", index.schema, group=OrGroup).parse(unicode(query,"UTF-8"))
        results = searcher.search(query, limit=lim)
        for r in results:
            res.append(r["id"])
        
        
    return res

def precision(result,expected):
    intersection = [val for val in result if val in expected]
    return float(len(intersection))/len(result)


def recall(result,expected):
    intersection = [val for val in result if val in expected]
    return float(len(intersection))/len(expected)

def f1(result,expected):
    Pr=precision(result, expected)
    Re=recall(result, expected)
    return (2*Re*Pr)/(Re+Pr)


def score(result,expected):
    intersection = [val for val in result if val in expected]
    if len(intersection)>0:
        Pr=float(len(intersection))/len(result)
        Re=float(len(intersection))/len(expected)
        F1=(2*Re*Pr)/(Re+Pr)
        return {"Pr":Pr,"Re":Re,"F1":F1}
    return {"Pr":0,"Re":0,"F1":0}



def stop(text):
    stopper = StopFilter()
    tokenizer = SimpleAnalyzer()
    tokens = tokenizer(text)

    result = []
    for token in stopper(tokens):
        result.append(repr(token.text))
    return ' '.join(result)






def searchPageRank(dir,index,query,lim,rank):
    index = open_dir(dir)
    
    class PageRankScorer(scoring.BaseScorer):
        def __init__(self, idf):
            self.idf = idf
    
        def score(self, matcher):
            doc = str(matcher.id()+1)
            
            r = 0
            if doc in rank.keys():
                r = rank[doc]
            s = matcher.weight() * self.idf* r
            
            print doc," | ", s
            return s
        

    class pageRankWeight(scoring.WeightingModel):
        def scorer(self, searcher, fieldname, text, qf=1):
            # IDF is a global statistic, so get it from the top-level searcher
            parent = searcher.get_parent()  # Returns self if no parent
            idf = parent.idf(fieldname, text)
            return PageRankScorer(idf)
    
    res = []   
    with index.searcher(weighting=pageRankWeight()) as searcher:
        query = QueryParser("content", index.schema, group=OrGroup).parse(unicode(query,"UTF-8"))
        results = searcher.search(query, limit=lim)
        for r in results:
            res.append(r["id"])
        
        
    return res
