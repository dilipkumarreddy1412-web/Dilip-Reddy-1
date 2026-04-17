def fibonacci_iterative(n_terms):
    n1,n2=0,1
    count=0
    if n_terms<=0:
        print("please enter a positive integer")
    elif n_terms==1:
        print(n1)
    else:
        print("fibonacci sequence:")
        while count<n_terms:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
fibonacci_iterative(7)
        
