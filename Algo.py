import csv
with open('Motoren.csv')as daten:
    reader = csv.reader(daten, delimiter= ';')

    datencounter = 0
    counter0 =0
    mod0haufigkeit=0
    counter1 =0
    mod1haufigkeit=0

    for row in reader:
        print(row[0])
        print(row[1])
        if(row[0]==0  ):
          counter0= counter1+1

        if (row[0] == 1 ):
            counter1 = counter1 + 1




        print('\t')
        datencounter= datencounter+1

    datencounter = datencounter-1
    mod0haufigkeit= datencounter/counter0
    mod1haufigkeit= datencounter/counter1
    print('Anzahl der Daten:'+datencounter+ 'Haufigkeit Mod 0:'+mod0haufigkeit+'Häufigkeit Mod 1: '+mod1haufigkeit);





