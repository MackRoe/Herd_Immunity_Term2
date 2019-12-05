# Herd Immunity Simulation

A basic simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against this virus.

*This is the Final Project for CS1.1*

## Goals

- A sick person only has a chance at infecting healthy, unvaccinated people they encounter.
- An infected person cannot infect a vaccinated person. This still counts as an interaction.
- An infected person cannot infect someone that is already infected. This still counts as an interaction.
- At the end of a time step, an infected person will either die of the infection or get better. The chance they will die is the percentage chance stored in mortality_rate.
- For simplicity's sake, if the person does not die, we will consider them immune to the virus and change is_vaccinated to True when this happens.
- Dead people can no longer be infected, either. Any time an individual dies, we should also change their .infected attribute to False.
- All state changes for a person should occur at the end of a time step, after all infected persons have finished all of their interactions.
- During the interactions, make note of any new individuals infected on this turn. After the interactions are over, we will change the .infected attribute of all newly infected individuals to True.
- Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.
- The simulation should output a logfile that contains a record of every interaction that occurred during the simulation. We will use this logfile to determine final statistics and answer questions about the simulation.

# Questions

1. What were the inputs you gave the simulation? (Population size, percent vaccinated, virus name, mortality rate, reproductive rate)
2. What percentage of the population became infected at some point before the virus burned out?
3. What percentage of the population died from the virus?
4. Out of all interactions sick individuals had during the entire simulation, how many total interactions did we see where a vaccination saved a person from potentially becoming infected?

[Answers](answers.txt)
