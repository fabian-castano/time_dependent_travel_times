


class MyNode:
    def __init__(self):
        self.ID_patient = None
        self.ID_node = None
        self.st_time = None
        self.serv_time = None
        self.type_serv = None
        self.in_neighbors = []
        self.out_neighbors = []

    def imprimir(self):
        print("Patient ID:", self.ID_patient)
        print("st time:", self.st_time)
        print("serv time:", self.serv_time)
        print("Follow:", self.in_neighbors)
        print("Coming:", self.out_neighbors)
        print("Node ID:", self.ID_node)

    def imprimirLineal(self):
        print(self.ID_patient, self.st_time / 3600, self.serv_time / 3600)