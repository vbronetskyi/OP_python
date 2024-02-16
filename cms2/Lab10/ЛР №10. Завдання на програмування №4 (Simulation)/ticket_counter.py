"""
file: ticketcounter.py
"""
from random import random
from arrays import Array
from list_queue import Queue
from people import TicketAgent, Passenger

class TicketCounterSimulation:
    """TicketCounterSimulation"""
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)

        for i in range(numAgents) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """Run the simulation using the parameters supplied earlier."""
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def printResults(self):
        """Print the simulation results."""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed

        print("")
        print("Number of passengers served = ", numServed)
        print(f"Number of passengers remaining in line = {len(self._passengerQ)}")
        print(f"The average wait time was {avgWait:.2f} minutes.")
    def returnResults(self):
        """Returns the print statement. It is essential for tests, don't delete or modify it"""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed

        return(f"Number of passengers served = {numServed}\n"
            f"Number of passengers remaining in line = {len(self._passengerQ)}\n"
            f"The average wait time was {avgWait:.2f} minutes.")

    def _handleArrival(self, curTime):
        """_handleArrival"""
        if self._randomChance(self._arriveProb):
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(passenger)
            print("Passenger", passenger.idNum(), "arrived at time", curTime)

    def _handleBeginService(self, curTime):
        """_handleBeginService"""
        for agent in self._theAgents:
            if agent.isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.dequeue()
                waitTime = curTime - passenger.timeArrived()
                self._totalWaitTime += waitTime
                agent.startService(passenger, curTime + self._serviceTime)
                print("Agent", agent.idNum(), "started serving passenger",
                      passenger.idNum(), "at time", curTime,
                      "with a wait time of", waitTime, "minutes")

    def _handleEndService(self, curTime):
        """_handleEndService"""
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                print("Agent", agent.idNum(), "finished serving passenger",
                      passenger.idNum(), "at time", curTime)

    def _randomChance(self, prob):
        """_randomChance"""
        return random() < prob
