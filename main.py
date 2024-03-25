wiersze=open('dziennik.txt','r')
tab=[]
for wiersz in wiersze:
    tab.append(int(wiersz.strip()))
# ZAD5.1
# licznik=0
# ilosc_liczb_wiekszych=0
# for i in range(len(tab)-1):
#     if tab[i+1]>tab[i]:
#         licznik+=1
#     else:
#         licznik=0
#     if licznik==2:
#         ilosc_liczb_wiekszych+=1
#
# print(ilosc_liczb_wiekszych)
# ZAD5.2
#
# min=tab[0]
# max=tab[0]
#
# for i in range(1,len(tab)):
#     if tab[i]>max:
#         max=tab[i]
#     if min>tab[i]:
#         min=tab[i]
# print(str(min)+ "  "+ str(max))
# ZAD5.3
# licznik_max=0
# licznik=0
# ilosc_liczb_wiekszych=0
# poczatkowa_serii=0
# roznica=0
# for i in range(len(tab)-1):
#     if tab[i+1]>tab[i]:
#         licznik+=1
#         if licznik==1:
#             poczatkowa_serii=tab[i]
#     else:
#         max_serii=tab[i]
#         if licznik > licznik_max:
#             licznik_max = licznik
#             roznica=max_serii-poczatkowa_serii
#         licznik=0
#         poczatkowa_serii=0
# print(str(licznik_max)+ "    "+str(roznica)+"    ")
