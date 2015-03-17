import re
import urllib2

from bs4 import BeautifulSoup, CData
import pymongo


feeds =['http://feeds.dn.pt/DN-Portugal',
        'http://feeds.dn.pt/DN-Globo',
        'http://feeds.dn.pt/DN-Economia',
        'http://feeds.dn.pt/DN-Ciencia',
        'http://feeds.dn.pt/DN-Artes',
        'http://feeds.dn.pt/DN-Media',
        'http://feeds.dn.pt/DN-Opiniao',
        'http://feeds.dn.pt/DN-Pessoas',
        'http://feeds.dn.pt/DN-Desporto',
        'http://feeds.dn.pt/DN-Cartaz',
        'http://feeds.dn.pt/DN-Politica',
        'http://feeds.dn.pt/DN-Gente',
        'http://feeds.dn.pt/DN-Galeria',
        'http://feeds.jn.pt/JN-ULTIMAS',
        'http://feeds.jn.pt/JN-Destaques',
        'http://feeds.jn.pt/JN-Politica',
        'http://feeds.jn.pt/JN-Sociedade',
        'http://feeds.jn.pt/JN-Saude',
        'http://feeds.jn.pt/JN-Educacao',
        'http://feeds.jn.pt/JN-Media',
        'http://feeds.jn.pt/JN-Seguranca',
        'http://feeds.jn.pt/JN-Economia',
        'http://feeds.jn.pt/JN-Pais',
        'http://feeds.jn.pt/JN-Mundo',
        'http://feeds.jn.pt/JN-Brasil',
        'http://feeds.jn.pt/JN-Palops',
        'http://feeds.jn.pt/JN-MundoInsolito',
        'http://feeds.jn.pt/JN-Desporto',
        'http://feeds.jn.pt/JN-Cultura',
        'http://feeds.jn.pt/JN-Gente',
        'http://feeds.jn.pt/JN-Tecnologia',
        'http://feeds.jn.pt/JN-Tendencias',
        'http://feeds.jn.pt/JN-Galerias',
        'http://feeds.jn.pt/JN-Videos',
        'http://feeds.jn.pt/JN-Audios',
        'http://feeds.jn.pt/JN-Infografias',
        'http://feeds.tsf.pt/TSF-Ultimas',
        'http://feeds.tsf.pt/TSF-Destaques',
        'http://feeds.tsf.pt/TSF-Portugal',
        'http://feeds.tsf.pt/TSF-Internacional',
        'http://feeds.tsf.pt/TSF-Economia',
        'http://feeds.tsf.pt/TSF-Desporto',
        'http://feeds.tsf.pt/TSF-Vida',
        'http://feeds.tsf.pt/TSF-Motores',
        'http://feeds.feedburner.com/jornali?format=xml',
        'http://www.cmjornal.xl.pt/rss.aspx',
        'http://expresso.sapo.pt/static/rss/atualidade--arquivo_23412.xml',
        'http://expresso.sapo.pt/static/rss/economia_23413.xml',
        'http://expresso.sapo.pt/static/rss/desporto_23414.xml',
        'http://expresso.sapo.pt/static/rss/dossies_23415.xml',
        'http://expresso.sapo.pt/static/rss/postais_23418.xml',
        'http://expresso.sapo.pt/static/rss/blogues_23423.xml',
        'http://expresso.sapo.pt/static/rss/opiniao_23424.xml',
        'http://expresso.sapo.pt/static/rss/multimedia_23430.xml',
        'http://expresso.sapo.pt/static/rss/iniciativas-e-produtos_23436.xml',
        'http://expresso.sapo.pt/static/rss/a-vida-de-saltos-altos_24943.xml',
        'http://expresso.sapo.pt/static/rss/gic_24979.xml',
        'http://expresso.sapo.pt/static/rss/audio_25020.xml',
        'http://expresso.sapo.pt/static/rss/cartoon_25024.xml',
        'http://expresso.sapo.pt/static/rss/leve-as-suas-criancas_25041.xml',
        'http://expresso.sapo.pt/static/rss/liga-200910_25190.xml',
        'http://expresso.sapo.pt/static/rss/sociedade_25194.xml',
        'http://expresso.sapo.pt/static/rss/a-europa-desalinhada_25281.xml',
        'http://expresso.sapo.pt/static/rss/dinheiro_25283.xml',
        'http://expresso.sapo.pt/static/rss/futuro-sustentavel-2010_25341.xml',
        'http://expresso.sapo.pt/static/rss/pt_25568.xml',
        'http://expresso.sapo.pt/static/rss/mercados_25511.xml',
        'http://expresso.sapo.pt/static/rss/24-horas-tt-2011_25516.xml',
        'http://expresso.sapo.pt/static/rss/optimus-alive_25585.xml',
        'http://expresso.sapo.pt/static/rss/quero-estudar-melhor_25593.xml',
        'http://expresso.sapo.pt/static/rss/mes-do-ambiente-do-expresso-2014_25751.xml',
        'http://expresso.sapo.pt/manchetes_feed.rss'
        ]


print feeds


for feed in feeds:
    try:
        response = urllib2.urlopen(feed)
        print "##### ",feed, " #####"
        rss = response.read()
        soup = BeautifulSoup(rss, "xml")
        soup.prettify()
        for tag in soup.findAll('title'):
            print tag.string.strip()
    except urllib2.URLError, e:
        print feed, " | ", e

