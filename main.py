print ("Wilkommen zu meinem Quizz")

playing = input("Möchtest du Spielen (Ja/Nein) ")

if playing.lower() != "ja":
    quit()

print("Okay! Legen wir los :)")
score = 0

answer = input("was bedeutet cpu? ")
if answer.lower() == "central processing unit":
    print("richtig")
    score += 1
else:
    print("falsch")

answer = input("was bedeutet RAM? ")
if answer.lower() == "random access memory":
    print("richtig")
    score += 1
else:
    print("falsch")

answer = input("was bedeutet GPU? ")
if answer.lower() == "graphic processing unit":
    print("richtig")
    score += 1
else:
    print("falsch")

answer = input("was bedeutet psu? ")
if answer.lower() == "power supply unit":
    print("richtig")
    score += 1
else:
    print("falsch")

print("Deine Punktzahl ist: " + str(score) )
print("Du hast " + str((score/4) * 100) + "% Richtige antworten")