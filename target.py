num=[2,4,3,5,6]
target=9
flag=0
for i in range(len(num)-1):
    if(flag==1):
        break
    for j in range(i+1, len (num)):
        if num[i]+num[j]==target:
            print(i,j)
            flag=1
            break

                
      

