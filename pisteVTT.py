# -*- coding: utf-8 -*-
import os
import urllib2
from BeautifulSoup import BeautifulSoup

rep="/media/Stockage/Data/Sites/map/scripts/"

#On recupere le texte sur le wiki
#page = urllib2.urlopen("http://wiki.openstreetmap.org/wiki/User:Awikatchikaen")
page = urllib2.urlopen("http://wiki.openstreetmap.org/wiki/FR:BeCikloXmlPistes")
soup = BeautifulSoup(page)
blocXMLs = soup.findAll('div',id='XMLBeciklo',recursive=True)

texteEntier="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE Map>"
for blocXML in blocXMLs:
	#On vire le bloc <pre>
	texte = str(blocXML.find('pre').contents[0])
	#On remet les balises
	texte = texte.replace('&lt;','<').replace('&gt;','>').replace('&quot;','\"')
	#les signes 'different' (<>) sont enleves
	texte =  texte.replace('<>','&lt;&gt;')
 	#on enleve les doubles lignes vides
	texte = texte.replace("\n\n",'\n')
	texteEntier =texteEntier+texte

#on supprime et recre le fichier xml
xmlfile = open(rep+'osm.xml/pisteCyclable.xml', 'w')
xmlfile.write(texteEntier)
xmlfile.close()
