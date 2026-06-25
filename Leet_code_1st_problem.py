# ----------------------------:Index wise merging of two strings:------------------------------
word1 = "ab"
word2 = "pq"
new = []
k = 0


if len(word1) == len(word2):

    for ch in word1:

        new.append(ch)
        new.append(word2[k])
        k += 1
    print(" ".join(new))


if len(word1) > len(word2):
    x = 0
    for ch in word1:
        new.append(ch)
        if x != len(word2):
            new.append(word2[x])
            x += 1
    print(" ".join(new))



if len(word1) < len(word2):
 y=0
 z=0
 for ch in word1:
     
     new.append(ch)
     new.append(word2[y])
     y+=1

 for i in range(y,len(word2)):
       
       new.append(word2[i])

    
       print(" ".join(new))


