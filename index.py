#1. Gör ett valfritt program som suddar skärmen med os.system(‘cls’) vid flera tillfällen. Du kan även uppdatera ett gammalt program
import os
import time 
import msvcrt
import random
from colors import bcolors

print("skiv 'cls' to clear the screen")
aws = input("skriv här: ")
if aws == ("cls"):
    os.system('cls')
#2. Använd sleep()-kommandot i valfritt projekt och spara som nytt filnamn sleep() används när du vill att programmet väntar innan det fortsätter
a = float(input("hur mycket väger du i kilo "))
b = float(input("hur lång är du i m "))
time.sleep(10)
print("det här är din BMI" , a//(b**2))
#3. Gör ett välkomstprogram som väntar på en knapptryckning (utan ENTER) innan det avslutas - getwch()
print("hej och välkomen till mitt program")
namn = input("vad heter du ")
age = input("hur gammal är du ")
print("ay skriv '1' eller '2' för om du vill ha det på engelska eller svenska")
svar_1 = int(msvcrt.getwch())
if svar_1 == 1:
    print("hello " + namn + " you are " + age + " years old")
if svar_1 == 2:
    print("hej " + namn + " du är " + age + " år gammal")

#4. Gör en modul som ändrar färg (kolla flödet här på CR)
#5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig
print("få ett random nummer i en random färg")
while True:
    game = int(input("""
skriv '1' för att starta 
skriv '2' för att avlsuta
                    """))
    if game == 1:
        random_number = random.randint(1, 100)
        random_number2 = random.randint(1, 6)
        if random_number2 == 1:
            print(bcolors.PURPLE , random_number)
        if random_number2 == 2:
            print(bcolors.BLUE , random_number)
        if random_number2 == 3:
            print(bcolors.CYAN , random_number)
        if random_number2 == 4:
            print(bcolors.GREEN , random_number)
        if random_number2 == 5:
            print(bcolors.YELLOW , random_number)
        if random_number2 == 6:
            print(bcolors.RED , random_number)
    if game == 2:
        break
    else:
        print("restart")
#6. Uppdatera gärna något annat gammalt program med getwch() och färger!


lives = 7
import random
run_game = True
secret_number = random.randint(0, 9)
print("ayy gissa nummret")
while True:
    try:
        print("enter number 0 <= x <= 9: ")
        number = int(msvcrt.getwch())
    except:
        print("nah uh")
    if number > secret_number:
        print("AYYY sänk farten")
        lives -= 1
        print("lives left " , lives)
    if number < secret_number:
        print("nah för lågt")
        lives -= 1
        print("lives left " , lives)
    if number == secret_number:
        print(bcolors.GREEN, '''
        ================
        abow du har rätt
        ================
        ''')
        svar1 = input("Börja om? Y/N ")
        if svar1 == "N":
            break
        if svar1 == "Y":
            lives = 7
            secret_number = random.randint(0,9)
        else:
            print("VA????")
            break
    if lives == 0:
        print(bcolors.RED, '''
             =========== 
              Game Over
             ===========
              ''')
        svar = input("Börja om? Y/N ")
        if svar == "N":
            break
        if svar == "Y":
            lives = 7
            secret_number = random.randint(0,9)
        else:
            print("VA????")
            break