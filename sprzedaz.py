from funkcje.accountant import zapis_historii
from funkcje.accountant import stan_konta
from funkcje.accountant import stan_magazynu
from funkcje.accountant import Manager, manager, akcje
import sys

@manager.assign("sprzedaz")
def sprzedaz(manager):

    historia = manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    magazyn = dict()
    magazyn = stan_magazynu(magazyn)
    stan_salda=stan_konta()
    id_produktu = sys.argv[3]
    cena = int(sys.argv[4])
    l_sprzedanych = int(sys.argv[5])
    if cena < 0 or l_sprzedanych < 0:
        print("Nieprawidłowa cena lub ilośc produktu (ujemne)")
    elif id_produktu in magazyn and l_sprzedanych <= magazyn[id_produktu]:
        sprzedaz = ('sprzedaz', id_produktu, cena, l_sprzedanych)
        historia.append(sprzedaz)
        for idx in range(len(historia)):
            b = historia[idx]
            if b[0] == akcje[0]:
                stan_salda += b[1]
            if b[0] == akcje[1]:
                stan_salda += b[2]*b[3]
            if b[0] == akcje[2]:
                stan_salda -= b[2] * b[3]
        for idx in range(len(historia)):
            b = historia[idx]
            if b[0] == akcje[2]:
                if b[1] in magazyn:
                    magazyn[b[1]] += b[3]
                else:
                    magazyn = {b[1]: b[3]}
            if b[0] == akcje[1]:
                if b[1] in magazyn:
                    magazyn[b[1]] -= b[3]
        zapis_historii(historia, sys.argv[2])
    else:
        print('Nie ma na tyle produktu do sprzedaży')

manager.execute("sprzedaz")