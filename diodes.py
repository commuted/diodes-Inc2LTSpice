import re

'''
Add Diodes Inc BJT spice decks to LTSpice standard.bjt

cat output to >> .\Documents\LTspiceXVII\lib\cmp\standard.bjt

Read Diodes Inc file: Transistor (BJT) Master Table.spice.txt
Add Vceo, Icrating iand mfg=diodesinc which are scraped from the 
file: Transistor (BJT) Master Tablr.xlsx
Remove spurious line gaps in + notation:w.
Remove spurious subckt ends'''


# Scrape master CVS doc to get Vceo and Icrating parameters for parametric selection
csv = dict()
with open('master.csv','r+') as fcsv:  
  for line in fcsv:
    x = line.strip().split(',')
    csv[x[0]]=x
 

p = re.compile('\)') # accomodate occasional use of () in single line models
flag = True

with open('out.txt','w', encoding='utf-8-sig') as f:
    with open("master.spice.txt", "r+") as fp:
      for line in fp:
        line = line.strip()
        x = line.split()
        if x: # something on line
          # remove purious subckt ends
          if x[0].strip().lower() == '.ends': #process subckt ends
            if flag == True: # remove purious subckt ends
              print("removing spurious ends",line)
              line = ''
            else:# close subckt
              flag = True
          if (x[0].strip().lower() =='.subckt') and (flag == True): # process start of subckt
            flag = False
          if x[0] =='.MODEL': # line is start of spice model
            if x[1] in csv: # part name also in in spreadsheet csv file
              br = p.search(line)
              if br: # test for sometimes '()' brackets
                vce = csv[x[1]][3].strip()[0:-1]
                im  = str(float(csv[x[1]][4].strip()[0:-1]) )
                line = line[0:br.span()[0]] + " mfg=DiodesInc " + "Vceo="+vce  + " Icrating="+im +")"
              else:
                vce = csv[x[1]][3].strip()[0:-1]
                im  = str(float(csv[x[1]][4].strip()[0:-1]) )
                line = line.strip()
                line = (line + " mfg=DiodesInc " + "Vceo="+vce  + " Icrating="+im)
          if line:   
            
            f.writelines(line+'\n')
