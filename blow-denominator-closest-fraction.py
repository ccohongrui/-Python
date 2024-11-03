def f(num1,num2):
    import sys
    sys.setrecursionlimit(num1+1)
    calculation=[]
    dictionary={}
    def calculate(num1,num2):
        num1_Denominator=num1
        for index_0 in range(1,num1):
            calculator=(num1-1)/num1_Denominator
            calculation.append(calculator)
            dictionary[(num1-1)/num1_Denominator]=str((num1-1))+"/"+str(num1_Denominator)
            num1=num1-1
        num1=num1_Denominator-1
        if num1>1:
            calculate(num1,num2)
    calculate(num1,num2)
    no_repeat=list(set(calculation))
    no_repeat.sort()
    no_repeat.reverse()
    if num2==0:
        print("1/1")
    elif len(no_repeat)>=num2:
        print(dictionary[no_repeat[num2-1]])
    else:
        print(-1)
f(3,2)
