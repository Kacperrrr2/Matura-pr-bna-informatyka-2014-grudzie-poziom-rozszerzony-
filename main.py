wiersze=open('slowa.txt','r')
tab=["100010000100",
"001",
"000",
"10101001110000",
"000011"]
# for wiersz in wiersze:
#     tab.append(wiersz.strip())

#ZADANIE 4.1
# liczbazer=0
# liczbajedynek=0
# tabLiczbaZerWiekszaOdLiczbyJedynek=[]
# for i in tab:
#     for j in i:
#         if j=='1':
#             liczbajedynek+=1
#         if j=='0':
#             liczbazer+=1
#     if liczbajedynek<liczbazer:
#         tabLiczbaZerWiekszaOdLiczbyJedynek.append(i)
#     liczbazer=0
#     liczbajedynek=0
#
#
# print(tabLiczbaZerWiekszaOdLiczbyJedynek)

# ZAD4.2
# liczbazer=0
# liczbajedynek=0
# tabLiczbaZerWiekszaOdLiczbyJedynek=[]
# for i in tab:
#     for j in range(len(i)-1):
#         if i[j]!=i[j+1]:
#             liczbazer+=1
#     if liczbazer==1:
#         tabLiczbaZerWiekszaOdLiczbyJedynek.append(i)
#     liczbazer=0
# print(tabLiczbaZerWiekszaOdLiczbyJedynek)

#ZAD4.3
# liczbazer=0
# liczbajedynek=0
# maks=0
# tabLiczbaZerWiekszaOdLiczbyJedynek=[]
# wynik=[]
# for i in tab:
#     for j in range(len(i)):
#         if i[j]=="0":
#             liczbazer+=1
#         if i[j]=="1":
#             liczbazer=0
#         if liczbazer > maks:
#             maks = liczbazer
#     liczbazer=0
# for i in tab:
#     for j in range(len(i)):
#         if i[j] == "0":
#             liczbazer += 1
#         if i[j] == "1":
#             liczbazer = 0
#         if liczbazer == maks:
#             wynik.append(i)
#     liczbazer=0
# print(wynik)

