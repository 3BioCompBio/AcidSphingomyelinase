import sys
import getopt

def readCommandLine(argv):
    if len(argv) == 0:
        print("Error: No argument was given!")
        printUsage()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv,"h",["help","var1=","var2="])

    except getopt.GetoptError as err:
        print(str(err))
        printUsage()
        sys.exit(2)

    parameters = {
        "var1": None,
        "var2": None 
    }

    for opt, arg in opts:
        if opt in ("-h","--help"):
            printUsage()
            sys.exit()

        elif opt == "--var1":
            parameters["var1"] = arg
        
        elif opt == "--var2":
            parameters["var2"] = arg

        else:
            print("Unknown argument(s): {}".format(opt))
            printUsage()
            sys.exit(2)

    if parameters["var1"] is None:
        print("Error: Missing --var1 parameter !")
        printUsage()
        sys.exit(2)

    return(parameters)


def loadData(fileName):
    try:
        dataFile = open(fileName,"r")
    
    except FileNotFoundError:
        print("Impossible to find {}. Please bring that file from".format(fileName))
        print("https://github.com/3BioCompBio/AcidSphingomyelinase in the same directory as this tool.")
        sys.exit(4)
    data = {}
    for line in dataFile.readlines():
        if line[0:7].lower() == "mutname":
            continue
        
        line = line.rstrip()
        mutName, Neutral, Npda, Npdb, Prediction = line.split(",")
        wt = mutName[0]
        pos = mutName[1:-1]
        
        synonymVar = wt + pos + wt
        
        if synonymVar not in data.keys():
            data.update({synonymVar: {"Neutral": 1.0, "NPDA": 0.0, "NPDB": 0.0, "Pred": "N"}})
            
        data.update({mutName: {"Neutral": float(Neutral), "NPDA": float(Npda), "NPDB": float(Npdb), "Pred":Prediction}})

    return data

def printUsage():
    print("""
This tool is used to predict the phenotype related to variants in the SMPD1 gene.
The predicted phenotype is either "A" for Niemann-Pick disease type A, "B" for Niemann-Pick disease type B
or "N" for a neutral phenotype.
USAGE:
    python SMPD1_ZooM.py -var1 VAR1 [-var2 VAR2]
        
PARAMETERS:
    -var1:   A variant in the SMPD1 gene. If given alone, SMPD1-ZooM will consider homozygocy and 
            predict the phenotype of a person holding that variant on both alleles.
            This has to be a proteic variant following the PDB 5i81 residue numbering (i.e W84C for example) 
            Synonymous variants (like W84W) are accepted (Mandatory).

    -var2:   A second variant in the SMPD1 gene. If given, SMPD1-ZooM will consider heterozygocy and
            predict the phenotype of a person holding both variants in their allele. (Optional)
""")
    
def getVarAnnotation(var):
    try:
        dataFile = open("NiemannPick.AllVariants.csv","r")

    except FileNotFoundError:
        print("Annotation file NiemannPick.AllVariants.csv not found in directory!")
        print("Impossible to check if given variant(s) is/are annotated in online databases")
        return None

    sequenceBasedMutName = var[0] + str(int(var[1:-1])+2) + var[-1]

    annotations = {}
    for line in dataFile.readlines():
        if line[0:7].lower() == "mutname":
            continue
        line = line.rstrip()
        columns = line.split(",")
        if columns[0] != sequenceBasedMutName:
            continue

        else:
            annotations.update({"Uniprot": columns[1], "ClinVar": columns[2], "INPDR": columns[3], "Combination": columns[4], "rs": columns[8]})
            return annotations

        return None

def averageProba(probaArray):
    
    nProba = len(probaArray)
    totalNeut = 0
    totalNpda = 0
    totalNpdb = 0
    for proba in probaArray:
        totalNeut = totalNeut + float(proba["Neutral"])
        totalNpda = totalNpda + float(proba["NPDA"])
        totalNpdb = totalNpdb + float(proba["NPDB"])
    
    prediction = ""
    avgNeut = totalNeut / nProba
    avgNpda = totalNpda / nProba
    avgNpdb = totalNpdb / nProba
    
    if avgNeut > avgNpda and avgNeut > avgNpdb:
        prediction = "N"
    elif avgNpda > avgNeut and avgNpda > avgNpdb:
        prediction = "A"
    elif avgNpdb > avgNeut and avgNpdb > avgNpda:
        prediction = "B"
    elif avgNpda == avgNpdb and avgNpda > avgNeut:
        prediction = "B"
    elif avgNpda == avgNeut and avgNpda > avgNpdb:
        prediction = "N"
    elif avgNpdb == avgNeut and avgNpdb > avgNpda:
        prediction = "N"
    else:
        print("Error! Unexpected case, please contact fancien@ulb.ac.be for correction.")
        exit(3)
    
    return ({"Neutral": avgNeut, "NPDA": avgNpda, "NPDB": avgNpdb, "Pred":prediction})



def main(argv):
    args = readCommandLine(argv)
    var1 = args["var1"]
    var2 = args["var2"]


# 1. Load the data
    wholeProteinPredictions = loadData("./NiemannPick.WholeProtein.Predictions.csv")

# 2. Check that the given variants are in the data
    if var1 not in wholeProteinPredictions.keys() or (var2 is not None and var2 not in wholeProteinPredictions.keys()):
        print("Error! One of the given variants is not found in the protein structure (PDB 5i81)")
        print("Variants given: var1 {}, var2 {}".format(var1,var2))
        print("The protein structure ranges from W84 to M611.")
        print("Make sure that the variants you gave also follow the structure residues numbering, not the sequence !")
        exit(1)

# 3. Get the probabilities for the two variants
    proba1 = wholeProteinPredictions[var1]
    proba2 = None
    average = None

    annotation1 =  getVarAnnotation(var1)
    
    if var2 is not None:
        proba2 = wholeProteinPredictions[var2]
        average = averageProba([proba1, proba2])

        annotation2 = getVarAnnotation(var2)


        if annotation1 is not None:
            print("Variant {} is annotated in online databases !".format(var1))
            print("Uniprot: {}, ClinVar: {}, INPDR: {}".format(annotation1["Uniprot"], annotation1["ClinVar"], annotation1["INPDR"]))
            if annotation1["rs"] != "/":
                print("Variant is found in dbSNP: {}".format(annotation1["rs"]))
            print("\n")


        if annotation2 is not None:
            print("Variant {} is annotated in online databases !".format(var2))
            print("Uniprot: {}, ClinVar: {}, INPDR: {}".format(annotation2["Uniprot"], annotation2["ClinVar"], annotation2["INPDR"]))
            if annotation2["rs"] != "/":
                print("Variant is found in dbSNP: {}".format(annotation2["rs"]))
            print("\n")

        print("An heterozygous patient with variants {} and {} is predicted as {}\n".format(var1,var2,average["Pred"]))
        print("Allele {} has the following predictions: P(Neutral) {:.3f}, P(NPDA) {:.3f}, P(NPDB) {:.3f}, Prediction {}".format(
                var1,
                proba1["Neutral"], 
                proba1["NPDA"],
                proba1["NPDB"],
                proba1["Pred"]))

        print("Allele {} has the following predictions: P(Neutral) {:.3f}, P(NPDA) {:.3f}, P(NPDB) {:.3f}, Prediction {}\n".format(
                var2,
                proba2["Neutral"], 
                proba2["NPDA"],
                proba2["NPDB"],
                proba2["Pred"]))

        print("Average values are: P(Neutral) {:.3f}, P(NPDA) {:.3f}, P(NPDB) {:.3f}, Prediction {}".format(
                average["Neutral"],
                average["NPDA"],
                average["NPDB"],
                average["Pred"]
        ))

    else:

        if annotation1 is not None:
            print("Variant {} is annotated in online databases !".format(var1))
            print("Uniprot: {}, ClinVar: {}, INPDR: {}".format(annotation1["Uniprot"], annotation1["ClinVar"], annotation1["INPDR"]))
            if annotation1["rs"] != "/":
                print("Variant is found in dbSNP: {}".format(annotation1["rs"]))
            print("\n")

        print("An homozygous patient with variants {} is predicted as {}\n".format(var1,proba1["Pred"]))
        print("Allele {} has the following predictions: P(Neutral) {:.3f}, P(NPDA) {:.3f}, P(NPDB) {:.3f}, Prediction {}".format(
                var1,
                proba1["Neutral"], 
                proba1["NPDA"],
                proba1["NPDB"],
                proba1["Pred"]))
            

    print()


if __name__ == "__main__":
    main(sys.argv[1:])