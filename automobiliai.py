<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("automobiliai.db")
c = conn.cursor()

with conn:
    c.execute("""
    CREATE TABLE IF NOT EXISTS automobiliai (
    markė VARCHAR(50) NOT NULL,
    modelis VARCHAR(50) NOT NULL,
    spalva VARCHAR(50),
    pagaminimo_metai VARCHAR(50),
    kaina INT
    )""")



while True:
    veiksmas = input("\n1 - Įvesti automobilį, 2 - Ieškoti automobilio, 0 - Išeiti: ")
    match veiksmas:
        case "1":
            print("Įveskite automobilį")
            markė = input("Markė: ")
            modelis = input("Modelis: ")
            spalva = input("Spalva: ")
            pagaminimo_metai = input("Pagaminimo metai: ")
            kaina = input("Kaina: ")
            with conn:
                c.execute("INSERT INTO automobiliai VALUES (?, ?, ?, ?, ?)", 
                          (markė, modelis, spalva, pagaminimo_metai, kaina))
        
        case "2":
            print("Įveskite ieškomo automobilio duomenis")
            with conn:
                c.execute("SELECT * FROM automobiliai")
                cars = c.fetchall()

            ieskoma = []
            sarasas = []

            markė = input("Markė: ")
            ieskoma.append(markė) if markė else ieskoma.append("___")
            modelis = input("Modelis: ")
            ieskoma.append(modelis) if modelis else ieskoma.append("___")
            spalva = input("Spalva: ")
            ieskoma.append(spalva) if spalva else ieskoma.append("___")
            metai_nuo = input("Nuo metų: ")
            ieskoma.append(metai_nuo) if metai_nuo else ieskoma.append("___")
            metai_iki = input("Iki metų: ")
            ieskoma.append(metai_iki) if metai_iki else ieskoma.append("___")
            kaina_nuo = input("Minimali kaina: ")
            ieskoma.append(kaina_nuo) if kaina_nuo else ieskoma.append("___")
            kaina_iki = input("Maksimali kaina: ")
            ieskoma.append(kaina_iki) if kaina_iki else ieskoma.append("___")

            def metai():
                if metai_nuo != "" and metai_iki != "":
                    return int(metai_nuo) <= int(car[3]) <= int(metai_iki)
                elif metai_nuo == "" and metai_iki != "":
                    return int(car[3]) <= int(metai_iki)
                elif metai_iki == "" and metai_nuo != "":
                    return int(metai_nuo) <= int(car[3])
                else:
                    return True
                    

            for car in cars:
                if markė.lower() == car[0].lower() or markė == "":
                    if modelis.lower() == car[1].lower() or modelis == "":
                        if spalva.lower() == car[2].lower() or spalva == "":
                            if metai():                              
                                try:
                                    if int(kaina_nuo) <= int(car[4]) <= int(kaina_iki):
                                        sarasas.append(car)
                                except ValueError:
                                    try:
                                        if car[4] <= int(kaina_iki) and kaina_nuo == "":
                                            sarasas.append(car)
                                    except ValueError:
                                        try:
                                            if int(kaina_nuo) <= car[4] and kaina_iki == "":
                                                sarasas.append(car)  
                                        except ValueError:                                 
                                            if kaina_nuo == "" and kaina_iki == "":
                                                sarasas.append(car)                                           
                else:
                    continue

            if len(sarasas) == 0:
                print(f"{"".center(100, "-")}")
                print(f"Saraše nėra tokio automobilio.\nMarkė: {ieskoma[0]}, "
                    f"modelis: {ieskoma[1]}, spalva: {ieskoma[2]}, "
                    f"nuo {ieskoma[3]} iki {ieskoma[4]} metų, "
                    f"kaina nuo \u20ac{ieskoma[5]} iki \u20ac{ieskoma[6]}")
            else:
                print(f"{"".center(100, "-")}") 
                # sarasas = sorted(sarasas, key=lambda x: x[3], reverse=True)
                sarasas.sort(key=lambda x: x[4], reverse=True)
                for auto in sarasas:
                    print(f"{auto[3]}m. {auto[0]} {auto[1]}, spalva: {auto[2]}"
                        f", kaina: \u20ac{auto[4]}")
                print(f"{"".center(100, "-")}")    
                print(f"Rastų automobilių: {len(sarasas)}"
                        f"\nMarkė: {ieskoma[0]}, "
                        f"modelis: {ieskoma[1]}, spalva: {ieskoma[2]}, "
                        f"nuo {ieskoma[3]} iki {ieskoma[4]} metų, "
                        f"kaina nuo \u20ac{ieskoma[5]} iki \u20ac{ieskoma[6]}")
                print(f"{"".center(100, "-")}")  
                                        
        case "0":
            print("Viso gero")
            break
        
        case _:
            print("Netinkamas pasirinkimas")
=======
import sqlite3

conn = sqlite3.connect("automobiliai.db")
c = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS automobiliai (
    markė VARCHAR(50) NOT NULL,
    modelis VARCHAR(50) NOT NULL,
    spalva VARCHAR(50),
    pagaminimo_metai VARCHAR(50),
    kaina INT
);
"""

with conn:
    c.execute(query)

while True:
    veiksmas = int(input("1 - Įvesti automobilį, 2 - Ieškoti automobilio, 0 - Išeiti: "))
    match veiksmas:
        case 1:
            print("Įveskite automobilį")
            markė = input("Markė: ")
            modelis = input("Modelis: ")
            spalva = input("Spalva: ")
            pagaminimo_metai = input("Pagaminimo metai: ")
            kaina = input("Kaina: ")
            with conn:
                c.execute("INSERT INTO automobiliai VALUES (?, ?, ?, ?, ?)", 
                          (markė, modelis, spalva, pagaminimo_metai, kaina))
        
        case 2:
            print("Įveskite ieškomo automobilio duomenis")
            with conn:
                c.execute("SELECT * FROM automobiliai")
                cars = c.fetchall()

            ieskoma = []
            sarasas = []

            markė = input("Markė: ")
            if markė:
                ieskoma.append(markė)
            else:
                ieskoma.append("__")
            modelis = input("Modelis: ")
            if modelis:
                ieskoma.append(modelis)
            else:
                ieskoma.append("__")
            spalva = input("Spalva: ")
            if spalva:
                ieskoma.append(spalva)
            else:
                ieskoma.append("__") 
            metai_nuo = input("Nuo metų: ")
            if metai_nuo:
                ieskoma.append(metai_nuo)
            else:
                ieskoma.append("__")
            metai_iki = input("Iki metų: ")
            if metai_iki:
                ieskoma.append(metai_iki)
            else:
                ieskoma.append("__")
            kaina_nuo = input("Minimali kaina: ")
            if kaina_nuo:
                ieskoma.append(kaina_nuo)
            else:
                ieskoma.append("__")
            kaina_iki = input("Maksimali kaina: ")
            if kaina_iki:
                ieskoma.append(kaina_iki)
            else:
                ieskoma.append("__")

            for car in cars:
                if markė == car[0] or markė == "":
                    if modelis == car[1] or modelis == "":
                        if spalva == car[2] or spalva == "":
                            if metai_nuo <= car[3] <= metai_iki or metai_nuo == "" and metai_iki == "":
                                try:
                                    if int(kaina_nuo) <= car[4] <= int(kaina_iki):
                                        sarasas.append(car)
                                except ValueError:
                                    if kaina_nuo == "" and kaina_iki == "":
                                        sarasas.append(car)
                                    try:
                                        if car[4] <= int(kaina_iki) and kaina_nuo == "":
                                            sarasas.append(car)  
                                    except ValueError:                                 
                                        if int(kaina_nuo) <= car[4] and kaina_iki == "":
                                            sarasas.append(car)
                else:
                    continue
                            
            if len(sarasas) == 0:
                print(f"Saraše nėra tokio automobilio.\nMarkė: {ieskoma[0]}, "
                    f"modelis: {ieskoma[1]}, spalva: {ieskoma[2]}, "
                    f"nuo {ieskoma[3]} iki {ieskoma[4]} metų, "
                    f"kaina nuo \u20ac{ieskoma[5]} iki \u20ac{ieskoma[6]}")
            else:     
                print(f"Rasti automobiliai:")
                for auto in sarasas:
                    print(auto)
                        

        case 0:
            print("Viso gero")
            break

        case _:
            print("Netinkamas pasirinkimas")
>>>>>>> 32e1aba7ad8ce7d2fa990c024b4954d1309eb64d
