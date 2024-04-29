#1--write a program to print all the vlaues in a tuple .
##a=('avi','ram',20)
##b=a
##print(b)

#2--Write a program to print all the values of a tuple in a list
##a=('avi','ram',20)
##b=[]
##b.append(a)
##print(b)
##i=0
##while i<len(a):
##    b.append(a[i])
##    i+=1
##print(b)

#3--wap to print all the even digits to another tuple
##a=(2,3,4,5,2,6,7,8,9,0,4)
##i=0
##z=()
##while i<len(a):
##    if a[i]%2==0:
##        z+=(a[i],)
##    i+=1
##print(z)

#4--wap to print all the even digits to another list
##a=(2,3,4,5,2,6,7,8,9,0,4)
##i=0
##z=[]
##while i<len(a):
##    if a[i]%2==0:
##        z.append(a[i])
##    i+=1
##print(z)

#5--wap to print all the odd digits to another tuple
##a=(2,3,4,5,2,6,7,8,9,0,4)
##i=0
##z=()
##while i<len(a):
##    if a[i]%2!=0:
##        z+=(a[i],)
##    i+=1
##print(z)

#6--wap to print all the odd digits to another list
##a=(2,3,4,5,2,6,7,8,9,0,4)
##i=0
##z=[]
##while i<len(a):
##    if a[i]%2!=0:
##        z.append(a[i])
##    i+=1
##print(z)

#7--wap to get alphabet from a tuple and add it to another tuple
##a=('a','b',123,'@')
##i=0
##k=()
##while i<len(a):
##    if not(isinstance(a[i],int)):
##     
##     if "A"<=a[i]<="Z" or "a"<=a[i]<="z":
##        k+=(a[i],)
##    i+=1
##print(k)

#8-- WAP to extract all numbers from tuples
##a=('a','b',123,'@')
##i=0
##z=()
##while i<len(a):
##    if isinstance(a[i],int):
##        z+=(a[i],)
##    i+=1
##print(z)

#9-- WAP to extract all special characters from tuples
##a=('a','b',123,'@')
##i=0
##z=()
##while i<len(a):
##    if not(isinstance(a[i],int))and not("a"<=a[i]<="k") and not("A"<=a[i]<="Z"):
##        z+=(a[i],)
##    i+=1
##print(z)

#10-- WAP to convert lower case alphabet to upercase
##a="ascilijailh"
##j=''
##i=0
##while i<len(a):
##    if "a"<=a[i]<="z":
##        j+=chr(ord(a[i])-32)
##    i+=1
##print(j)


#11--Wap to convert all lowercase alphabet to upper case
##a="ascilijailh".upper()
##j=''
##i=0
##while i<len(a):
##    if "A"<=a[i]<="Z":
##        j+=chr(ord(a[i])+32)
##    i+=1
##print(j)


#12--WAP to find the length of the tuple\
##a=("sss",99,'@@@')
##print(len(a))


#13--WAP to find the length of the tuple\
##a=("sss",99,'@@@')
##i=0
##for n in a:
##    i+=1
##print(i)

#14--wap to find the number of alphabets present in a tuple
##a=("s","k",99,'@@@')
##i=0
##j=0
##while i<len(a):
##     if not(isinstance(a[i],int)):
##        if 'a'<=a[i]<='z' or 'A'<=a[i]<='Z':
##          print((a[i]))   
##          j+=1
##     i+=1
##print(j)

#15--WAP to find number of numbers in a tuple
##a=("s","k",99,'@@@',88,77)
##i=0
##j=0
##for n in a:
##     if isinstance(a[i],int):
##          j+=1
##     i+=1
##print(j)

##16.wap to find the number of special characters in a tuple.
##a=("s","k",99,'@@@',88,77)
##i=0
##j=0
##for n in a:
##     if not(isinstance(a[i],int)):
##          if not('a'<=a[i]<='z' or 'A'<=a[i]<='Z'):
##              j+=1
##     i+=1
##print(j)

##17.wap to reverse a tuple.
##a=("s","k",99,'@@@',88,77)
##print(a[::-1])

##18.wap to reverse a tuple w/o using slicing.
##a=("s","k",99,'@@@',88,77)
##i=[]
##j=0
##k=-1
##while j<len(a):
##      i.append(a[k])
##      k-=1
##      j+=1
##a=tuple(i)
##print(a)

##19.wap to add two tuples.
##a=("s","k",99,'@@@',88,77)
##b=("b",88,'k',45,"ROHIT")
##a=a+b
##print(a)

##20.wap to remove the repeated values in tuple
##a=("s","k",99,'@@@',88,77)
##b=("b",88,'k',45,"ROHIT")
##a=a+b
##b=()
##i=0
##while i<len(a):
##     if a[i] not in(a[i+1::]):
##       b+=(a[i],)
##     i+=1
##print(b)
##print(a)

##21.wap to extract the repeated values in a tuple.
##a=("s","k",99,'@@@',88,77)
##b=("b",88,'k',45,"ROHIT")
##a=a+b
##b=()
##i=0
##while i<len(a):
##     if a[i] in(a[i+1::]):
##       b+=(a[i],)
##     i+=1
##print(b)
##print(a)

##22.wap to find the sum of the numbers present in a tuple.
##a=('s', 'k', 99, '@@@', 88, 77, 'b', 88, 'k', 45, 'ROHIT')
##i=0
##sum=0
##while i<len(a):
##     if isinstance(a[i],int):
##          sum+=a[i]
##     i+=1   
##print(sum)

##23.wap to find the sum of ascii values of numbers in a tuple.
##a=('s', 'k', 99, '@@@', 88, 77, 'b', 88, 'k', 45, 'ROHIT')
##i=0
##sum=0
##while i<len(a):
##     if isinstance(a[i],int):
##          sum+=int(ascii(a[i]))
##     i+=1   
##print((sum))

##24.wap to find the sum of the ascii values of special characters in a tuple.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'ROHIT','_')
##i=0
##sum=0
##while i<len(a):
##     if not isinstance(a[i],int):
##          if not('a'<=a[i]<='z' or 'A'<=a[i]<='Z'):
##              sum+=int(ord(a[i]))
##     i+=1
##print(sum)

##25.wap to print number of alphabets present in a tuple, if the sum of the ascii 
##values of alphabets is greater than sum of ascii value of numbers.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##sum=0
##cum=0
##while i<len(a):
##     if not isinstance(a[i],int):
##          if ('a'<=a[i]<='z' or 'A'<=a[i]<='Z'):
##              sum+=int(ord(a[i]))
##     elif isinstance(a[i],int):
##          cum+=a[i]
##     i+=1
##if sum>cum:
##     for n in a:
##          if not isinstance(n,int):
##            if ('a'<=n<='z' or 'A'<=n<='Z'):
##               print(n)

##26.wap to check whether the tuple is empty or not.
##a=()
##if not a:
##     print("empty")
##else :
##   print("has some thing")

##27.wap to check whether the tuple contains special characters or not.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##while i<len(a):
##     if not(isinstance(a[i],int) and ('a'<=a[i]<='z' or 'A'<=a[i]<='Z')):
##               print("Special char")
##     i+=1

##28.wap to check whether the tuple contains numeric value or not.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##while i<len(a):
##     if (isinstance(a[i],int) ):
##               print("Numeric")
##     i+=1
##29.wap to check whether the tuple contains alphabets or not.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##while i<len(a):
##     if ( ('a'<=a[i]<='z' or 'A'<=a[i]<='Z')):
##               print("Alphabet")
##     i+=1

##30.wap to print the ascii values of alphabets if the alphabet present in an even 
##index
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##j=0
##while i<len(a):
##     if i%2==0:
##       if not isinstance(a[i],int):
##         j+=ord(a[i])
##       else:
##        j+=a[i] 
##     i+=1
##print(j)

##31.wap to print the sum of the numbers in a tuple, if the number is present in odd 
##index.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'Rohit','_')
##i=0
##j=0
##while i<len(a):
##     if i%2!=0:
##       if isinstance(a[i],int):
##         j+=(a[i])
##     i+=1
##print(j)

##32.wap to extract all the ovels in a given tuple.
##a=('s', 'e', 99, '@', 88, 77, 'b', 88, 'k', 45, 'ROHIT','_')
##i=0
##j=""
##while i<len(a):
##   if isinstance(a[i],str):
##        for n in a[i]:
##           if n in "aeiouAEIOU":
##                j+=n
##   i+=1
##print(j)

##33.wap to extract all the consonants is a tuple.
##a=('s', 'e', 99, '@', 88, 77, 'b', 88, 'k', 45, 'ROHIT','_')
##i=0
##j=""
##k=''
##while i<len(a):
##   if isinstance(a[i],str):
##        for n in a[i]:
##           if n not in "aeiouAEIOU":
##                j+=n
##   i+=1
##print(j)


##34.wap to print the sum of all the ascii values of the alphabet if it is in even index 
##and if it is ovel.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##j=0
##while i<len(a):
##     if i%2==0:
##       if not isinstance(a[i],int)and ('a'<=a[i]<='z' or 'A'<=a[i]<='Z'):
##           if a[i] in "aeiouAEIOU":
##                j+=ord(a[i])
##     i+=1
##print(j)

##35.wap to check whether all the values in a tuple is singe value data type or not.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##while i<len(a):
##     if isinstance (a[i],int or float or bool):
##          print("single valued data type")
##     i+=1

##36.wap to check whether all the values in a tuple is multi value data type or not.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##while i<len(a):
##     if not isinstance (a[i],int or float or bool):
##          print("multi valued data type")
##     i+=1

##37.wap to check whether the tuple is homogeneous tuple or heterogeneous 
##tuple.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##j=True
##b=type(a[0])
##while i<len(a):
##     if b!=type(a[i+1]):
##          print("heterogeneous")
##          j=False
##          break
##     i+=1
##if j==True:
##     print("homo")

##38.wap to check whether the tuple is homogeneous or heterogeneous, if it is 
##homogeneous print the type of values in a tuple.
##a=( 99,88,77,88,45)
##i=0
##b=type(a[0])
##while i<len(a):
##     if b!=type(a[i+1]):
##          print("heterogeneous")
##          break
##     else:
##          print(type(a[i]))
##          print("homogeneous")
##     i+=1

##39.wap to extract all the single value datatype values in a tuple.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##j=()
##while i<len(a):
##     if isinstance (a[i],int or float or bool):
##          j+=(a[i],)
##     i+=1
##print(j)

##40.wap to extract all the multi value data type values in a tuple.
##a=('s', 'k', 99, 'i', 88, 77, 'o', 88, 'e', 45, 'R','_')
##i=0
##j=()
##while i<len(a):
##     if not isinstance (a[i],int or float or bool):
##          j+=(a[i],)
##     i+=1
##print(j)

##41.wap to extract all the ovel characters in a tuple.
##a=('s', 'e', 99, '@', 88, 77, 'b', 88, 'k', 45, 'ROHIT','_')
##i=0
##j=""
##while i<len(a):
##   if isinstance(a[i],str):
##        for n in a[i]:
##           if n in "aeiouAEIOU":
##                j+=n
##   i+=1
##print(j)


##42.wap to extract all the values in a tuple if it is in even indexing. 
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##j=()
##while i<len(a):
##     if i%2==0:
##       j+=(a[i],)
##     i+=1
##print(j)

##43.Wap to extract all the numbers if it is in odd index and if it is divisible by 5.
##a=('s', 'k', 99, '@', 88, 77, 'b', 88, 'k', 45, 'R','_')
##i=0
##j=()
##while i<len(a):
##     if i%2!=0 and i%5==0:
##       j+=(a[i],)
##     i+=1
##print(j)

##44.wap to extract all the happy numbers in a heterogeneous tuple.
##a=(13,6)
##i=0
##k=0
##j=0
##res=[]
##def happynum(p):
##    global k
##    global j
##    while p>0:
##        k+= (p%10)**2
##        p//=10
##    j=k
##    k=0
##    return p
##for n in a:
##    j=n
##    while j!=1:
##        happynum(j)
##    if j==1:
##        print("Happy num",n)
##    else:
##        print("Hauni modwara")
        

##45.wap to extract all the perfect numbers in a homogeneous tuple.
##a=(66,77,88,16,6)
##i=1
##k=1
##res=[]
##j=0
##pd=0
##for n in a:
##   while k<n:
##       if n%k==0:
##        res.append(k)
##       k+=1
##       pd=sum(res)       
##   print(res)
##   print(pd)
##   if pd==n:
##     print("perfect number")
##   else :
##    print("Not a perfect number")
##   k=1
##   res=[]
##   pd=0



##46.wap to extract all the Armstrong numbers in a tuple.
##a=(66,77,88,16,153)
##i=0
##j=0
##for n in a:
## temp=n
## temp2=n
## while(n>0):
##    i+=1
##    n//=10
## while(temp>0):
##    j+= (temp%10)**i
##    temp//=10
## if temp2==j:
##    print(j)
##    print(temp2)
##    print ("Amstrong number")
## else:
##    print(j)
##    print(temp2)
##    print("Not Amstrong")
## i=0
## j=0

##47.wap to check whether the character present in a tuple or not.
##a=("sanu",77,'Rohit sharma','@@')
##i=0
##while i<len(a):
##   if not isinstance(a[i],int):
##      for n in a[i]:
##         if "s" in n:
##            print("andar hai")
##   i+=1
   
      
##48.wap to check whether the character present in a tuple or not, if it is present 
##print the ascii value
##a=("sanu",77,'Rohit sharma','@@')
##i=0
##while i<len(a):
##   if not isinstance(a[i],int):
##      for n in a[i]:
##         if "s" in n:
##            print(ord(n))
##   i+=1
   
##49.wap to nest a tuple inside to another tuple.
##a=("sanu",77,'Rohit sharma','@@')
##a+=('c',"bbbb",90),
##print(a)

##50.wap to extract all the even index values in a tuple.
##a=("sanu",77,'Rohit sharma','@@',0)
##i=0
##k=()
##while i<len(a):
##   if i%2==0:
##      k+=a[i],
##   i+=1
##print(k)

##51.wap to extract all the odd index values in a tuple, if it is an integer datatype 
##and if it multiple of 3
##a=("sanu",77,'Rohit sharma',8,55,33,90,66)
##i=0
##k=()
##while i<len(a):
##    if i%2!=0:
##      if isinstance(a[i],int) and a[i]%3==0:
##          k+=a[i],
##    i+=1
##print(k)

##52.wap to extract all odd index values if it is mutable datatype.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##i=0
##k=()
##while i<len(a):
##    if i%2!=0:
##      if isinstance(a[i],list) or isinstance(a[i],set) or isinstance(a[i],dict) :
##          k+=a[i],
##    i+=1
##print(k)

##53.wap to extract all the values in a tuple separately, according to datatype.



##54.wap to count the number of words in a tuple if the value is a string.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##i=0
##count=0
##j=0
##num=[]
##while i<len(a):
##      if isinstance(a[i],str):
##          count=0
##          k=a[i]
##          while j<len(k):
##              if (k[j]==' ' and k[j+1]!=' ') or j== (len(k)-1):
##               count+=1   
##              j+=1
##          num.append(count)
##      j=0
##      i+=1
##      
##print(num)

##55.wap to extract all the odd index values using slicing.
##a=[11,98,7,67,54,9,85,23]
##b=[]
##b.append(a[1::2])
##print(b)

##56.wap to extract all the odd index values without using slicing.
##a=[11,98,7,67,54,9,85,23]
##i=0
##b=[]
##while i<len(a):
##    if i%2!=0:
##        b.append(a[i])
##    i+=1
##print(b)

##57.wap to concatenate all the string values in a given tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##i=0
##num=''
##while i<len(a):
##      if isinstance(a[i],str):
##          num+=a[i]
##      i+=1
##print(num)

##58.wap to print datatypes of all the values in a homogeneous tuple.
##a=(44,99,88,78,67,89,9)
##for  i in a:
##    print(type(i))

##59.wap to print datatypes of all the values in a heterogeneous tuple separately.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##for i in a:
##    print(type(i))

##60.wap to test if a variable is list or set or tuple.
##x=[77,99,00,99,8]
##if isinstance(x,list):
##   print("list")
##elif isinstance(x,tuple):
##    print("tuple")
##elif isinstance(x,set):
##    print("set")
    
##61.wap to sort a list of tuples by the second Item.









##62.wap to print the sum of tuple elements.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##sum=0
##for i in a:
##    if isinstance(i,int):
##        sum+=i
##print(sum)

##63.wap to Check if the given element is present in tuple or not.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##if 77 in a :
##    print ("present")

##64. W.A.P to check the second largest number given in the tuple?
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##b=[]
##for i in a:
##    if isinstance(i,int):
##        b.append(i)
##b.sort()
##print(b[-2])


##65.WAP TO Print the sum of all integer numbers in a tuple
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##sum=0
##for i in a:
##    if isinstance(i,int):
##        sum+=i
##print(sum)


##66.WAP TO Print the sum of even and odd numbers in a tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##sum=0
##mum=0
##for i in a:
##    if isinstance(i,int):
##       if i%2==0:
##           sum+=i
##       else:
##           mum+=i
##print(sum)
##print(mum)

##67.WAP TO Print the product of the all the even numbers in a tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',4)
##sum=1
##for i in a:
##    if isinstance(i,int):
##       if i%2==0:
##           sum*=i
##print(sum)

##68.WAP Check the collection is having middle value or not.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##if len(a)%2!=0:
##   print("middle")

##69.WAP to extract the middle value of the tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##if len(a)%2!=0:
##    print(a[((len(a))//2)])
    
##70.wap to Check whether given data is mutable or immutable in a tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh')
##i=0
##while i<len(a):
##    if i%2!=0:
##      if isinstance(a[i],list) or isinstance(a[i],set) or isinstance(a[i],dict) :
##          print(f"{a[i]} is mutable")
##    i+=1
    
##71. W.A.P to get the following output.
## i/p=(‘hai’, ‘hello’, ‘how’, ‘are’, ‘you’)
## o/p={‘hai’:[3,’ai’], ‘hello’:[5,’e’], ‘how’:[3,’o’], ‘are’:[3,’ae’], ‘you’:[3,’ou’]
##from collections import defaultdict
##a=('hai', 'hello', 'how', 'are', 'you')
##d=defaultdict()
##for k in a:
## j=''
## i=0
## while i<len(k):
##    if k[i] in 'aeiou':
##        j+=k[i]
##    i+=1
## d[k]=[len(k),j]
##print(d)

##72.wap to Count the number of complex data items present inside the tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',9+8j)
##for i in a:
##    if isinstance(i,complex):
##        print(i)

##73. Find the sum of even integer numbers if it is present in odd index and divisible by3.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##for i in (a[::2]):
##    if isinstance(i,int):
##        if i%2==0 and i%3==0:
##            print(i)
                    
##74. Split the given tuple collection of integer numbers into even & odd collection.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##b=()
##c=()
##for i in (a):
##    if isinstance(i,int):
##      if i%2==0:
##        b+=i,
##      else:
##          c+=i,
##print(b,c)

##75. Count number of string data items present in a tuple.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##sum=0
##for i in (a):
##    if isinstance(i,str):
##        sum+=1
##print(sum)

##76. W.A.P to get the following output.
## i/p= (‘hai’, ‘hello’, ‘how’, ‘are’, ‘you’)
## o/p= {‘hai’:3, ‘hello’:5, ‘how’:3, ‘are’:3, ‘you’:3}
##from collections import defaultdict
##a=('hai', 'hello', 'how', 'are', 'you')
##d=defaultdict()
##for k in a:
## d[k]=len(k)
##print(d)

##77. Print cube of all even numbers which are divisible by 4
##a=20
##x=[i**3 for i in range (a+1) if i%4==0]
##print(x)

##78. W.A.P to get the following output.
##i/p= [‘hai’,90,6.7, ’hello’,(8,9),’python’]
##o/p={(‘hai’,3),(‘hello’,5),(‘python’,6)}
##d=()
##a=['hai',90,6.7, 'hello',(8,9),'python']
##for i in (a):
##    if isinstance(i,str):
##         d+=(i,len(i)),
##print(set(d))

##79. Extract all the string data items present inside the given tuple only if it is 
##starting from ‘a’.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'abhiram','gfhfh',36,90,30,42,45,33,39,60)
##b=()
##for i in (a):
##    if isinstance(i,str):
##      if i[0]=='a':
##        b+=i,
##      
##print(b)

##80. Extract all the string data items from a given tuple only if it is at odd index & 
##length is greater than 3.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##b=()
##for i in (a[::2]):
##    if isinstance(i,str):
##      if len(i)>3:
##        b+=i,
##print(b)

##81. W.A.P to get the following output.
##i/p='PYTHon is Easy'
##o/p=('PYTHon2','is2','Easy3')
##p='PYTHon is Easy'.split()
##j=0
##sum=0
##k=()
##for i in p:
##    while j<len(i):
##          if 'a'<=(i[j])<='z':
##             sum+=1
##          j+=1
##    k+=(i+str(sum)),
##    sum=0
##    j=0
##print(k)

##82. W.A.P to get the following output.
##i/p=(2.3,18,71,’hai’,3+2j,{1,2},23)
##o/p=(2.3,9,8,3,3+2j,2,5)
##a=(2.3,18,71,'hai',3+2j,{1,2},23)
##b=()
##for i in a:
##    k=0
##    if isinstance(i,int):
##        while i>0:
##            k+=i%10
##            i//=10
##        b+=k,
##    elif isinstance(i,str) or isinstance(i,set):
##        b+=len(i),
##    else:
##        b+=i,
##print(b)

##83. W.A.P to get the following output.
##i/p=’abcd hai hello*’
##o/p=[‘abcd1’,’hello2’]
##a='abcd hai hello*'.split()
##a=a[::len(a)-1]
##i=0
##while i<len(a):
##    a[i]+=str(i+1)
##    i+=1
##print(a)


##84. Considering heterogeneous tuple find the sum of individual digits present 
##inside an integer number only if it is having more than 4 digits.
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],31398,9079807,'gfhfh',36,90,30,42118,45,33,39,60)
##b=()
##for i in (a):
##    sum=0
##    if isinstance(i,int) and i//10000>0:
##      while i>0:
##        sum+=i%10
##        i//=10
##      b+=sum,
##print(b)

##85. Extract all the string values present inside a tuple collection if it is present at 
##odd index & length of string is even (using functions).
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##def add():
## b=()
## for i in (a[::2]):
##     if isinstance(i,str):
##      if len(i)%2==0:
##        b+=i,
## print(b)
##add()


##86. W.A.P to get the following output (using functions).
##i/p= (12, ‘abcde’, ‘python’, 89, 4.5, ‘123’)
##o/p=((‘abcde’,5), (‘python’,6),(‘123’,3))
##a=(12, 'abcde', 'python', 89, 4.5, '123')
##b=()
##for i in (a):
##     if isinstance(i,str):
##        b+=(i,len(i)),
##print(b)

##87. W.A.P to get the following output.
##i/p=’hai hello python’
##o/p=((‘hai’,2,’a’), (‘hello’,2,’el’), (‘python’,1,’yhyn’))
##a='hai hello python'.split()
##b=()
##i=0
##while i<len(a):
##     count=0
##     j=''
##     for o in a[i]:
##         if o in 'aeiou':
##             count+=1
##             j+=o
##     b+=(a[i],count,j),
##     i+=1
##print(b)


##89. W.A.P to get the following output.
##i/p= ‘AbcD hAi Hello’
##o/p=((‘AbcD’,’bc’,2), (‘hAi’,’hi’,2), (‘Hello’,’ello’,4))
##p= 'AbcD hAi Hello'.split()
##i=0
##b=()
##while i<len(p):
##    k=''
##    for j in p[i]:
##        if 'a'<=j<='z':
##            k+=j
##    b+=(p[i],k,len(k)),
##    i+=1
##print(b)


##90. W.A.P to find the sum of factorial of all the integer numbers present inside the 
##tuple (using functions).
##a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
##def fact():
## b=()
## listt=[]
## for i in (a):
##     j=1
##     sum=0
##     if isinstance(i,int):
##      while j<i:
##        if i%j==0:
##          sum+=j
##        j+=1
##      listt.append(sum)
## print(listt)
##fact()

##91. Extract all the integer numbers which are divisible by 5 from the given tuple 
##by using recursion.
# a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
# b=[]
# def listt_num(tup,ind=0):
#     if ind== len(tup):
#         return
#     if isinstance (tup[ind],int) and tup[ind]%5==0:
#         b.append(tup[ind])
#     listt_num(tup,ind+1)
# listt_num(a)
# print(b)



##92. W.A.P to remove the duplicates from a tuple collection by using recursion 
##(without using typecasting).
# a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
# b=[]
# def listt_num(tup,ind=0):
#     if ind== len(tup):
#         return
#     if tup[ind] not in b :
#         b.append(tup[ind])
#     listt_num(tup,ind+1)
# listt_num(a)
# print(b)

##93. W.A.P to get the following output (using recursion).
##i/p=’python is very’
##o/p=((‘python’,’nohtyp’,6),(‘is’,’si’,2),(‘very’,’yrev’,4))
# a= 'python is very '.split()
# b=()

# def listt_num(tup,ind=0):
#     global b
#     if ind== len(tup):
#         return
#     b+=(tup[ind],(tup[ind])[::-1],len(tup[ind]))
#     listt_num(tup,ind+1)
    
# listt_num(a)
# print(b)


##94. Extract all the integer numbers present inside heterogonous tuple, print the 
##cube of all the values.
# a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60,3,4)
# lisst=[n**3 for n in a if isinstance(n,int)]
# print(lisst)

##95. Extract all the integer numbers present inside heterogonous tuple, if value is 
##more than 15 present at odd index.
# a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60)
# lisst=[p for n,p in enumerate(a) if (n%2!=0) ]
# print(lisst)

##96. Extract all the integer values present inside given heterogeneous list if it’s 
##value is b/w the range 15 -75, and the ASCII value of the number is divisible by 3.
# a=["sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60,7,8,9]
# listt=[n for n in a if (isinstance (n,int)) and n>-75 and n<=15 and ord(str(n))%3==0]
# print(listt)

##97.wap to print the sum of ASCII values of the integers present in the given tuple 
##if the value present in even index and if the ASCII value is odd.
# a=("sanu",77,'Rohit sharma',{9,0},55,[99,00,8],33,90,'gfhfh',36,90,30,42,45,33,39,60,9,7,6,4,3)
# sum=0
# for n,p in enumerate(a):
#     if n %2==0:
#         if isinstance(p,int) and p<9:
#              sum+=ord(str(p))
#              print(p)
# print(sum)

##98.wap to print the product of the indexing number if the indexing number 
##contains alphabets, and if the ASCII value of the character is multiple of 5 in a 
##given heterogeneous tuple.
# a=(1,"s",77,'R',8,'i',{9,0},55,[99,00,8],33,90,'g',36,90,30,42,45,33,39,60,9,7,6,4,3)
# prod=1
# for n,p in enumerate(a):
#     if isinstance(p,str) and ord(p)%5==0:
#         prod*=n
# print(prod)


##99.wap to print the second greatest number in a given homogeneous tuple.
# a=(77,55,33,90,36,90,30,42,45,33,39,60,9,7,6,4,3)
# c=()
# for n in a:
#     if n not in c:
#         c+=n,
# c=sorted(c)
# print(c[-2])


##100.wap to print the third smallest number in a given homogeneous tuple.
# a=(77,55,33,90,36,90,30,42,45,33,39,60,9,7,6,4,3)
# c=()
# for n in a:
#     if n not in c:
#         c+=n,
# c=sorted(c)
# print(c[2])

##101.wap to copy a tuple into another tuple by excluding the special characters 
# a=('j','i',9,'J','R','&','*',"#")
# b=()
# for m in a:
#  if  (isinstance (m,str)):
#     if 'a'<=m<='z' or  'A'<=m<='Z' :
#         b+=m,
#  else:
#      b+=m,       
# print(b)