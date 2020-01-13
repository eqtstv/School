import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


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

class BusOneWay:
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

class BusTwoWays:
    def __init__(self):
        self. passengers = []

    def enter_passengers(self, pending):
        self.passengers.extend(pending)
        self.entering1 = []
        self.entering2 = []

        for i in pending:
            if len(self.entering1) > len(self.entering2):
                self.entering2.append(i)
            else:
                self.entering1.append(i)

        return sum(self.entering1), sum(self.entering2)

    def exit_passengers(self, exiting):
        self.left = [self.passengers[i] for i in exiting if i<len(self.passengers)]
        self.exiting1 = []
        self.exiting2 = []

        for i in self.left:
            if len(self.exiting1) > len(self.exiting2):
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
    if type(bus) is BusOneWay:
        stop_times = []
        for stop in stops:
            exiting_time = bus.exit_passengers(list(set(np.random.randint(len(bus.passengers)+1, size=int(np.random.lognormal(exiting[0], exiting[1]))))))
            entering_time = bus.enter_passengers(stop.pending)
            stop_times.append(time_on_stop_Bus1(entering_time, exiting_time))
        return stop_times

    elif type(bus) is BusTwoWays:
        stop_times = []
        for stop in stops:
            q1ex, q2ex = bus.exit_passengers(list(set(np.random.randint(len(bus.passengers)+1, size=int(np.random.lognormal(exiting[0], exiting[1]))))))
            q1et, q2et = bus.enter_passengers(stop.pending)
            stop_times.append(time_on_stop_Bus2(q1et, q2et, q1ex, q2ex))
        return stop_times

def test_buses(no_times, no_stops, entering, times, exiting):
    """
    Args:
        no_times (int): Ilosc przeprowadzanych testow
        no_stops (int): Ilosc przystankow
        entering (avg, std_dev): Srednia i odcylenie dla ilosci wsiadajacych na przystanku
        times (avg, std_dev): Srednia i odchylenie standardowe czasow wsiadania i wysiadania
        exiting (avg, std_dev): Srednia i odcylenie dla ilosci wysiadajacych na przystanku

    Returns:
        bus1_times (list): Lista srednich dla Autobusu z jednym wej i jednym wyj
        bus2_times (list): Lista srednich dla Autobusu z dwoma wej/wyj
    """

    bus1_times = []
    bus2_times = []
    for i in range(no_times):
        bus1 = BusOneWay()
        bus2 = BusTwoWays()
        stops = make_stops(no_stops, (entering[0], entering[1]), (times[0], times[1]))
        stop_times1 = make_trip(bus1, stops, (exiting[0], exiting[1]))
        stop_times2 = make_trip(bus2, stops, (exiting[0], exiting[1]))
        bus1_times.append(sum(stop_times1)/len(stop_times1))
        bus2_times.append(sum(stop_times2)/len(stop_times2))
    return bus1_times, bus2_times

def get_avg(times):
    avg = sum(times)/len(times)
    return avg

def plot_graphs(no_times, bus1_times, bus2_times):
    t = np.arange(no_times)
    plt.figure()
    plt.scatter(t, bus1_times, label="Bus One Way")
    plt.scatter(t, bus2_times, label="Bus Two Ways")
    plt.legend(loc="lower right")

    plt.figure()
    sns.distplot(bus1_times, label="Bus One Way")
    sns.distplot(bus2_times, label="Bus Two Ways")
    plt.legend(loc="lower right")

    plt.figure()
    sns.scatterplot(bus1_times, bus2_times)
    sns.scatterplot(bus2_times, bus1_times)

    plt.figure()
    data = [bus1_times, bus2_times]
    sns.boxplot(data=data)
    plt.show()

def plot_graphs_all(no_times, bus1_times, bus2_times):
    f, axs = plt.subplots(2, 2)
    t = np.arange(no_times)
    
    axs[0, 0].scatter(t, bus1_times, label="Bus One Way")
    axs[0, 0].scatter(t, bus2_times, label="Bus Two Ways")
    axs[0, 0].legend(loc="lower right")
    
    sns.distplot(bus1_times, label="Bus One Way", ax=axs[0, 1])
    sns.distplot(bus2_times, label="Bus Two Ways", ax=axs[0, 1])
    axs[0, 1].legend(loc="lower right")
    
    sns.scatterplot(bus1_times, bus2_times, ax=axs[1, 0])
    sns.scatterplot(bus2_times, bus1_times, ax=axs[1, 0])
    
    data = [bus1_times, bus2_times]
    sns.boxplot(data=data, ax=axs[1, 1])
    plt.show()




t1_bus1_times, t1_bus2_times = test_buses(30, 3, (3, 0.1), (0.3, 0.1), (2, 0.1))
t2_bus1_times, t2_bus2_times = test_buses(30, 3, (3, 0.1), (0.3, 0.05), (2, 0.1))

t1_avg_bus1 = get_avg(t1_bus1_times)
t1_avg_bus2 = get_avg(t1_bus2_times)

t2_avg_bus1 = get_avg(t2_bus1_times)
t2_avg_bus2 = get_avg(t2_bus2_times)

print(t1_avg_bus1, t1_avg_bus2)
print(t2_avg_bus1, t2_avg_bus2)

#plot_graphs_all(30, t1_bus1_times, t1_bus2_times)
plot_graphs_all(30, t2_bus1_times, t2_bus2_times)
