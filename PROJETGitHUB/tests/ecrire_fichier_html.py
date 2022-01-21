#!/usr/bin/python3


def write_html_header(fichier, titre):
    fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    fichier.write("<!DOCTYPE html>\n")
    fichier.write("<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">\n")
    fichier.write("<style>\n")
    fichier.write("table, th, td {\n")
    fichier.write("border:1px solid black;")
    fichier.write("}\n")
    fichier.write("</style>")
    
    fichier.write("\t <head>\n")
    fichier.write(("\t\t<title>"+titre)+"</title>\n")
    fichier.write("\t </head>\n")
    
def write_html_body_begin(fichier):
    fichier.write("<body>\n")

def write_html_body_end(fichier):
    fichier.write("</body>\n")

    
def write_html_body(fichier):
    fichier.write("Blablabla...\n")
    
def write_html_table(fichier, colonne1, colonne2, colonne3, colonne4, colonne5):
    fichier.write("<table>\n")
    fichier.write("<tr>")
    fichier.write("\t<th> Nom </td>")
    fichier.write("\t<th> Prenom </td>")
    fichier.write("\t<th> Promotion </td>")
    fichier.write("\t<th> Situation apres le DUT R&T </td>")
    fichier.write("\t<th> Situation actuelle </td>")
    fichier.write("\t</tr>\n")
    for i in range(len(colonne1)):
         fichier.write("<tr>")
         fichier.write("\t<td>"+str(colonne1[i])+"</td>")
         fichier.write("\t<td>"+str(colonne2[i])+"</td>")
         fichier.write("\t<td>"+str(colonne3[i])+"</td>")
         fichier.write("\t<td>"+str(colonne4[i])+"</td>")
         fichier.write("\t<td>"+str(colonne5[i])+"</td>")
         fichier.write("\t</tr>\n")
    fichier.write("</table>\n")
        
def write_html_end(fichier):
    fichier.write("</html>")
    
fichier = open("fichier.html", "w")
write_html_header(fichier,"Mon titre")
write_html_body_begin(fichier)
#write_html_body(fichier)
colonne1 = ["test", 2, 3, 4]
colonne2 = [4, 5, 6, 8]
colonne3 = [4, 5, 7, 2]
colonne4 = [4, 5, 4, 3]
colonne5 = [4, 5, 3, 8]
write_html_table(fichier, colonne1, colonne2, colonne3, colonne4, colonne5)
write_html_body_begin(fichier)
write_html_end(fichier)


fichier.close()
