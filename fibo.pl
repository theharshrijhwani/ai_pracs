fibo(0,0).
fibo(1,1).
fibo(F,N):- N>1, N1 is N-1, N2 is N-2, fibo(F1, N1), fibo(F2, N2), F is F1+F2.