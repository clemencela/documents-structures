# -*- coding: utf-8 -*-
from lxml import etree
mlfile = "Duchn-etiquetage.txt.xml"
tree = etree.parse(mlfile)
root = tree.getroot() 

#extraire tous les déterminants => accessibles dans une liste "determinants"
determinants = []
for element in root.iter("element"):
    for child in element:
        if child.attrib.get("type") == "type" and child.text == "DET:ART":
            for sibling in child.itersiblings():
                if sibling.attrib.get("type") == "string" : 
                    determinants.append(sibling.text)
               
#afficher les patrons DET-NOM
#on fait une liste avec tous les éléments (type + lemma + string)
elements = []
for element in root.iter("element"):
    for child in element:
        myTuple = tuple()
        if child.attrib.get("type") == "type" :
            typ = child.text
        if child.attrib.get("type") == "lemma" :
            lem = child.text
        if child.attrib.get("type") == "string" :
            s=child.text
        
    myTuple = (typ,lem,s)
    elements.append(myTuple)
      
#on parcourt la liste pour récupérer les patrons en question    
for i,token in enumerate(elements):
    if token[0] == "DET:ART" and elements[i+1][0] == "NOM":
        print(token[2] + " "+ elements[i+1][2])
 
#reconstruire les phrases => accessibles dans une liste "phrases"       
phrases = []
phrase = []
for token in elements:
    if  token[0] == "SENT":
        phrase.append(token[2])
        propre = "".join(phrase)
        phrases.append(propre)
        phrase = []
    else:
        phrase.append(token[2]+" ")

#transformer l'affichage en token/lemme/pos
for token in elements:
    print(f"{token[2]}/{token[1]}/{token[0]}")