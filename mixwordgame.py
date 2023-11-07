import enchant
import pwinput
print ("\tWelcome to Khannapong's Word Game")
enchant.Dict("en_US")
gameend = 0
print ("START [Y]")
print("EXIT [n]")
x=input("Type here: ")
while(x.lower()!='y' and x.lower()!='n'):
 x=input()
 print(x)
#ATTEMPTS FOR PLAYERS
attempt1=4
attempt2=4
wordcheck=enchant.Dict("en_US")
if x.lower()=='y':
        while gameend == 0:
            print("------------------------------------")
            print("\tGame is starting...")
            print("------------------------------------")
            print("Enter the word")
            #WORD2=WORD THAT PLAYER 2 HAVE TO GUESS
            word2=pwinput.pwinput("Player 1: ")
            while wordcheck.check(word2)==False:
                print("Please check you have typed you word correctly")
                word2=pwinput.pwinput("Player 1: ")
            #WORD1=WORD THAT PLAYER 1 HAVE TO GUESS
            word1=pwinput.pwinput("Player 2: ")
            while wordcheck.check(word1)==False:
                print("Please check you have typed you word correctly")
                word1=pwinput.pwinput("Player 2: ")
            #PLAY2 = TEMP OF WORD 2
            play2=list(word2)
            word2=list(word2)
            play1=list(word1)
            word1=list(word1)
            ans1=""
            for i in word1:
                ans1+=str(i)
            ans2=""
            for i in word2:
                ans2+=str(i)    
            tag1=0
            tag2=0
            while attempt1 !=0  and attempt2 != 0:
                if attempt1 == 4 and attempt2 == 4:
                    print ("Player 1 Turn:\nAttempt(s) = ",attempt1)
                    print("The Word: ",end='')
                    for x in range (len(play1)):
                        play1[x]="_"
                        print(play1[x],end=' ')
                    g1=input("\nGuess a character: ")
                    while len(g1) > 1:
                        g1=input("Type only 1 character: ")
                    for x in range (len(play1)):
                        if word1[x].lower()==g1.lower():
                            play1[x]=word1[x].upper()
                            print(play1[x].upper(),end=' ')
                        else:
                            print("_",end=' ')
                    attempt1-=1
                    anstmp=input("\nGuess the word: ")
                    if anstmp.lower()==ans1.lower():
                        print("You are correct, the word is ",ans1.upper())
                        tag1=1
                    else:
                            print(anstmp.upper(),"is not correct")
                    print("------------------------------------")
                    print ("Player 2 Turn:\nAttempt(s) = ",attempt2)
                    print("The Word: ",end='')
                    for x in range (len(play2)):
                        play2[x]="_"
                        print(play2[x],end=' ')
                    g2=input("\nGuess a character: ")
                    while len(g2) > 1:
                        g2=input("Type only 1 character: ")
                    for x in range (len(play2)):
                        if word2[x].lower()==g2.lower():
                            play2[x]=word2[x].upper()
                            print(play2[x].upper(),end=' ')
                        else:
                            print("_",end=' ')
                    attempt2-=1
                    anstmp=input("\nGuess the word: ")
                    if anstmp.lower()==ans2.lower():
                        print("You are correct, the word is ",ans2.upper())
                        tag2=1
                    else:
                            print(anstmp.upper(),"is not correct")
                    print("------------------------------------")
                elif attempt1==0 or attempt2==0 or (tag1==1 and tag2==1):
                    if attempt1>attempt2:
                        print("Player 1 is the winner")
                        print("The word are",ans1.upper(),"and",ans2.upper())
                    elif attempt1==attempt2:
                        print("Draw")
                        print("The word are",ans1.upper(),"and",ans2.upper())
                    else:
                        print("Player 2 is the winner")
                        print("The word are",ans1.upper(),"and",ans2.upper())
                    print("------------------------------------")
                    print("Thank you for playing!")
                    print("------------------------------------")
                    exit(3)
                else:
                    if (tag1==0):
                        print ("Player 1 Turn:\nAttempt(s) = ",attempt1)
                        print("The Word: ",end='')
                        for x in range (len(play1)):
                            print(play1[x],end=' ')
                        g1=input("\nGuess a character: ")
                        while len(g1) > 1:
                            g1=input("Type only 1 character: ")
                        for x in range (len(play1)):
                            if word1[x].lower()==g1.lower():
                                play1[x]=word1[x].upper()
                                print(play1[x].upper(),end=' ')
                            else:
                                print(play1[x],end=' ')
                        attempt1-=1
                        anstmp=input("\nGuess the word: ")
                        if anstmp.lower()==ans1.lower():
                            print("You are correct, the word is ",ans1.upper())
                            tag1=1
                        else:
                            print(anstmp.upper(),"is not correct")
                        print("------------------------------------")
                    if (tag2==0):
                        print ("Player 2 Turn:\nAttempt(s) = ",attempt2)
                        print("The Word: ",end='')
                        for x in range (len(play2)):
                            print(play2[x],end=' ')
                        g2=input("\nGuess a character: ")
                        while len(g2) > 1:
                            g2=input("Type only 1 character: ")
                        for x in range (len(play2)):
                            if word2[x].lower()==g2.lower():
                                play2[x]=word2[x].upper()
                                print(play2[x].upper(),end=' ')
                            else:
                                print(play2[x],end=' ')
                        attempt2-=1
                        anstmp=input("\nGuess the word: ")
                        if anstmp.lower()==ans2.lower():
                            print("You are correct, the word is ",ans2.upper())
                            tag2=1
                        else:
                            print(anstmp.upper(),"is not correct")
                        print("------------------------------------")
elif (x.lower()=='n'):
    print ("See you again next time...")
    exit()
