import time
def compte(N):
    for i in range(N, -1, -1):
        print(i)
        time.sleep(1)
N = int(input("Saisissez en entier positif "))
if N < 0:
    print("Le nombre est négatif.")
else:
    compte(N)




#import time
#def compte-à-rebours(n):
   # while n >= 0:
   #     print(n)
    #    n -= 1
    #    time.sleep(1)
#n = int(input("Veuillez saisir un nombre entier positif : "))
#if n < 0:
 #   print("Veuillez saisir un nombre entier positif.")
#else:
 #   compte-à-rebours(n)
