#!/usr/bin/env/ python

import numpy as np
import matplotlib.pyplot as plt
import plotting_mod as pm

shape = (50, 50)
N = shape[0]
print(N)

#Initial Set-up (Generates lattice of random spins)
spins = np.random.choice([-1, 1], size=shape)

# Magnetic moment
moment = 0

# External magnetic field
field = np.full(shape, 0)

# Temperature (in units of energy)
temperature = 2.1

# Interaction (ferromagnetic if positive, antiferromagnetic if negative)
J = 1



def probability(energy1, energy2, temperature):
	return np.exp((energy1 - energy2) / temperature)

def get_energy(spins):
	return -np.sum(
	 J * spins * np.roll(spins, 1, axis=0) +
	 J * spins * np.roll(spins, -1, axis=0) +
	 J * spins * np.roll(spins, 1, axis=1) +
	 J * spins * np.roll(spins, -1, axis=1)
	 )/2 - moment * np.sum(field * spins)

def update(spins, temperature):
  	spins_new = np.copy(spins)
  	i = np.random.randint(spins.shape[0])
  	j = np.random.randint(spins.shape[1])
  	spins_new[i, j] *= -1
  
  	current_energy = get_energy(spins)
  	new_energy = get_energy(spins_new)
  	#print(current_energy, new_energy, probability(current_energy, new_energy,       temperature))
	a = np.random.random()
	#print(a)
  	if probability(current_energy, new_energy, temperature) > a:
		return spins_new
  	else:
		return spins




t = 0
#T = [ 100, 1000, 10000, 100000, 200000, 300000, 500000, 1000000]
while t <= 100000:
	spins = update(spins, temperature)
	#if t in T:
		#spins[spins == -1] = 0
		#pm.myplot(spins, "spins_%i.pbm" % t)	
	t += 1

spins[spins == -1] = 0
pm.myplot(spins, "spins.pbm")



