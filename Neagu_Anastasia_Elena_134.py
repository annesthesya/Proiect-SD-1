import time
import random

def generare_date_int(numar, lungime):
    global n
    n = random.randint(numar, numar * 10)
    return random.choices(range(lungime), k=n)

def sortat(L):
    if L == sorted(L):
        return True
    return False

def sortare_nativa(L):
    start = time.time()
    L = sorted(L)
    stop = time.time()
    print("Timp executie sortare nativa: ", time.time() - start, "s", sep="")
    return L

def sortare_partiala1(L):
    L = sorted(L[0:n // 4]) + L[n // 4:]
    return L


def sortare_partiala2(L):
    L = sorted(L[0:n // 2]) + L[n // 2:]
    return L


def sortare_partiala3(L):
    L = sorted(L[0:(n * 3) // 4]) + L[(n * 3) // 4:]
    return L


def sortare_partiala1r(L):
    L = sorted(L[0:n // 4], reverse=True) + L[n // 4:]
    return L


def sortare_partiala2r(L):
    L = sorted(L[0:n // 2], reverse=True) + L[n // 2:]
    return L


def sortare_partiala3r(L):
    L = sorted(L[0:(n * 3) // 4], reverse=True) + L[(n * 3) // 4:]
    return L

def BubbleSort(L):
    start = time.time()
    for i in range(len(L) - 1):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                m = L[j]
                L[j] = L[j + 1]
                L[j + 1] = m
    print("Timp executie BubbleSort: ", time.time() - start, "s", sep="")
    return L

def CountSort(L, ordin_date):
    start = time.time()
    count = [0 for x in range(ordin_date + 1)]

    for i in L:
        count[i] += 1

    n = len(L)
    L = [0 for x in range(n)]
    nrc = 0
    for i in range(len(count)):
        while count[i] != 0:
            L[nrc] = i
            nrc += 1
            count[i] -= 1
    print("Timp executie CountSort: ", time.time() - start, "s", sep="")
    return L

def RadixSortLSD(L, ordin_date):
    start = time.time()
    exp = 1
    while exp * 10 <= ordin_date:
        M = [[] for x in range(10)]
        for i in L:
            M[(i // exp) % 10].append(i)
        L = []
        for i in range(10):
            L.extend(M[i])
        exp *= 10
    print("Timp executie RadixSort LSD: ", time.time() - start, "s", sep="")
    return L

def merge(L, s, d, m):
    i = s
    j = m + 1
    M = []
    while i <= m and j <= d:
        if L[i] <= L[j]:
            M.append(L[i])
            i += 1
        else:
            M.append(L[j])
            j += 1
    if i <= m:
        M.extend(L[i:m + 1])

    if j <= d:
        M.extend(L[j:d + 1])

    L[s:d + 1] = M[:]

def MergeSort(L, s, d):
    if s < d:
        m = (s + d) // 2
        MergeSort(L, s, m)
        MergeSort(L, m + 1, d)
        merge(L, s, d, m)

def QuickSort(L):
    if len(L) <= 1:
        return L
    else:
        pivot = random.choice(L)
        S = [x for x in L if x < pivot]
        M = [x for x in L if x == pivot]
        D = [x for x in L if x > pivot]
        return QuickSort(S) + M + QuickSort(D)

print('==========- MENIU PRINCIPAL -==========')
y = int(input('''Alegeti tipul de vector: \n\t1. Citit de la tastatura; \n\t2. Aleator; \n\t3. Sortat ascendent 25%; 
\t4.Sortat ascendent 50%; \n\t5. Sortat ascendent 75%; \n\t6. Sortat ascendent; \n\t7. Sortat descendent 25%; 
\t8.Sortat descendent 50%; \n\t9. Sortat descendent 75%; \n\t10. Sortat descendent;\n'''))
if y==1:
    L = [int (l) for l in input("Inserati numerele din vector(numai spatii):\n").split()]
    n = len(L)
    ordin_date = 1
    while ordin_date <= max(L):
        ordin_date *= 10
elif y==2:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
elif y == 3:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala1(L)
elif y == 4:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala2(L)
elif y == 5:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala3(L)
elif y == 6:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sorted(L)
elif y == 7:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala1r(L)
elif y == 8:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala2r(L)
elif y == 9:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sortare_partiala3r(L)
elif y == 10:
    ordin_lungime = int(input("Inserati ordin lungime vector(100,1000 etc.):\n"))
    ordin_date = int(input("Inserati ordin date(100,1000 etc.):\n"))
    L = generare_date_int(ordin_lungime, ordin_date)
    L = sorted(L, reverse= True)
x = int(input('Alegeti metoda de sortare: \n\t1. Sortare individuala; \n\t2. Testati toate sortarile.\n'))
raspuns1 = 'd'
if (ordin_lungime >= 1000000):
    raspuns1 = input("===- ATENTIE -===\nAti selectat un ordin de lungime al vectorului care poate determina rularea  sa ia peste 10 minute. Continuati? d/n.")
if raspuns1 == 'd':
    if x == 1:
        z = int(input('''Alege sortarea: \n\t1. Sortarea nativa(TimSort); \n\t2. BubbleSort; \n\t3. CountSort; 
    4. RadixSortLSD; \n\t5. MergeSort; \n\t6. QuickSort.\n'''))
        if z == 1:
            M = sortare_nativa(L)
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")
        elif z == 2:
            raspuns2 = 'd'
            if ordin_lungime >= 10000:
                raspuns2 = input("===- ATENTIE -===\nAti selectat un ordin de lungime al vectorului care poate determina rularea sa ia peste 10 minute \nContinuati? d/n.")
            if raspuns2 == 'd':
                M = BubbleSort(L)
                if sortat(M) is True:
                    print("OK")
                else:
                    print("EROARE")
        elif z == 3:
            M = CountSort(L, ordin_date)
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")
        elif z == 4:
            M = RadixSortLSD(L, ordin_date)
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")
        elif z == 5:
            M = [x for x in L]
            start = time.time()
            MergeSort(M, 0, n - 1)
            stop = time.time()
            print("Timp executie MergeSort: ", time.time() - start, "s", sep="")
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")
        elif z == 6:
            start = time.time()
            M = QuickSort(L)
            stop = time.time()
            print("Timp executie QuickSort: ", time.time() - start, "s", sep="")
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")
    elif x == 2:
        M = sortare_nativa(L)
        if sortat(M) is True:
            print("OK")
        else:
            print("EROARE")
            raspuns3 = 'd'
        if ordin_lungime >= 10000:
            raspuns3 = input("===- ATENTIE -===\nAti selectat un ordin de lungime al vectorului care poate determina rularea algoritmului BubbleSort sa ia peste 10 minute \nContinuati? d/n.")
        if raspuns3 == 'd':
            M = BubbleSort(L)
            if sortat(M) is True:
                print("OK")
            else:
                print("EROARE")

        M = CountSort(L, ordin_date)
        if sortat(M) is True:
            print("OK")
        else:
            print("EROARE")

        M = RadixSortLSD(L, ordin_date)
        if sortat(M) is True:
            print("OK")
        else:
            print("EROARE")

        M = [x for x in L]
        start = time.time()
        MergeSort(M, 0, n - 1)
        stop = time.time()
        print("Timp executie MergeSort: ", time.time() - start, "s", sep="")
        if sortat(M) is True:
            print("OK")
        else:
            print("EROARE")
        start = time.time()
        M = QuickSort(L)
        stop = time.time()
        print("Timp executie QuickSort: ", time.time() - start, "s", sep="")
        if sortat(M) is True:
            print("OK")
        else:
            print("EROARE")
