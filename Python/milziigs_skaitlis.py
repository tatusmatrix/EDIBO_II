#! /usr/bin/python3.6

print("Ievadiet skaitli")
# a=2**2000000

#te ir trīs darbības - vertības sagaidīšana, vērtības pārveidošana, piešķiršana
#argument = input()
#int(argument)
#a = int(argument)

#pildot int(input()) "bez izmēģinājuma", programma var vienkārši izlidot ...
#tāpēc, lai "nelidotu", mēs izmantosim try ... except ... finally konstrukciju
paziime = False
while (not paziime):
#while paziime==False:
#while paziime!=True:
    try:
        a = int( input() )
        paziime = True
    except:
        print("Diemžēl, cienījamais lietotāj, to, kas ievadīts, nevar",\
              "pārveidot par vesela tipa skaitli :-( ")
        print("Lūdzu, ievadi s_k_a_i_t_l_i vēlreiz")
'''
paziime = True
while paziime:
    try:
        a = int( input() )
        paziime = False
    except:
        print("Diemžēl, cienījamais lietotāj, to, kas ievadīts, nevar",\
              "pārveidot par vesela tipa skaitli :-( ")
        print("Lūdzu, ievadi s_k_a_i_t_l_i vēlreiz")
'''


#if (a == int): print("a**100")
#ja jau ļoti gribās, tad var salīdzinat type(a) == int -> rezultāts būs True
if (a == 5):
    print(a**100)
    print("Aprēķins ir gatavs")
print("Šis teksts atrodas ārpus darbību bloka - pierakstīts bez",\
      "atstarpēm priekšā, tāpēc tas parādīsies jebkurā gadījumā")
#    print("Atstarpes šeit vairs nedrīkst būt")

'''
print ("Ievadāmai vērtībai jābūt skaitlim")
b=a**100
'''
'''
aaa	bbb
aaaa	bbb
aaaaa	bbb
'''
