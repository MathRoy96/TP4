#importation du package csv
import csv

#Définir mes variables
total_interv_2015 = 0
total_interv_2016 = 0
total_interv_2017 = 0
total_interv_2018 = 0
total_interv_2019 = 0
moy_interv_par_annee = 0.0

#Ouvrir le fichier csv
csv_file = open("Données_TP4.csv")

#Enlever l'entête pour faciliter mes calculs
csv_file.readline()

csv_reader = csv.reader(csv_file, delimiter=';')

arrondissement = {}

for ligne in csv_reader :
    if ligne[9] == "Indetermine":
        if str(ligne[8]) in arrondissement.keys() :
            arrondissement[str(ligne[8])] += 1
        else :
            arrondissement[str(ligne[8])] = 1
    else:
        if str(ligne[9]) in arrondissement.keys() :
            arrondissement[str(ligne[9])] += 1
        else :
            arrondissement[str(ligne[9])] = 1
    if ligne[1] == "2015":
        total_interv_2015 += 1
    if ligne[1] == "2016":
        total_interv_2016 += 1
    if ligne[1] == "2017":
        total_interv_2017 += 1
    if ligne[1] == "2018":
        total_interv_2018 += 1    
    if ligne[1] == "2019":
        total_interv_2019 += 1


        
moy_interv_par_annee = (total_interv_2015 + total_interv_2016 + total_interv_2017 + total_interv_2018 + total_interv_2019) / 5

print("Le nombre total d'intervention à Montréal en 2015 :",total_interv_2015)
print("Le nombre total d'intervention à Montréal en 2016 :",total_interv_2016)
print("Le nombre total d'intervention à Montréal en 2017 :",total_interv_2017)
print("Le nombre total d'intervention à Montréal en 2018 :",total_interv_2018)
print("Le nombre total d'intervention à Montréal en 2019 :",total_interv_2019)
print("Le nombre moyen d'intervention par année à Montréal :",moy_interv_par_annee)

print(arrondissement)
