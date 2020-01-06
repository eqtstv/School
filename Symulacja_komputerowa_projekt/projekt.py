import numpy as np

#   Parametry
# - ilosc przystanków
# - czasy wsiadania

# Wskaznik jakosci:
# Czas postoju na przystanku

#   TODO:
# - ustawianie sie w kolejke
# - wskaznik jakosci


class Stop:
    def __init__(self, no_ppl):
        self.no_ppl = abs(int(no_ppl))
        self.pending = []

    def add_pending(self, times):
        self.pending.extend(times)

class Bus:
    def __init__(self):
        self.passengers = []

    def enter_passengers(self, pending):
        self.passengers.extend(pending)
        return sum(pending)

    def exit_passengers(self, exiting):
        self.left = [self.passengers[i] for i in exiting if i<len(self.passengers)]

        for i in self.left:
            self.passengers.remove(i)

        return sum(self.left)

class Bus2:
    def __init__(self):
        self. passengers = []

    def enter_passengers(self, pending):
        self.passengers.extend(pending)
        self.entering1 = []
        self.entering2 = []

        for i in pending:
            if sum(self.entering1) > sum(self.entering2):
                self.entering2.append(i)
            else:
                self.entering1.append(i)

        return max(sum(self.entering1), sum(self.entering2))

    def exit_passengers(self, exiting):
        self.left = [self.passengers[i] for i in exiting if i<len(self.passengers)]
        self.exiting1 = []
        self.exiting2 = []

        for i in self.left:
            if sum(self.exiting1) > sum(self.exiting2):
                self.exiting2.append(i)
            else:
                self.exiting1.append(i)

        for i in self.left:
            self.passengers.remove(i)

        return max(sum(self.exiting1), sum(self.exiting2))


def time_on_stop(entering, exiting):
    return max(entering, exiting)


# tworzenie busa 1
bus1 = Bus()

# ----------------------------------------

# tworzenie przystankow

# stop1
stop1 = Stop(np.random.normal(5, 3))
stop1.add_pending([abs(np.random.normal(10, 5)) for ppl in range(stop1.no_ppl)])

# stop2
stop2 = Stop(2)
stop2.add_pending([5 for ppl in range(stop2.no_ppl)])
stop2exit = [1, 2]

# stop3
stop3 = Stop(np.random.normal(3, 2))
stop3.add_pending([np.random.uniform(5) for ppl in range(stop3.no_ppl)])

# ----------------------------------------

# wsiadanie i wysiadanie

# stop 1
et1 = bus1.enter_passengers(stop1.pending)
ex1 = 0
# stop 2
ex2 = bus1.exit_passengers([1, 2, 3])
et2 = bus1.enter_passengers(stop2.pending)
# stop 3
ex3 = bus1.exit_passengers([2])
et3 = bus1.enter_passengers(stop3.pending)


#print(time_on_stop(et1, ex1))
#print(time_on_stop(et2, ex2))
#print(time_on_stop(et3, ex3))

# -------------------------------------------------------------------

# tworzenie busa2
bus2 = Bus2()

# ----------------------------------------

# tworzenie przystankow

# stop1
stop1 = Stop(np.random.normal(5, 3))
stop1.add_pending([abs(np.random.normal(10, 5)) for ppl in range(stop1.no_ppl)])

# stop2
stop2 = Stop(2)
stop2.add_pending([5 for ppl in range(stop2.no_ppl)])
stop2exit = [1, 2]

# stop3
stop3 = Stop(np.random.normal(3, 2))
stop3.add_pending([np.random.uniform(5) for ppl in range(stop3.no_ppl)])

# ----------------------------------------

# wsiadanie i wysiadanie

# stop 1
et21 = bus2.enter_passengers(stop1.pending)
ex21 = 0
# stop 2
ex22 = bus2.exit_passengers([1, 2, 3])
et22 = bus2.enter_passengers(stop2.pending)
# stop 3
ex23 = bus2.exit_passengers([2])
et23 = bus2.enter_passengers(stop3.pending)

print(time_on_stop(et21, ex21))
print(time_on_stop(et22, ex22))
print(time_on_stop(et23, ex23))