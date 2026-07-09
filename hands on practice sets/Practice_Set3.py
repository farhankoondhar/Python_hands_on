STR = "farhan  is "
# for i in STR:
if STR.count("  ") == 1:
        print ("detected double space : ")
        STR =STR.replace("  ", " ")
        print(STR)
else:
        print("NO double spaces found!...")