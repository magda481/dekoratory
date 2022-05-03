import sys


class Manager:

    def __init__(self):
        self.actions = {}

    def odczyt_pliku(self, fd):
        with open(fd, 'r') as plik:
            dane_z_pliku = plik.read()
            dane = dane_z_pliku.split('\n')
            return dane

    def history(self, dane):
        lista = ["saldo", "sprzedaz", "zakup", "stop"]
        historia = []
        for idx in range(len(dane)):
            if dane[idx] == lista[0]:
                if dane[idx + 3] not in lista:
                    print('Błędna akcja, program przerywa pracę!')
                    break
                saldo = (dane[idx], int(dane[idx + 1]), (dane[idx + 2]))
                historia.append(saldo)
            elif dane[idx] == lista[1]:
                if dane[idx + 4] not in lista:
                    print('Błędna akcja, program przerywa pracę!')
                    break
                sprzedaz = (dane[idx], (dane[idx + 1]), int(dane[idx + 2]),
                            int(dane[idx + 3]))
                historia.append(sprzedaz)
            elif dane[idx] == lista[2]:
                if dane[idx + 4] not in lista:
                    print('Błędna akcja, program przerywa pracę!')
                    break
                zakup = (dane[idx], dane[idx + 1], int(dane[idx + 2]),
                         int(dane[idx + 3]))
                historia.append(zakup)
        return historia

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


manager = Manager()


def zapis_magazyn(plik_do_zapisu, magazyn):
    with open(plik_do_zapisu, 'w') as zapis:
        for k, v in magazyn.items():
            zapis.write("{}: {}".format(k, v))


def stan_magazynu(magazyn):
    akcje = ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad"]
    historia =manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    for i in range(len(historia)):  # magazyn
        b = historia[i]
        if b[0] == akcje[2]:
            if b[1] in magazyn:
                magazyn[b[1]] += b[3]
            else:
                magazyn = {b[1]: b[3]}
        if b[0] == akcje[1]:
            if b[1] in magazyn:
                magazyn[b[1]] -= b[3]
    return (magazyn)


def stan_konta():
    akcje = ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad"]
    historia = manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    stan_salda=0
    for i in range(len(historia)):  # stan salda
        b = historia[i]
        if b[0] == akcje[0]:
            stan_salda += b[1]
        if b[0] == akcje[1]:
            stan_salda += b[2] * b[3]
        if b[0] == akcje[2]:
            stan_salda -= b[2] * b[3]
    return stan_salda


def zapis_historii(historia,plik_do_zapisu):
    with open(plik_do_zapisu, "w") as zapis:
        for idx in range(len(historia)):
            b = historia[idx]
            for i in range(len(b)):
                zapis.write(str(b[i])+'\n')
        zapis.write("stop")





