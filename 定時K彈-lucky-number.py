P=N=int(input("定時K彈人數"))
M=int(input("定時K彈第幾人爆炸"))
K=int(input("定時K彈爆炸幾次"))
i=0
M_bigger=M%N
N_list=[i for i in range(1,N+1)]
for index_bomb in range(1,K+1):
    N_list[M_bigger-1]=0
    M_bigger=M_bigger+M
    i=i+1
    if i<K: 
        if M_bigger//N!=0:
            if N//M==0:
                for index_remove in range(1):
                    N_list.remove(0)
                if M_bigger==M:
                    N=N-1
                    M_bigger=M_bigger%N
                else:
                    M_bigger=M_bigger-N
                    N=N-1
                    M_bigger=M_bigger%N
            else:
                for index_remove_a in range(N//M):
                    N_list.remove(0)
                M_bigger=M_bigger%N
                N=N-(N//M)
if P>M*K:
    print(N_list[M*K])
elif N_list[-1]!=0:
    print(N_list[M_bigger-M])
elif N_list[-1]==0:
    print(N_list[0])