import sys
from funkcje.accountant import zapis_historii
from funkcje.accountant import Manager, manager

@manager.assign("saldo")
def saldo(manager):
    historia = manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    x = sys.argv[3]
    y = sys.argv[4]
    saldo = ("saldo", int(x), y)
    historia.append(saldo)
    zapis_historii(historia, sys.argv[2])


manager.execute("saldo")