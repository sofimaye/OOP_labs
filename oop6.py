"""поліморфізм та наслідування"""

class Train:
    def __init__(self, trainname, comfclass, passagers, totalbaggage, totalseats, coupes, seatsincoupe):
        self.trainname = trainname
        self.comfclass = comfclass
        self.passagers = passagers
        self.baggage = totalbaggage
        self.seats = totalseats
        self.coupes = coupes
        self.seatsincoupe = seatsincoupe

    def __str__(self):
        return str(self.passagers) #magic method

    def __repr__(self):

        return 'trainame:' + self.trainname + ' ' + 'comflass:' + str(self.comfclass)


class Minitrain(Train):

    def train(self):
        print('Minitrain')
        return self.trainname


train1 = Minitrain('AA01', 1, 35, 70, 35, 7, 5)
train2 = Minitrain('AA02', 5, 30, 60, 30, 6, 5)


class Highspeed(Train):
    def train(self):
        print('Highspeedtrain')
        return self.trainname


train3 = Highspeed('BB01', 2, 30, 60, 30, 6, 5)


class Coupetrain(Train):

    def train(self):
        print('Coupetrain')
        return self.trainname

train4 = Coupetrain('KC01', 4, 60, 120, 60, 15, 4)
train5 = Coupetrain('KC02', 3, 40, 80, 40, 10, 4)


trainslist = [train1, train2, train3, train4, train5]

baggage = []
for train in trainslist:
    baggage.append(train.baggage)

passagers = []
for passager in trainslist:
    passagers.append(passager.passagers)

def differentsum(Train):
    thesum=0
    for totalbag in Train:
        thesum = thesum + totalbag
    return thesum

print('Total sum of baggage in all trains: ', differentsum(baggage))
print('Total sum of passagers: ', differentsum(passagers))

print(trainslist)

start = int(input('Start:', ))
end = int(input('End:', ))

for train in trainslist:
    if start <= train.passagers <= end:
        print(train, train.train())


print('Trains sorted by class: ', sorted(trainslist, key=lambda train: train.comfclass))

print('Minitrain is subclass of train', issubclass(Minitrain, Train))

print(Minitrain.__bases__) #суперкласс возвр

print(train1.__dict__) #повертає всі атрибути
print(train1.__dict__['trainname'], train1.trainname)


