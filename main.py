import enchant

exists = enchant.Dict("en_US")

word = input("Enter The word  :  ")
L = list(word)
length = len(L)
for i in range (length):
    suf = L[-i:]
    suf = "".join(suf)
    #print(suf)
    suf=suf+"\n"
    with open('readme.txt') as f:
        lines = f.readlines()
        for x in lines:
            if suf == x:
               # print("suf is equal to x")
                r_word = "".join(L[0:len(L)-i])
               # print(r_word)
                while True:
                    res = exists.check(r_word)
                    if res == True :
                        break
                    else:
                        tem_word = r_word
                        if r_word[-1] == r_word[-2]:
                           # print("consecutive not")
                            tem_word = r_word[:-1]
                            res = exists.check(tem_word)
                            if res == True:
                                r_word = tem_word
                                break
                        if r_word[-1] == "y":
                            tem_word=r_word[:-1]
                            tem_word=tem_word+"ie"
                            res = exists.check(tem_word)
                            if res == True:
                                r_word = tem_word
                                break
                        if r_word[-1] == "i":
                            tem_word=r_word[:-1]
                            tem_word=tem_word+"y"
                            res = exists.check(tem_word)
                            if res == True:
                                r_word = tem_word
                                break
                        if r_word[-1] != "e":
                           # print("adding e")
                            tem_word=r_word+"e"
                            res = exists.check(tem_word)
                            if res == True:
                                r_word = tem_word
                                #print(r_word)
                                break
                            else:
                                break
                if exists.check(r_word):
                    print("root form of the word is : - ")
                    print(r_word)


