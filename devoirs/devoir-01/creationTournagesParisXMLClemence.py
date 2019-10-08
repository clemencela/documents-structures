# -*- coding: utf-8 -*-
import csv
from lxml import etree

with open("tournagesdefilmsparis2011.csv","r",encoding="utf-8") as tableFilms, open("tournagesParisXmlClemence.xml","wb") as sortieXml:
    films=csv.reader(tableFilms,delimiter=";")
    next(films)
	#la racine
    root=etree.Element("tournages_paris")
    for i,row in enumerate(films,start=1):
		#premier element sous racine
        tournage=etree.SubElement(root,"tournage")
		#ses attributs
        tournage.set("n",str(i))
		#l'element tournage va contenir d'autres elements avec du texte
        titre=etree.SubElement(tournage,"titre")
        titre.text=row[0]
        realisateur=etree.SubElement(tournage,"realisateur")
        realisateur.text=row[1]
        organisme=etree.SubElement(tournage,"organisme_demandeur")
        organisme.text=row[3]
        typtournage=etree.SubElement(tournage,"type_tournage")
        typtournage.text=row[4]
        lieu=etree.SubElement(tournage,"lieu")
		#les sous-elements de lieu avec du texte
        adresse=etree.SubElement(lieu,"adresse")
        adresse.text=row[2]
        arrondi=etree.SubElement(lieu,"arrondissement")
        arrondi.text=row[5]
        xy=etree.SubElement(lieu,"xy")
        xy.text=row[8]
        dates=etree.SubElement(tournage,"dates")
		#les sous-elements de dates avec du texte
        datedebut=etree.SubElement(dates,"date_debut")
        datedebut.text=row[6]
        datefin=etree.SubElement(dates,"date_fin")
        datefin.text=row[7]
	#on indique la racine de notre arborescence
    tree = etree.ElementTree(root)
	#on ecrit notre arborescence, la structure complete xml avec une declaration xml et une indentation propre
    tree.write(sortieXml, encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
       