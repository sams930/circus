# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


print("spēle cirks")
pozicija1 = 0 # sākuma pozicijas
pozicija2 = 0
while True: # dod variantus kurš iet pirmais vai beigt spēli
    print("\nizvēleties kurš met pirmais un uzpidied 1")
    print("1. spēletajs1 met kauluiņus")
    print("2. spēletajs2 met kauliņus")
    print("3. beigt spēli")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
            
            import random
            
            x = random.randint(1, 6) #izvēlas cipars no 1-6
            y = (x + pozicija1) #saskaita doto ciparu ar poziciju
            pozicija1 = pozicija1 + x #saglaba doto poziciju
            print("spelētājs1 iet uz priekšu", x) #uzraksta cik izkrita
            print("spēletaja1 pozicija", y) #uzrksta spēletaja poziciju
            if pozicija1 == 18:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija pazeminās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 7
                print("spēletaja1 pozicija", pozicija1)
            if pozicija1 == 67:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija pazeminās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 46   
                print("spēletaja1 pozicija", pozicija1)         
            if pozicija1 == 80:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija pazeminās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 69
                print("spēletaja1 pozicija", pozicija1)
            if pozicija1 == 74:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija pazeminās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 63
                print("spēletaja1 pozicija", pozicija1)


            if pozicija1 == 15:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija paugstinās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 24
                print("spēletaja1 pozicija", pozicija1)
            if pozicija1 == 39:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija paugstinās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 48   
                print("spēletaja1 pozicija", pozicija1)         
            if pozicija1 == 33:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija paugstinās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 52
                print("spēletaja1 pozicija", pozicija1)
            if pozicija1 == 87:# ja spēletaja numurs ir tādas kāds uz kāpnēm tad spēletaja pozicija paugstinās
                print("jūs uzkāpāt uz kāpnēm")
                pozicija1 = 96
                print("spēletaja1 pozicija", pozicija1)

         
            if pozicija1 > 100: # ja spēletaja pozicija ir 100 tad viņš uzvar
                print("spēletājs1 uzvarēja")
                break# spēle beidzās
            pass
    elif choice == '2': # spēletajam 2 ir tas pats kas ir 1
            
            import random
            
            x = random.randint(1, 6)
            y = (x + pozicija2)
            pozicija2 = pozicija2 + x
            print("spelētājs2 iet uz priekšu", x)
            print("spēletaja2 pozicija", y)
            if pozicija2 == 18:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 7
                print("spēletaja1 pozicija", pozicija2)
            if pozicija2 == 67:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 46   
                print("spēletaja1 pozicija", pozicija2)         
            if pozicija2 == 80:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 69
                print("spēletaja1 pozicija", pozicija2)
            if pozicija2 == 74:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 63
                print("spēletaja1 pozicija", pozicija2)


            if pozicija2 == 15:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 24
                print("spēletaja1 pozicija", pozicija2)
            if pozicija2 == 39:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 48   
                print("spēletaja1 pozicija", pozicija2)         
            if pozicija2 == 33:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 52
                print("spēletaja1 pozicija", pozicija2)
            if pozicija2 == 87:
                print("jūs uzkāpāt uz kāpnēm")
                pozicija2 = 96
                print("spēletaja1 pozicija", pozicija2)




            if pozicija2 > 100:
                print("spēletājs2 uzvarēja")
                break
            pass
    elif choice == '3': # var beigt spēli jebkāda momentā
        print("paldies par spēli")
        break









