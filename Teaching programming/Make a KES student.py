#Sub program

#chracteristics

#Sam Doughty
Sam = {"size" : ["large"],
       "fattness" : ["thin"],
       "aura" : ["0"],
       "IQ" : ["1M", "1m"],
       "style" : ["average"]}
Samcounter = 0
#Reese He
Reese ={"size" : ["regular"],
       "fattness" : ["regular"],
       "aura" : ["100"],
       "IQ" : ["0"],
       "style" : ["skibidi"]}
Reesecounter = 0
#Ralfs Varpins
Ralfs = {"size" : ["regular"],
       "fattness" : ["regular"],
       "aura" : ["1000"],
       "IQ" : ["100"],
       "style" : ["skibidi"]}
Ralfscounter = 0
#Zeke Knights
Zeke = {"size" : ["regular"],
       "fattness" : ["thin"],
       "aura" : ["1000"],
       "IQ" : ["0"],
       "style" : ["skibidi"]}
Zekecounter = 0
#Advin Varghese
Advin = {"size" : ["small"],
       "fattness" : ["fatty"],
       "aura" : ["0"],
       "IQ" : ["0"],
       "style" : ["ugly"]}
Advincounter=0
#Main program
ready = input("Are you ready to make a KES student!? (y/n) ")
if ready == "n":
    print("YOUR A BETA!")
elif ready == "y":
    print("Okay lets begin!")
    size = input("Enter the persons size-hint(small, regular or large) ")
    fattness = input("Enter the persons fattness-hint(thin, regular or fatty) ")
    aura = input("Enter the persons aura-hint(0, 100 or 1000) ")
    IQ = input("Enter the persons IQ-hint(0, 100 or 1M) ")
    style = input("Enter the persons dress sense-hint(ugly, average or skibidi) ")
#output a student
if size in Sam["size"]:
    Samcounter += 1
if size in Ralfs["size"]:
    Ralfscounter += 1
if size in Reese["size"]:
    Reesecounter += 1
if size in Zeke["size"]:
    Zekecounter += 1
if size in Advin["size"]:
    Advincounter += 1
if fattness in Sam["fattness"]:
    Samcounter += 1
if fattness in Ralfs["fattness"]:
    Ralfscounter += 1
if fattness in Reese["fattness"]:
    Reesecounter += 1
if fattness in Zeke["fattness"]:
    Zekecounter += 1
if fattness in Advin["fattness"]:
    Advincounter += 1
if aura in Sam["aura"]:
    Samcounter += 1
if aura in Ralfs["aura"]:
    Ralfscounter += 1
if aura in Reese["aura"]:
    Reesecounter += 1
if aura in Zeke["aura"]:
    Zekecounter += 1
if aura in Advin["aura"]:
    Advincounter += 1
if IQ in Sam["IQ"]:
    Samcounter += 1
if IQ in Ralfs["IQ"]:
    Ralfscounter += 1
if IQ in Reese["IQ"]:
    Reesecounter += 1
if IQ in Zeke["IQ"]:
    Zekecounter += 1
if IQ in Advin["IQ"]:
    Advincounter += 1
if style in Sam["style"]:
    Samcounter += 1
if style in Ralfs["style"]:
    Ralfscounter += 1
if style in Reese["style"]:
    Reesecounter += 1
if style in Zeke["style"]:
    Zekecounter += 1
if style in Advin["style"]:
    Advincounter += 1

counter = [Samcounter,Ralfscounter,Reesecounter,Zekecounter,Advincounter]
names = ["Sam","Ralfs","Reese","Zeke","Advin"]
c = ["", -1]
for x in range(len(counter)):
    if c[1] < counter[x]:
     c[1] = counter[x]
     c[0] = names[x]

print("WOWZA YOU CREATED",c[0],"THE WORST PERSON EVER!")
    
    

    
