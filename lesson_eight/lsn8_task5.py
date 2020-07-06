# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

from lsn8_task4 import *
from collections import Counter


class Storage:
    storage = []
    office = []
    type_eq = {'принтер': Printer, 'сканер': Scaner, 'ксерокс': Xerox}

    def get_equipment(self, type_eq: str):
        """Прием оборудования на склад"""
        try:
            self.storage.append(self.type_eq[type_eq.lower()]())
            return
        except:
            print('Данный тип оборудование храниться не на этом складе')

    def move_equipment(self, type_eq: str):
        """Перемещение оборудования со склада в офис"""
        for k, i in enumerate(self.storage):
            if i.__class__ == self.type_eq[type_eq.lower()]:
                self.office.append(self.storage.pop(k))
                return

    def revision_eq(self):
        ls = [type(i).__name__ for i in self.storage]
        lo = [type(i).__name__ for i in self.office]
        print('Склад', Counter(ls))
        print('Офис', Counter(lo))

# Продолжение в следующем задании
if __name__ == '__main__':
    a = Storage()
    a.get_equipment('принтер')
    a.get_equipment('принтер')
    a.get_equipment('принтер')
    a.get_equipment('сканер')
    print(a.storage)
    print(a.office)
    a.move_equipment('принтер')
    print(a.storage)
    print(a.office)
    a.revision_eq()

