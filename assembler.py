simport shutil
def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))
shutil.copy('code.txt', 'code2.txt')
code = open('code.txt')
linetot = 0
lineCT = 0
flag = 0
flagdec = 1
wordCT = 0
indirect =0
#ma3 kol lafa bethot el line fe string w bet3ed el lines
for line in code:
    words = line.split()
    if words[0] != "//": 
      linetot = linetot + 1
code = open('code.txt')
ins = open('ins.txt','r')
inst =  ins.read()

for line in code:
     words = line.split()
     if words[0] != "//": 

      for word in words:
          #check if indirect
            if len(word) == 1 and word == "I":
              indirect =1
          #checks ORG is first or not
            if lineCT == 0 and words[0] != "ORG" and wordCT == 0:
                print("Error Missing ORG instruction at line : 1", "Instead of word:", word, " suggested solution: add ORG")
                flag = 1
                break
            elif words[0] == "ORG":
                org = words[1]

          #checks end is last or not
            if lineCT == linetot-1 and words[0] != "END":
                print("Error missing END instruction at line:" , lineCT+1, "Instead of word:", word, " suggested solution: is add END")
                flag = 1
                break
           #checks the instrctions with 1 words
            if len(words) == 1:
                #checks if instruction valid
                 if (len(word) !=3 or word not in inst) and lineCT != linetot-1:
                        print("Uknown instruction in line: " , lineCT+1, "\nSuggested solution: check instruction")  
                        flag = 1
                        break
           #checks the instruions with 2 words and if variables are declared
            if len(words) == 2 and lineCT != 0:
                codDec = open('code2.txt')
                # checks if variable decleared
                for line in codDec:
                       klam = line.split()
                       if words[1]+"," == klam[0]:
                           flagdec = 0

                if flagdec != 0 :
                       print("Error undecleared variable: " , lineCT+1, "\nSuggested solution: decleare variable" , words[1])  
                       flag = 1
                       break
                if words[0] not in inst:
                        print("Uknown instruction in line: " , lineCT+1, "\nSuggested solution: check instruction")  
                        flag = 1
                        break
                if words[1].isdigit() :
                        print("forgot to add variable?: " , lineCT+1, "\nSuggested solution: add variavle to hold value")  
                        flag = 1
                        break

           #checks the instruions with 3 words
            if len(words) == 3:
              #checks the comma after variables
                if words[0][len(words[0])-1] != "," and words[0] not in inst :
                        print("Error Missing comma at line: " , lineCT+1, "\nSuggested solution: you forgot the comma")  
                        flag = 1
                        break
              #checks the comma after variables        
                variables = ""
                for letter in words[0] :
                    if letter == ",":
                        break
                    variables= variables + letter
                if variables in inst:
                    print("Flipped instruction at line" , lineCT+1)
                    flag = 1
                    break
              #variable declare dec or hex
                if  words[1] != "DEC" and words[1] != "HEX" and words[2].isdigit():
                    print("Variable type is not declared" , lineCT+1 ,"Insted of ",words[1])
                    flag = 1
                    break
                if not words[2].isdigit() and words[2][0] != "-" and words[2][0] != "I" :
                    print("Error Add value to varivble", lineCT+1,"\n suggested solution:add value to variable")
                    flag = 1
                    break
            if len(words) > 3:
                print("Error Extra instrution at line", lineCT+1,"\n suggested solution: delete: any aditional instrulineCTions")
                flag = 1
                break

            wordCT +=1
      wordCT = 0
      if flag == 1:
          break
      lineCT +=1


if flag != 1:
   code = open('code.txt')
   ins = open('ins.txt','r')
   out = open('output.txt','a')
   inst =  ins.read()
   org = int(org,16)
   print("Memory Location:")
   i=1
   list1 = ["Memory Location:"]
   list2 = ["Machine Code In hex"]
   for i in range(linetot-1): 
       print(hex(org)[2:])
       list1.append(hex(org)[2:])
       org = org +1
   org = org - lineCT+1
   loc = org
   # fetching code
   print("Machine code in HEX:")
   zero = "0"
   for line in code:
     words =line.split()
     if words[0] != "//": 
       lineCT +=1
       wordsCT=0
       for word in words:
           if word == "END":
               break
           if word in inst and not word.isdigit():
               klam =inst.split()
               i=0
               for kelma in klam:
                   i += 1
                   if kelma == word:
                       print(word," ",end ="")
                          
                       if i < 29:
   
                          codDec = open('code2.txt')
                          codecre= codDec.readlines()
                          
                          for j in range(len(codecre)):
                                 sprech = codecre[j].split()
                                 if words[1]+"," == sprech[0]:
                                     loc = j
                                     loc = hex(j + org-1)[2:]
   
                          if not indirect:
                              print(klam[i]+loc)
                              list2.append(klam[i]+loc)
   
                          else:
                              print(klam[i+2]+loc)
                              list2.append(klam[i+2]+loc)
   
                              
                       else:
                           print(klam[i])
                           list2.append(klam[i])
   
           elif word == "DEC" or word == "HEX":
               print(word," ",end ="")
               if word == "DEC":
                       zero = "0"
                       put = tohex(int(words[wordsCT +1]), 16)[2:]
                       while len(put) <4 :
                            put = zero + tohex(int(words[wordsCT +1]), 16)[2:]
                            zero = zero + zero
                       print(put)
                       list2.append(put)
               else:
                   put = words[wordsCT +1]
                   zero = "0"
                   while len(put) < 4:
                       put = zero + put
                       zero = zero +zero
                       
                   print(put)
                   list2.append(put)
                   
   
           wordsCT +=1 
   
   
   #output
   j=0
   i=1
   for i in range (linetot*2-2):
       if i % 2 !=0:
           print(list2[j])
           out.write(list2[j]+"\n")
           j+=1
       else:
           print(list1[j]," " ,end="")
           out.write(list1[j]+" ")
           
       
any = input("done")
