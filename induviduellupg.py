class Inloggning:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.name = ""
        self.lastname = ""
        self.age = 0
                            
   #def kontrollera(self, username, password):
        #return self.username == username and self.password == password
        #hade det först men gjorde en annan lösning istället
inlogg = []

def logga_in(username, password):
    for user in inlogg:
        if user.username == username:
            if user.password == password:
                return "rätt", user
            
            else:
                return "lösenord", None
#ksk elif här lättare att läsa
    return "användare", None

def kontrollera_lösenord(password):
    stor_bokstav = False
    
    for tecken in password:
        if tecken.isupper():
            stor_bokstav = True
            
    if len(password) >= 10 and stor_bokstav: 
        return "rätt"
    return "fel"


val_1 = 0

while val_1 != 4:
    print("---HUVUDMENY---")
    print("1. Logga in")
    print("2. Skapa användare")
    print("3.Visa användare")
    print("4. Avsluta")

    val_1 = int(input())

    if val_1 == 1:
        print ("Logga in")
        username = input("Användarnamn: ")
        password = input("Lösenord: ")
        
        resultat, user = logga_in(username, password)

        if resultat == "rätt":
            print("Välkommen!", username)

            val_2 = 0
           
                            
                    
            while val_2 != 4:
                print("---PROFIL---")
                print("1.Visa profil")
                print("2.Ändra profil")
                print("3.Ändra lösenord")
                print("4.Logga ut")
                
                val_2 = int(input())

                if val_2 == 1:
                    
                    print("Namn: ", user.name)
                    print("Eftermanm: ", user.lastname)
                    print("Ålder: ", user.age)
                    

                elif val_2 == 2:

                    #def spara_beskrivning(name, lastname, age):
                    user.name = input("Vad är ditt namn?: ")
                    user.lastname = input("Vad är ditt efternamn?: ")
                    user.age = int(input("Hur gammal är du?: "))
                    #spara_beskrivning = Inloggning(name, lastname, age)
                    #beskrivning_lista.append(spara_beskrivning)

                elif val_2 == 3:
                    
                    ändra_lösenord = input("Skriv in ditt nya lösenord: ")
                    user.password = ändra_lösenord
                    print("Lösenordet har ändrats.")
                    
                        

        elif resultat == "användare":
            print("Okänd användare")
        elif resultat == "lösenord":
            print("Fel lösenord")
                

    elif val_1 == 2:
        print("Skapa användare")
        username = input("Skriv in ditt användarnamn: ")
        password = input("Skriv in ditt lösenord: ")
        
        if kontrollera_lösenord(password) == "rätt":
            nytt_inlogg = Inloggning(username, password)
            inlogg.append(nytt_inlogg)
            
        else:
            print("Lösenordet måste innehålla minst 10 tecken och en stor boksvan försök igen")
        #while så den inte går tillbaka

    elif val_1 == 3:
        for user in inlogg:
            print(user.username)
    

