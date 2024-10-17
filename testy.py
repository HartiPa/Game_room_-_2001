# 1; 2; 3; 4; 5; 6; 7; 8; 9;
#for i in range (10):
#    print(i, end="; ")

#print()
#print("*" * 40)
# 5; 6; 7; 8;
#for i in range (5,9):
#    print(i, end=" - ")

#print()
#print("*" * 40)
#for i in range(1,10,2):
#    print(i, end=" | ")

#print()
#print("*" * 40)
#def num(n):
#    for i in range(1, n + 1):
#        print(i, end=" dále ")
#    print()
#num(5)
#num(11)

#print("*" * 40)

#def sud_num(n):
#    for i in range(1, n + 1):
#        if i % 2 == 0:
#            print(i,end="_;_")
#        print()
#sud_num(20)

#print("*" * 40)

#def powers(base, n):
#    for i in range(1, n + 1):
#        num = base ** i
#        print(num, end="; ")
#    print()

#powers(2, 10)

#print("*" * 40)

#def divisors(n):
#    for i in range(1, n + 1):
#        if n % i == 0:
#            print(i, end=",")
#    print()

#divisors(14)

#print("*" * 40)
#def subsequences(n):
#    numbers = []
#    for i in range(1, n + 1):
#        numbers.append(i)
#        print(numbers, end=" ")
#    print()

#subsequences(10)
#print("*" * 40)

#def alternating(n):
#    n_positive = 0
#    n_negative = 0
#    for i in range(1, n):
#        print(f"{i}  -{i}")

#alternating(8)

#def table_products(n):
#    for radek in range(1, n+1):
#        seznam = ""
#        for nasobilka in range(1, n+1):
#            seznam += str(radek * nasobilka) + ";"
#        print(f"{radek} | {seznam}")

#table_products(5)

#def table_powers(n):
#    for radek in range(1, n + 1):
#        seznam = ""
#        for nasobilka in range(1, n+1):
#            seznam += str(radek ** nasobilka) + ";"
#        print(f"{radek} | {seznam}")

#table_powers(5)

#def table_additions(n):
#    for radek in range(1, n + 1):
#        seznam = ""
#        for nasobilka in range(1, n+1):
#            seznam += str(radek + nasobilka) + ";"
#        print(f"{radek} | {seznam}")

#table_additions(5)

#def table_maxs(n):
#    for i in range(1, n+1):
#        seznam = ""
#        for j in range(1, n+1 ):
#            if j < i:
#                seznam += str(i) + " "
#            else:
#                seznam += str(j) + " "
#        print(f"{i} | {seznam}")

#table_maxs(2)

# ČTVEREC
#def square(x):
#    for i in range(x):
#        print("# " * x)

#square(7)

# PRÁZDNÝ ČTVEREC
#def empty_square(n):
#    print("# "*n)
#    for i in range(n):
#        print("# " + ". " * (n - 2) + "#")
#    print("# " * n)

#empty_square(5)

# PIRAMIDA
#def piramid(n):
#    omezeni = n -1
#    k = 1
#    for i in range(n):
#        space = (n-omezeni)
#        j = "# "
#        print((". " * omezeni) + (k * j) + (". " * omezeni))
#        omezeni -= 1
#        k += 2

#piramid(10)

#def chessboard(n):
#    c1 = "x . "
#    c2 = ". # "
#    x = n // 2
#    if n % 2 == 0:
#        for i in range(x):
#            print(c1 * x)
#            print(c2 * x)
#    else:
#        num = int(n/2)
#        print(num)

#chessboard(7)

#def series_sum(n):
#    total = 0
#    for i in range(1,n+1):
#    total += i
#    return total

#print(series_sum(1))
#print(series_sum(5))
#print(series_sum(10))
#print(series_sum(1000))

