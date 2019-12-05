class Virus:
    '''Represents the virus that will be used to infect people in the
        simulation'''

    def __init__(self, name, reproduction_num, mortality_num):
        '''Sets up the virus to include the name of the virus, the reproduction
        number that controls how infectious it is, and the mortality rate or
        how deadly it is'''
        self.name = name  # string
        self.reproduction_num = reproduction_num
        # float number between 0.0 and 1.0
        self.mortality_num = mortality_num
        # a float number between 0.0 and 1.0

    def did_survive_infection(self):
        pass

    def print_population(self):
        '''prints out each person in the population'''
        pass

    def get_infected(self):
        '''returns a list of all the infected people in the population'''
        pass

    def simulation_should_continue(self):
        '''determines whether the simulation should continue based on the
        state of the population'''
        pass

    def determine_survival(self):
        '''checks if each of the current infected died or survived and became
        vaccinated, occurs after each time step'''
        pass

    def time_step(self):
        '''call interactions between an infected person and a random person
        from the population'''
        pass

    def interaction(self):
        '''random person may become infected or vaccinated'''
        pass
