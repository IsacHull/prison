# Skriv beskrivning för rum 1 och 2 och gör så att man kan navigera mellan dessa två rum

# MENYN
    # STARTA SPELET
    # AVSLUTA SPELET

# RUM 1 - CELLEN - HITTA NYCKELN LÅS UPP DÖRREN
    # SKRIV VAD SOM FINNS I RUMMET
def rum_1():
    print("\n--- Du är i en cell ---")
    print("Ditt mål är att hitta nyckeln och låsa upp dörren.")
    
    nyckel_hittad = False
    
    while True:
        print("\nVad vill du göra?")
        print("1. Undersök sängen")
        print("2. Undersök toaletten")
        print("3. Undersök golvet")
        print("4. Försök öppna dörren")
        
        val = input("Välj ett alternativ (1-4): ")
        
        if val == "1":
            print("Du kollar under sängen men hittar inget av värde.")
        elif val == "2":
            print("Du undersöker toaletten... och där ligger en NYCKEL!")
            nyckel_hittad = True
        elif val == "3":
            print("Du söker igenom golvet men hittar ingenting.")
        elif val == "4":
            if nyckel_hittad:
                print("Du använder nyckeln och låser upp dörren! Du är fri... för nu.")
                break
            else:
                print("Dörren är låst. Du behöver en nyckel.")
        else:
            print("Ogiltigt val, försök igen.")
    
rum_1()



def rum_2():
    print("\n--- Du är i ett pusselrum ---")
    print("Du befinner dig i ett stort öppet rum.")
    print("Längst bak ser du en gallerförsedd dörr med en trappa bakom.")
    print("En röst ljuder: 'För att gå vidare måste du svara på denna gåta:'")
    print("\"Vad går upp och ner utan att röra sig?\"")
    
    rätt_svar = "trappor"
    försök = 3

    while försök > 0:
        svar = input(f"\nDu har {försök} försök kvar. Ditt svar: ").strip().lower()
        
        if svar == rätt_svar:
            print("Rösten säger: 'Korrekt! Du får gå vidare.'")
            print("Dörren öppnas och du går vidare ner för trappan...")
            return  
        else:
            försök -= 1
            if försök > 0:
                print("Fel svar. Försök igen.")
            else:
                print("Fel svar. Du har slut på försök.")
                print("Ett larm går igång! Vakterna kommer och släpar dig tillbaka till cellen...")
                rum_1() 

rum_1()
rum_2()

# Du får tre försök på o svara, om alla tre svar är fel så går ett larm och vakter kommer och tar dig tillbaka till första rummet, svara rätt en gång och du får gå vidare


# RUM 3 - EN FIENDE SOM SPELAREN BEHÖVER TA SIG FÖRBI
    # RUMSBESKRIVNING
    # HUR SKA MAN VINNA MOT FIENDEN?
    # VAL SOMSPELAREN KAN GÖRA



# RUM 4 - DU HAR KLARAT SPELET AVSLUTANDE TEXT
    # AVSLUTNINGSTEXT