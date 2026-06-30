# s = "Race! A56 car3#"
# s = "A man, a plan, a canal: Panama"
# s=""
s="0P"
lis=[]


for ch in s:

     if ch.isalnum() :
          
          lis.append(ch.lower())

Str="".join(lis)
lis.reverse()
str="".join(lis)



if str == Str :
  
    print("True")

else:

      print("False")    