import sys
from funkcje.accountant import zapis_historii
from funkcje.accountant import stan_konta
from funkcje.accountant import stan_magazynu
from funkcje.accountant import Manager, manager, akcje

@manager.assign("zakup")
def zakup(manager):

    historia =manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    magazyn = dict()
    magazyn=stan_magazynu(magazyn)
    stan_salda=stan_konta()
    id_produktu = sys.argv[3]
    cena = int(sys.argv[4])
    l_kupionych = int(sys.argv[5])
    if cena < 0 or l_kupionych < 0:
        print("Nieprawidłowa cena lub liczba sztuk (ujemna)")
    elif stan_salda < cena*l_kupionych:
        print("Za mało pieniędzy na koncie,zakup niemozliwy")
    else:
        zakup = ("zakup", id_produktu, cena, l_kupionych)
        historia.append(zakup)
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
        for idx in range(len(historia)):
            b = historia[idx]
            if b[0] == akcje[0]:
                stan_salda += b[1]
            if b[0] == akcje[1]:
                stan_salda += b[2] * b[3]
            if b[0] == akcje[2]:
                stan_salda -= b[2] * b[3]
        zapis_historii(historia, sys.argv[2])

manager.execute("zakup")