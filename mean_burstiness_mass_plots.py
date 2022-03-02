import os 
import numpy as np
import pynbody as pb
import starlifetime as slt
import imf
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter
from matplotlib import rc
import pickle

cptm_halo_dir_path = "/myhome2/users/azartash/sncalc/cptmarvel_halos/"
elektra_halo_dir_path = "/myhome2/users/azartash/sncalc/elektra_halos/"
storm_halo_dir_path = "/myhome2/users/azartash/sncalc/storm_halos/"   
rogue_halo_dir_path = "/myhome2/users/azartash/sncalc/rogue_halos/"  

###---Select for Cpt Marvel if plotting individual SIM---###
halos = [1,2,3,5,6,7,10,11,13,14,24] 
data = pickle.load(open(cptm_halo_dir_path + 'cpt_marvel_burstiness.pickle', 'rb')) 
Data = pickle.load(open(cptm_halo_dir_path +'cpt_marvel_avg_burstiness.pickle', 'rb'))
avg_burstiness , stellar_mass, virial_mass, avg_active_burstiness = [],[],[],[]
for h in ['1','2','3','5','6','7','10','11','13','14','24']:
    avg_burstiness.append(np.mean(data[h]['Burstiness']))
    stellar_mass.append(Data[h]['Stellar Mass'])
    virial_mass.append(Data[h]['Virial Mass'])
    burstiness = data[h]['Burstiness']
    t_burst = data[h]['Burstiness_bins']
    last_star_form = Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    avg_active_burstiness.append(np.mean(new_burstiness)) 

###---Select for Elektra if plotting individual SIM---###
halos = [1,2,3,4,5,8,9,10,11,12,17,36,64]
data = pickle.load(open(elektra_halo_dir_path +'elektra_burstiness.pickle', 'rb'))
Data = pickle.load(open(elektra_halo_dir_path +'elektra_avg_burstiness.pickle', 'rb'))
#avg_burstiness , stellar_mass, virial_mass, avg_active_burstiness = [],[],[],[] #uncomment to do SIM individually
for h in ['1','2','3','4','5','8','9','10','11','12','17','36','64']:
    avg_burstiness.append(np.mean(data[h]['Burstiness']))
    stellar_mass.append(Data[h]['Stellar Mass'])
    virial_mass.append(Data[h]['Virial Mass'])
    burstiness = data[h]['Burstiness']
    t_burst = data[h]['Burstiness_bins']
    last_star_form = Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    avg_active_burstiness.append(np.mean(new_burstiness))

###---Select for Storm if plotting individual SIM---###
halos = [1,2,3,4,5,6,7,8,10,11,12,14,15,22,23,31,37,44,48,55,118]
data = pickle.load(open(storm_halo_dir_path +'storm_burstiness.pickle', 'rb'))
Data = pickle.load(open(storm_halo_dir_path +'storm_avg_burstiness.pickle', 'rb'))
#avg_burstiness , stellar_mass, virial_mass, avg_active_burstiness = [],[],[],[] #uncomment to do SIM individually
for h in ['1','2','3','4','5','6','7','8','10','11','12','14','15','22','23','31','37','44','48','55','118']:
    avg_burstiness.append(np.mean(data[h]['Burstiness']))
    stellar_mass.append(Data[h]['Stellar Mass'])
    virial_mass.append(Data[h]['Virial Mass'])
    burstiness = data[h]['Burstiness']
    t_burst = data[h]['Burstiness_bins']
    last_star_form = Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    avg_active_burstiness.append(np.mean(new_burstiness))

###---Select for Rogue if plotting individual SIM---###
halos = [1,3,7,8,10,11,12,15,16,17,28,31,37,58,116]
data = pickle.load(open(rogue_halo_dir_path +'rogue_burstiness.pickle', 'rb'))
Data = pickle.load(open(rogue_halo_dir_path +'rogue_avg_burstiness.pickle', 'rb'))
#avg_burstiness , stellar_mass, virial_mass, avg_active_burstiness = [],[],[],[] #uncomment to do SIM individually
for h in ['1','3','7','8','10','11','12','15','16','17','28','31','37','58','116'] :
    avg_burstiness.append(np.mean(data[h]['Burstiness']))
    stellar_mass.append(Data[h]['Stellar Mass'])
    virial_mass.append(Data[h]['Virial Mass'])
    burstiness = data[h]['Burstiness']
    t_burst = data[h]['Burstiness_bins']
    last_star_form = Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    avg_active_burstiness.append(np.mean(new_burstiness))

stellar_over_virial = [i/j for i, j in zip(stellar_mass, virial_mass)]

print("Creating plots...")
    # Plotting of star formation rate and burstiness
    # activate latex text rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
fig, ax1 = plt.subplots()
v = virial_mass
s = stellar_mass
r = stellar_over_virial
#c = avg_burstiness               #select for mean burstiness
c = avg_active_burstiness         #select for mean active burstiness
im = ax1.scatter(stellar_over_virial, avg_active_burstiness, c=r, cmap="twilight_shifted")       #change x, y and c=
fig.suptitle('Marvel') #change to match SIM
ax1.set_ylim(-1,0)
ax1.semilogx()
ax1.set_ylabel('Mean Active Burstiness')                      #change y label for Mean Burstiness or Mean Active Burstiness 
#ax1.set_xlabel(r'\textit{Stellar Mass ($M_{\odot}$)}')       #select for plotting Stellar or Virial Mass-- change title
ax1.set_xlabel(r'\textit{$Log_{10} (M_{stars}/M_{halo}$})')   #select for plotting log (stellar/virial)
fig.colorbar(im, ax=ax1)
plt.savefig('full_avg_active_burstiness_stellarovervirial_mass.jpg')     #change file name 
plt.show()



