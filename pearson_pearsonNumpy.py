from math import sqrt
import numpy

users = {
        "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def pearson(rating1,rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    udaloSiePorownac = False
    korelacja=0
    i=0
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    for klucz in klucze1: 
        if klucz in rating2.keys():
            udaloSiePorownac = True
            a1 = a1 + ((rating2[klucz]) * (rating1[klucz]))
            a2= a2 +(rating2[klucz])
            a3= a3 +(rating1[klucz])
            a4= a4 + ((rating1[klucz])**2)
            a5= a5 + ((rating2[klucz])**2)
            i=i+1
    korelacja=(a1-((a2*a3)/i))/((sqrt(a4-((a3**2)/i)))*(sqrt(a5-((a2**2)/i))))
    return korelacja
print "Wspó³czynnik korelacji wynosi: "  + str(pearson(users["Bonia"],users["Ania"]))


def pearsonNumpy(rating1,rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    korelacja = 0
    udaloSiePorownac = False
    lista1=[]
    lista2=[]
    for klucz in klucze1: 
        if klucz in rating2.keys():
            udaloSiePorownac = True
            lista1.append(rating1[klucz])
            lista2.append(rating2[klucz])
    korelacja=numpy.corrcoef(lista1, lista2)[0, 1]

    return korelacja

print "Wspó³czynnik korelacji z numpy wynosi: "  + str(pearsonNumpy(users["Ania"], users["Bonia"]))

