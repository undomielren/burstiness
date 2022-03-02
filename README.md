# burstiness
automated_burstiness.py will create a pickle file for each Marvel SIM after selecting halo list. Change file name for each SIM

automated_burstiness_plots.py will generate burstiness plots for each halo within a Marvel SIM. Uncomment the SIM you want to plot.

mean_burstiness.py will create a pickle file for the last star formation, stellar mass, and virial mass for all halos within a Marvel SIM. 
Load the desired Marvel path and match the halo list.

mean_burstiness_plots.py will calculate the mean burstiness and mean active burstiness for all halos in all Marvel SIMs and plot against 
stellar mass, virial mass, or log (stellar/virial). The default will plot data for all SIMs. To plot each SIM individually, uncomment
"avg_burstiness , stellar_mass, virial_mass, avg_active_burstiness = [],[],[],[]" under each SIM. 
