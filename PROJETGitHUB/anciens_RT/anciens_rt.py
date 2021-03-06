#!/usr/bin/python3


def write_html_header(fichier, titre):
    fichier.write("<!DOCTYPE html>\n")
    fichier.write("<html>\n")
    fichier.write("<head>\n")
    fichier.write(("<title>"+titre)+"</title>\n")
    fichier.write("<meta name=\"ROBOTS\" content=\"NOINDEX, NOFOLLOW\">\n")
    fichier.write("<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\n")
    fichier.write("<meta http-equiv=\"content-type\" content=\"application/xhtml+xml; charset=UTF-8\">\n")
    fichier.write("<meta http-equiv=\"content-style-type\" content=\"text/css\">\n")
    fichier.write("<meta http-equiv=\"expires\" content=\"0\">\n")
    fichier.write("<link href=\"./sae15.css\" rel=\"stylesheet\" type=\"text/css\">\n")
    fichier.write("</head>\n")
    
def write_html_body_begin(fichier):
    fichier.write("<body>\n")

def write_html_body_end(fichier):
    fichier.write("</body>\n")

    
def write_html_body(fichier):
    fichier.write("<header>\n")
    fichier.write("\t <h1><b>Les anciens eleves de RT</b></h1>\n")
    fichier.write("</header>\n")
    fichier.write("<nav><p id=\"intro\">Bonjour, voici une page que nous avons cree pour avoir un apercu de ce que deviennent les anciens etudiants de Chatellerault.</p>\n")
    fichier.write("<p id=\"intro\">Voici, ci-dessous, certains profils d'anciens etudiants en Reseaux et Telecommunications a l'IUT de Chatellerault.</p>\n")
    fichier.write("</nav>\n")
    
def write_html_table(fichier, colonne1, colonne2, colonne3, colonne4, colonne5):
    fichier.write("<section>\n")
    fichier.write("<p>\n")
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
    fichier.write("</p>\n")
    fichier.write("</section>")

def write_html_footer(fichier):
    fichier.write("<footer>\n")
    fichier.write("<p>Sources : </p>")
    fichier.write("<p><a  href=\"https://fr.linkedin.com/\" target=\"blank\"><img src=\"data:image/png;base64,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\" width=\"40\" height=\"33\" alt=\"\"></a> <a  href=\"https://viadeo.journaldunet.com/\" target=\"blank\"><img src=\"data:image/png;base64,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\" width=\"40\" height=\"33\" alt=\"\"></a> </p>\n")
    fichier.write("<p>Qui sommes-nous ? Bastien Gibel et Jonas Bourreau, actuellement etudiants en RT.</p>\n")
    fichier.write("<p>Pour nous contacter : <a style=\"color: pink;\" href=\"mailto:bastien.gibel@etu.univ-poitiers.fr?\" target=\"_top\">Envoyer un mail a Bastien</a>  ou <a style=\"color: pink;\" href=\"mailto:jonas.bourreau@etu.univ-poitiers.fr?\" target=\"_top\">Envoyer un mail a Jonas</a></p>\n")
    fichier.write("</footer>\n")
    
def write_html_end(fichier):
    fichier.write("</html>")
    
fichier = open("../html/fichier1.html", "w")
write_html_header(fichier,"Projet_RT")
write_html_body_begin(fichier)
write_html_body(fichier)
colonne1 = ["test", 2, 3, 4]
colonne2 = [4, 5, 6, 8]
colonne3 = [4, 5, 7, 2]
colonne4 = [4, 5, 4, 3]
colonne5 = [4, 5, 3, 8]
write_html_table(fichier, colonne1, colonne2, colonne3, colonne4, colonne5)
write_html_footer(fichier)
write_html_body_end(fichier)
write_html_end(fichier)


fichier.close()
