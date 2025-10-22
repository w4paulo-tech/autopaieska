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
