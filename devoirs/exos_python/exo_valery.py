# -*- coding: utf-8 -*-
from lxml import etree
from collections import Counter
mlfile = "valery_ame-et-danse_1921.xml"

#initialiser la lecture du fichier
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(mlfile,parser)

#la racine
root = tree.getroot()

#utiliser un espace de nom
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE

#afficher le nom de l'éditeur
for element in root.iter(TEI + "edition"):
    print(element.text)

#afficher l'url de la licence            
for element in root.iter(TEI + "licence"):
    print(element.attrib.get("target"))
    
#afficher le personnage avec le plus de tours de parole et le nombre de tours
nbRepliq = Counter()
for element in root.iter(TEI + "div"):
    for child in element:
        if child.tag == TEI + "label" and child.attrib.get("type") == "speaker":
            nbRepliq[child.text]+=1
    print(nbRepliq.most_common(1))

#ajouter un autre <respStmt> avec deux enfants name et resp contenant du texte
for element in root.iter(TEI + "editionStmt"):
    child = etree.SubElement(element, "respStmt")
    subchild1 = etree.SubElement (child, "name")
    subchild1.text = "Clémence"
    subchild2 = etree.SubElement (child, "resp")
    subchild2.text = "Ajout d'enfants dans le document"

#modifier la valeur de la signature <signed> pour afficher le texte en majuscule
for element in root.iter(TEI + "signed"):
    for child in element:
        child.text = child.text.upper()
        
#on réécrit l'arbre pour voir nos modifications      
tree.write(mlfile, encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
    