import hashlib

#hashage du mot de passe avec a l'aide de la librairie hashlib
def hashmotdepasse(motdepasse):
    motdepasshash = hashlib.sha256(motdepasse.encode()).hexdigest()
    return motdepasshash


#fonction qui a pour fonction de verifier si les conditions du mot de passe ont bien été respecté 


def mdp_check(str):
    i = 0
    maj = 0
    min = 0
    num = 0
    spe = 0
    if len(str) > 8:
        while i < len(str):
            if str[i].isupper() == True:
                maj += 1
            if str[i].isnumeric() ==True:
                num += 1
            if str[i].islower() == True:
                min += 1
            if str[i] == "!" or str[i] == "@" or str[i] == "#" or str[i] == "$" or str[i] == "%" or str[i] == "^" or str[i] == "&" or str[i] == "*":
                spe += 1
            i+=1
    
    if num>=1 and maj >= 1 and min >= 1 and spe >= 1 and len(str) > 8:
        return 1
    else:
        return 0


#fonction qui a pour fonction d'informer l'utilisateur du processus de vérification 


def informations():
    turn = 0
    mdp = input("Choisissez votre mot de passe :")
    check = mdp_check(mdp)
    while turn < 4:
        if check > 0:
            motdepasshash = hashmotdepasse(mdp)
            print("Votre mode passe respecte les conditions de sécurité")
            break
        else:
            mdp = input("Votre mode passe ne pas respecte les conditions de sécurité : ")
            check = mdp_check(mdp)
            turn +=1
    if turn > 0 and check == 0:
        print("Votre mot de passe ne respecte pas les conditions de sécurité !")

informations()
