from funkcje.accountant import stan_magazynu, zapis_magazyn
import sys
from funkcje.accountant import Manager, manager



@manager.assign("magazyn")
def magazyn(manager):
    magazyn = dict()
    magazyn= stan_magazynu(magazyn)
    zapis_magazyn(sys.argv[2], magazyn)

manager.execute("magazyn")