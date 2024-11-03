num=input("輸入你的數字") 
odd=num[0::2]
odd_new=odd[0:-1]
even=num[1::2]
even_new=even[0:-1]
I=0
i=0
index_odd=int(odd[0])
index_even=int(even[0])
if int(num)<10:
    print(int(num))
else:
    for index in odd_new:
        index_odd=index_odd+int(odd[I+1])
        I=I+1
    for index in even_new:
        index_even=index_even+int(even[i+1])
        i=i+1
    print(abs(index_even-index_odd))
