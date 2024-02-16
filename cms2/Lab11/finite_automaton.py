"""Lab_3.finite_automaton"""
import random

class State:
    """Determination of possible states of the finite automaton"""
    SLEEP = "Sleep"
    EAT = "Eat"
    WORK = "Work"
    RELAX = "Relax"
    PLAY = "Play"

class FiniteStateMachine:
    """A class that implements a finite automaton"""
    def __init__(self):
        """Constructor"""
        self.state = State.SLEEP

    def run(self):
        """
        The run method simulates a day in the life using a finite state machine.
        Each hour is checked for current status and transitions are made
        into new states depending on conditions and random events.
        """

        for hour in range(24):
            if self.state == State.SLEEP:
                # Перехід до стану EAT за випадкової події та о 7:00 годині
                if random.random() > 0.5 and hour == 7:
                    print("Ah..., good new day")
                    self.state = State.EAT
                # Перехід до стану RELAX о 8:00 годині
                elif hour == 8:
                    print("Oh god not, I did not wake up in time again..")
                    self.state = State.RELAX
                else:
                    print("Zzzz.....")
            elif self.state == State.EAT:
                # Перехід до стану WORK о 9:00 годині
                if hour == 9:
                    print("Good... breakfast was nice, now it is time to work")
                    self.state = State.WORK
            elif self.state == State.WORK:
                # Перехід до стану RELAX за випадкової події та о 14:00 годині
                if random.random() > 0.8 and hour == 14:
                    print("I need a break, time to relax")
                    self.state = State.RELAX
                # Перехід до стану PLAY о 18:00 годині
                elif hour == 18:
                    print("Work is done, time to play")
                    self.state = State.PLAY
            elif self.state == State.RELAX:
                # Перехід до стану WORK о 19:00 годині
                if hour == 19:
                    print("Relaxation time is over, back to work")
                    self.state = State.WORK
            elif self.state == State.PLAY:
                # Перехід до стану SLEEP за випадкової події та о 22:00 годині
                if random.random() > 0.6 and hour == 22:
                    print("Tired, time to sleep")
                    self.state = State.SLEEP

fsm = FiniteStateMachine()
fsm.run()
