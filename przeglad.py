import sys
from funkcje.accountant import Manager, manager


@manager.assign("przeglad")
def przeglad(manager):

    historia = manager.history(dane=manager.odczyt_pliku(fd=sys.argv[1]))
    lsp = int(sys.argv[3])
    psp = int(sys.argv[4])+1

    with open(sys.argv[2], "w") as zapis:
        for idx in range(lsp, psp):
            b = historia[idx]
            for i in range(len(b)):
                zapis.write(str(b[i]) + '\n')
        zapis.write("stop")

manager.execute("przeglad")