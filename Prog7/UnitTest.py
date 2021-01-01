import unittest
from Collection import *


class TestCase(unittest.TestCase):
    def setUp(self):
        self.cl = Collection()
        self.fid = ForeignID('16256496', 'ukr', 'AS123456', 'Andriy', 'Sokulskiy',
                             '2000-01-20', '2016-01-31', '2026-02-01')
        self.fid2 = ForeignID('48624563', 'pol', 'NK265485', 'Mykola', 'Kotsan',
                         '2000-09-27', '2014-10-07', '2024-10-28')
        self.fid3 = ForeignID('63245125', 'ukr', 'YT987456', 'Yurthik', 'Tyhonlyi',
                         '2000-06-06', '2018-01-20', '2028-01-21')
        self.fids = [self.fid, self.fid2, self.fid3]


    def adding(self, int):
        for i in range(len(self.fids)):
            if i < int:
                self.cl.add_to_collec(self.fids[i])


    def test_add_to_collec(self):
        self.adding(1)

        self.assertIn(self.fid, self.cl.get_collec())


    def test_add_from_file(self):
        file = open("TestFile.txt", "r")
        self.cl.add_from_file(file)
        file.close()

        for j in range(len(self.cl.get_collec())):
            for i in range(len(dictio)):
                self.assertEqual(self.fids[j].get(dictio[i]), self.cl.get_collec()[j].get(dictio[i]))


    def test_add_to_file(self):
        self.adding(3)
        cl1 = Collection()

        file = open("TestFile.txt", "w")
        self.cl.add_to_file(file)
        file.close()

        file = open("TestFile.txt", "r")
        cl1.add_from_file(file)
        file.close()

        for j in range(len(cl1.get_collec())):
            for i in range(len(dictio)):
                self.assertEqual(self.fids[j].get(dictio[i]), cl1.get_collec()[j].get(dictio[i]))


    def test_delete_from_collec(self):
        self.adding(3)

        self.cl.delete_from_collec('pol')

        self.assertEqual(len(self.cl.get_collec()), 2)
        for j in range(len(self.cl.get_collec())):
            if self.fids[j].get('country_code') != 'pol':
                for i in range(len(dictio)):
                    self.assertEqual(self.fids[j].get(dictio[i]), self.cl.get_collec()[j].get(dictio[i]))


    # delete_from_file використовує: delete_from_collec та add_to_file, які вже протестовані


    def test_edit_collec(self):
        self.adding(2)

        self.cl.edit_collec('country_code', 'isr', '16256496')

        self.assertEqual('isr', self.cl.get_collec()[0].get(dictio[1]))


    # edit_from_file використовує: edit_from_collec та add_to_file, які вже протестовані


    def test_backup(self):
        MeM = Caretaker(self.cl)
        self.adding(3)
        MeM.backup()
        for j in range(len(self.cl.get_collec())):
            for i in range(len(dictio)):
                self.assertEqual((MeM._mementos[MeM.last_pos]).get_collection()[j].get(dictio[1]), self.cl.get_collec()[j].get(dictio[1]))


    def test_undo_redo(self):
        MeM = Caretaker(self.cl)
        self.adding(3)
        cl1 = self.cl.copy_collection()

        cl1.append(self.fid)
        for i in range(6): #повертає до 5 дій
            self.cl.add_to_collec(self.fid)
            MeM.backup()
        for i in range(6):
            MeM.undo()

        for j in range(len(self.cl.get_collec())):
            for i in range(len(dictio)):
                self.assertEqual(cl1[j].get(dictio[i]), self.cl.get_collec()[j].get(dictio[i]))

        for i in range(6):
            cl1.append(self.fid)
        for i in range(6):
            MeM.redo()

        for j in range(len(self.cl.get_collec())):
            for i in range(len(dictio)):
                self.assertEqual(cl1[j].get(dictio[i]), self.cl.get_collec()[j].get(dictio[i]))


if __name__ == '__main__':
    unittest.main()
