from Memento import *

class Collection:

    def __init__(self):
        self.collec = []

    def __str__(self):
        strng = ''
        for i in self.collec:
            strng += str(i) + '\n'
        return strng

    def get_collec(self):
        return self.collec

    def copy_collection(self):
        copy_collec = Collection()
        for i in self.collec:
            fid = ForeignID()
            for j in range(len(dictio)):
                fid.set(dictio[j], i.get(dictio[j]))
            copy_collec.add_to_collec(fid)
        return copy_collec.collec

    def add_to_collec(self, elem):
        self.collec.append(elem)

    def add_from_file(self, file):
        while True:
            fid = ForeignID()
            f = file.readline().strip('\n')
            if not f:
                break
            for i in range(len(dictio)):
                fid.set(dictio[i], f)
                f = file.readline().strip('\n')
            self.add_to_collec(fid)

    def add_to_file(self, file):
        for i in self.collec:
            for j in range(len(dictio)):
                file.write(i.get(dictio[j]))
                file.write('\n')
            file.write('\n')

    def delete_from_collec(self, iDn):
        del_em = []
        for i in self.collec:
            for j in range(len(dictio)):
                if i.get(dictio[j]) == iDn:
                    del_em.append(i)
                    break
        for k in del_em:
            self.collec.remove(k)

    def delete_from_file(self, file, iDn):
        self.delete_from_collec(iDn)
        self.add_to_file(file)

    def edit_collec(self, iDn, ed):
        for i in self.collec:
            for j in range(len(dictio)):
                if dictio[j] == iDn:
                    getattr(i, dictio1[j])(ed)


    def edit_file(self, file, iDn, ed):
        self.edit_collec(iDn, ed)
        self.add_to_file(file)

    def find_in_collec(self, string):
        tempo = Collection()
        for i in self.collec:
            for j in range(len(dictio)):
                if string == str(i.get(dictio[j]))[0:len(string)]:
                    tempo.add_to_collec(i)
        if tempo.get_collec() == []:
            return
        else:
            return tempo

    def sort_of_collec(self, atrb):
        self.collec = sorted(self.collec, key=lambda col: col.get(dictio[int(atrb)]).upper())

    def save(self):
        return Memento(self)

    def restore(self, mem = None):
        self.collec = mem.get_collection()
