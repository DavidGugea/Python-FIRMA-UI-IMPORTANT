import pickle, sys, glob, random
if glob.glob("fBinary_UEC_SCRIPT.bin"):
    #Ask the user if he wants to rewrite the file, or if he wants to see the data 
    while True:
        question = input("The UEC binary file already exists. Would you like to rewrite the file ? -- > ")
        if question == "Yes" or question == "yes":
            break 
        else:
            dFile = open("fBinary_UEC_SCRIPT.bin", "rb")
            binList = []
            while True:
                try:
                    binList.append(pickle.load(dFile))
                    continue 
                except:
                    break 
            #print(binList)
            print("ADMINISTRATOR UEC CODE -- > {0}".format(binList[0]))
            print("WORKED UEC CODE -- > {0}".format(binList[1]))
            endInput = input("Press any key to close the programm. - - - >")
            sys.exit(0) 

dfile = open("fBinary_UEC_SCRIPT.bin", "wb")
alphabet = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I"]

ADMIN_UEC = ""
WORKER_UEC = ""

for i in range(5):
    ADMIN_UEC += random.choice(alphabet)
    WORKER_UEC += random.choice(alphabet)
for i in range(5):
    ADMIN_UEC += str(random.randint(1, 101))
    WORKER_UEC += str(random.randint(1, 101))
for i in range(5):
    ADMIN_UEC += random.choice(alphabet)
    WORKER_UEC += random.choice(alphabet)
for i in range(5):
    ADMIN_UEC += str(random.randint(1, 101))
    WORKER_UEC += str(random.randint(1, 101))

pickle.dump(ADMIN_UEC, dfile)
pickle.dump(WORKER_UEC, dfile)
dfile.close()
