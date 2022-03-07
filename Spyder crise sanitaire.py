import pandas as pd
import numpy as np
import datetime


print ("Bonjour, voici un fichier vous permettant de voir les différentes personnes ayant fait leur vaccin"\
+" ayant fait leur première dose :\n"\
+" ayant fait leur vaccination complete\n"\
+" ayant fait leur dose de rappel\n"\
+" en fonction des jours "
+" En fonction de votre choix, un tableau avec les differentes doses faites par jour en France apparaitra")


dose_date = input("Quel date souhaitez-vous choisir ?  () 27/12/2020 jusqu'au 25/01/2022  :\n")
#class datetime.date (year, month, day)


dose_de_vaccins = int(input("Que souhaitez-vous choisir comme nombre de doses faites ? ( pour premiere dose taper 1: \n "\
                            +" pour vaccination_complete taper 2 : \n"\
                                +" pour dose_de_rappel taper 3 : \n "))

def get_record (dose_date, dose_de_vaccins):
    if dose_de_vaccins == 1:
        col_to_choose = "premiere_dose"
    elif dose_de_vaccins == 2:
        col_to_choose = "vaccination_complete"
    elif dose_de_vaccins == 3:
        col_to_choose = "dose_de_rappel"
    else:
        print ("Pas de colonne choisie !")
    print ("type (dose_date) = " + str (type (dose_date)))
    df_extract = df [df ["Date"]== dose_date]
    my_df = df.loc [:, ["Date", col_to_choose]]
    print (df_extract)
    print (my_df)
    return df_extract

# print (df.loc[df['vaccination complete']< 3400])

personne_dose_de_rappel = int(input("Souhaitez vous voir la liste des jours dans laquelle les personnes ayant eu ou non une dose de rappel ? ( pour une dose de rappel taper 4: \n "\
+"pour zero dose de rappel taper 5:\n"))

def record (personne_dose_de_rappel):
    if personne_dose_de_rappel == 4:
        print (df.loc[df['dose_de_rappel']=="1",:])
    elif personne_dose_de_rappel == 5:
        print (df.loc[df['dose_de_rappel']=="0",:])
    else:
        print ("Pas de dose choisie !")
    df_extract = df [df ["dose_de_rappel"]== personne_dose_de_rappel]
    print (df_extract)
    print (my_df)
    return df_extract

df=pd.read_csv("crise_sanitaire_comma.txt")
print (df.head())

get_record (dose_date, dose_de_vaccins)
record (personne_dose_de_rappel)


