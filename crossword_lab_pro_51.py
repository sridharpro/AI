

## Author: Sridhar Chowdhary  Created on: 13-DEC-2018
## M.Tech AI, CVR college of Engineering
## Under the guidance of Dr. R. Ponnusamy

## This program solves the crossword puzzle
## which is a constraint satisfaction problem
## additionally applying heuristic function
# Solution state:
#['C', 'A', 'T', '#']
#['O', 'N', '#', 'A']
#['A', 'D', '#', '#']
#['T', '#', 'W', 'E']


import itertools
class Crossword:
    def __init__(self):
        self.crossword = [['','','','#'],
                          ['','','#',''],
                          ['','','#','#'],
                          ['','#','','']]
        
        self.crosswordres =  [['','','','#'],
                              ['','','#',''],
                              ['','','#','#'],
                              ['','#','','']]
        
        self.allwords = ['AND','A','WE','COAT','CAT']
        self.completed_flag = False

        self.word_batch=[['','',''],[''],['',''],['','','',''],['','','']]
        self.word_batch_pos=[(0,0,0),(1,3,0),(3,2,0),(0,0,1),(0,1,1)]
        
        self.cons_0_3 =[]
        self.cons_0_4 =[]


        self.cons_0=[]
        self.cons_1=[]
        self.cons_2=[]
        self.cons_3=[]
        self.cons_4=[]

    def checkconstraints(self):

        if self.word_batch[0][0]!='' and self.word_batch[3][0] != '':
            self.cons_0_3 =[self.word_batch[0][0],self.word_batch[3][0]]
        else:
            self.cons_0_3 =['','']
        if self.word_batch[0][1] != '' and self.word_batch[4][0] != '':
            self.cons_0_4 =[self.word_batch[0][1],self.word_batch[4][0]]
        else:
            self.cons_0_4 = ['','']


        self.cons_0=[len(self.word_batch[0]),3]
        self.cons_1=[len(self.word_batch[1]),1]
        self.cons_2=[len(self.word_batch[2]),2]
        self.cons_3=[len(self.word_batch[3]),4]
        self.cons_4=[len(self.word_batch[4]),3]

        if (self.cons_0_3[0]==self.cons_0_3[1] and self.cons_0_4[0]==self.cons_0_4[1] \
            and self.cons_0[0]==self.cons_0[1]  and self.cons_1[0]==self.cons_1[1] \
            and self.cons_2[0]==self.cons_2[1] and self.cons_3[0]==self.cons_3[1] and \
            self.cons_4[0]==self.cons_4[1]):
            return True
        else:
            return False


    def clear(self):

        for i in range(len(self.crosswordres)):
            for j in range(len(self.crosswordres[0])):
                if self.crossword[i][j]=='#':
                    self.crosswordres[i][j]='#'
                else:
                    self.crosswordres[i][j]=' '
                
             
    def populate(self):

        for (word,x) in zip(self.word_batch,self.word_batch_pos):
            if x[2] == 0:
                for i in range(len(word)):
                    if word[i] != '': 
                        self.crosswordres[x[0]][x[1]+i]=word[i]
            elif x[2] == 1:
                for i in range(len(word)):
                    if word[i] != '':
                        self.crosswordres[x[0]+i][x[1]]=word[i]

    def heuristic(self,L):
        
        score=0
        for i in range(len(L)):
            if len(L[i])==len(self.word_batch[i]):
                score+=1
            else:
                score-=1
        return score

        
    def solve(self):


        combo_words_list=[]
        templist=[]
        combo_words=list(itertools.permutations(self.allwords,len(self.allwords)))
        for x in combo_words:
            templist=[]
            templist.append(self.heuristic(x))
            templist.extend(list(x))
            combo_words_list.append(templist)
        combo_words_list.sort(key=lambda p: p[0],reverse=True)
        

        jflag=True
        iflag=True
        for i_1 in [x for x in combo_words_list]:
            i=i_1[1:]
            iflag=True
            self.clear()
            for j in range(len(i)):
                jflag=True
                if len(i[j])==len(self.word_batch[j]):
                    self.word_batch[j]=list(i[j])
                    self.populate()
                else:
                    if j==0:
                        iflag=False
                    print('------------------------------')
                    print("Current Word:",i[j])
                    for k in range(len(self.crosswordres)):
                        print(self.crosswordres[k])    
                    break
                print('------------------------------')
                print("Current Word:",i[j])
                for k in range(len(self.crosswordres)):
                        print(self.crosswordres[k])
                jflag=self.checkconstraints()
                if jflag==False:
                    break
                elif jflag== True and j==len(i)-1:
                    self.completed_flag=True
                    break
            if iflag==False:
                break
            if self.completed_flag==True:
                break

            

    
                

cw1 = Crossword()
cw1.solve()
        
