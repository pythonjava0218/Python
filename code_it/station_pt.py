def __init__(self, name):
    self.name = name
    self.neighbors = []
    
    
def add_connection(self, another_station):
    self.neighbors.append(another_station)
    another_station.neighbors.append(self)


r_file = open('stations.txt', 'r', encoding = 'utf-8')

for file in r_file:
    station = file.strip().split(" - ")
    print(station)

r_file.close()
