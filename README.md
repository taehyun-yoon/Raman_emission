Bleach script
==========

This repository contains scripts to plot graphs of Raman decay rate vs detuning and power of Raman pump light and derive decay rate of excited state and metastable state.

Overview
--------

The file rabi.py calculates dipole moments and Rabi frequencies of each transition. Based on these Rabi frequencies, population.py file calculates the population on the excited states. plot_detuning.py and plot_power.py fit the final equation of Raman decay rate and plot graphs.

Dependencies
------------

- All codes are wrtten in python3

Description of files
--------------------

python files:

filename                     |  description
-----------------------------|------------------------------------------------------------------------------------
constant.py                  |  Defines physical constant values
rabi.py                      |  Calculates Rabi frequency
population.py                |  Calculates pupulation on excited states
plot_detuning.py             |  Plots the graph of Raman decay rate vs detuning
plot_power.py                |  Plots the graph of Raman decay rate vs power
