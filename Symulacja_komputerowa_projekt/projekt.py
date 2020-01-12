import numpy as np
import random as rnd

#   Parametry
# - ilosc przystanków
# - czasy wsiadania

# Wskaznik jakosci:
# Czas postoju na przystanku

#   TODO:
# - ustawianie sie w kolejke
# - wskaznik 

# Notes:
# log norm
# kazdy test 3x minimum
# t srednia 0.3 i sprawdzac dochylenia 0.05:0.1
# wsiadanie wysiadanie rozklad lognorm
# czasy, wsiadajacy, wysiadajacy
# plan dwupoziomowy calkowity


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

        return sum(self.entering1), sum(self.entering2)

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

        return sum(self.exiting1), sum(self.exiting2)


def time_on_stop_Bus1(entering, exiting):
    return max(entering, exiting)

def time_on_stop_Bus2(q1et, q2et, q1ex, q2ex):
    return max(q1et + q1ex, q2et + q2ex)

def make_stops(no_stops, entering, times):
    """
    Args:
        no_stops (int): Number of stops.
        entering (avg, std_dev): Average and std_dev of people in every stop lognorm(avg, std_dev)
        times (avg, std_dev): Average and std_dev of move times for ppl lognorm(avg, std_dev)

    Returns:
        stops (list): List of Stop objects

    """
    stops = [Stop(np.random.lognormal(entering[0], entering[1])) for i in range(no_stops)]
    for stop in stops:
        stop.add_pending([np.random.lognormal(times[0], times[1]) for ppl in range(stop.no_ppl)])
    return stops

def make_trip(bus, stops, exiting):
    """
    Args:
        bus (object): Created bus object
        stops (list): List of stop objects
        exiting (avg, std_dev): Average and std_dev of ppl exiting on every stop

    Returns:
        stop_times (list): List of stop times on every stop

    """
    if type(bus) is Bus:
        stop_times = []
        for stop in stops:
            exiting_time = bus.exit_passengers(list(set(np.random.randint(len(bus.passengers)+1, size=int(np.random.lognormal(exiting[0], exiting[1]))))))
            entering_time = bus.enter_passengers(stop.pending)
            stop_times.append(time_on_stop_Bus1(entering_time, exiting_time))
        return stop_times

    elif type(bus) is Bus2:
        stop_times = []
        for stop in stops:
            q1ex, q2ex = bus.exit_passengers(list(set(np.random.randint(len(bus.passengers)+1, size=int(np.random.lognormal(exiting[0], exiting[1]))))))
            q1et, q2et = bus.enter_passengers(stop.pending)
            stop_times.append(time_on_stop_Bus2(q1et, q2et, q1ex, q2ex))
        return stop_times





bus1_times = []
bus2_times = []
for i in range(30):
    bus1 = Bus()
    bus2 = Bus2()
    stops = make_stops(3, (2, 0.1), (0.3, 0.1))
    stop_times1 = make_trip(bus2, stops, (1, 0.1))
    stop_times2 = make_trip(bus2, stops, (1, 0.1))
    bus1_times.append(sum(stop_times1)/len(stop_times1))
    bus2_times.append(sum(stop_times2)/len(stop_times2))

avg_bus1 = sum(bus1_times)/len(bus1_times)
avg_bus2 = sum(bus2_times)/len(bus2_times)

print(avg_bus1)
print(avg_bus2)
