#Voila maintenant je suis entrain de m'exercer sur GitHub tout en ajoutant ce code sur ce fichier main.py qui va etre envoyer vers mon répertoire local !
def pangramme(string):
    alphabet = "azertyuiopqsdfghjklmwxcvbn"
count=0
for letter in alphabet:
    if letter in string:
count+=1
if count == 26:
    return True
else:
    return False
phrase = input()
phrase = phrase.lower()

print(pangramme(phrase))
