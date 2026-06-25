s="a#b%*"

def fn(s):
 s3=[]
 for ch in s:
     if ch >= "a" and ch <="z":
          s3.append(ch)

     elif ch == "*" :
          s3.pop()

     elif ch == "#":
       s3.append(s3.copy()) 






     elif ch == "%":
          s3.reverse()

 output=[]


 for ch in s3:
    if type(ch)== list:
        output.append("".join(ch))
    else:
           output.append("".join(ch))    

 ret="".join(output)
 if not ret:
      return("")

 else:return("".join(output))



print(fn(s))