import sys
from funkcje.accountant import stan_konta
from funkcje.accountant import Manager, manager

@manager.assign("konto")
def konto(manager):
        konto = str(stan_konta())
        with open(sys.argv[2], 'w') as zapis:
                zapis.write(konto)


manager.execute("konto")