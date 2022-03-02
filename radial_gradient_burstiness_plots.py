import os 
import numpy as np
import pynbody as pb
import starlifetime as slt
import imf
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from matplotlib import cm
from colorspacious import cspace_converter
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
import pickle

sncalc = "/myhome2/users/azartash/sncalc/"
cptm_halo_dir_path = "/myhome2/users/azartash/sncalc/cptmarvel_halos/"
elektra_halo_dir_path = "/myhome2/users/azartash/sncalc/elektra_halos/"
storm_halo_dir_path = "/myhome2/users/azartash/sncalc/storm_halos/"
rogue_halo_dir_path = "/myhome2/users/azartash/sncalc/rogue_halos/"

cptmarvel_gradients = np.loadtxt(sncalc + 'gradients_cptmarvel.txt')
#cm_data = np.array(cptmarvel_gradients)

elektra_gradients = np.loadtxt(sncalc + 'gradients_elektra.txt')
#e_data = np.array(elektra_gradients)

storm_gradients = np.loadtxt(sncalc + 'gradients_storm.txt')
#s_data = np.array(storm_gradients)

rogue_gradients = np.loadtxt(sncalc + 'gradients_rogue.txt')
#r_data = np.array(rogue_gradients)

cm_data = pickle.load(open(cptm_halo_dir_path + 'cpt_marvel_burstiness.pickle', 'rb'))
cm_Data = pickle.load(open(cptm_halo_dir_path +'cpt_marvel_avg_burstiness.pickle', 'rb'))

e_data = pickle.load(open(elektra_halo_dir_path +'elektra_burstiness.pickle', 'rb'))
e_Data = pickle.load(open(elektra_halo_dir_path +'elektra_avg_burstiness.pickle', 'rb'))

s_data = pickle.load(open(storm_halo_dir_path +'storm_burstiness.pickle', 'rb'))
s_Data = pickle.load(open(storm_halo_dir_path +'storm_avg_burstiness.pickle', 'rb'))

r_data = pickle.load(open(rogue_halo_dir_path +'rogue_burstiness.pickle', 'rb'))
r_Data = pickle.load(open(rogue_halo_dir_path +'rogue_avg_burstiness.pickle', 'rb'))

cptm_halos = [1,2,3,5,6,7,10,11,13]
elektra_halos = [1,2,3,4,5,9,10,11,12,17,36]
storm_halos = [1,2,3,4,5,6,7,8,10,11,12,14,15,23,31,44]
rogue_halos = [1,3,7,8,10,11,12,15,16,17,28,31,37]

cm_avg_burstiness , cm_avg_active_burstiness = [],[]
for h in ['1','2','3','5','6','7','10','11','13']:
    cm_avg_burstiness.append(np.mean(cm_data[h]['Burstiness']))
    burstiness = cm_data[h]['Burstiness']
    t_burst = cm_data[h]['Burstiness_bins']
    last_star_form = cm_Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<cm_Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    cm_avg_active_burstiness.append(np.mean(new_burstiness))

e_avg_burstiness , e_avg_active_burstiness = [],[]
for h in ['1','2','3','4','5','9','10','11','12','17','36']:
    e_avg_burstiness.append(np.mean(e_data[h]['Burstiness']))
    burstiness = e_data[h]['Burstiness']
    t_burst = e_data[h]['Burstiness_bins']
    last_star_form = e_Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<e_Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    e_avg_active_burstiness.append(np.mean(new_burstiness))

s_avg_burstiness , s_avg_active_burstiness = [],[]
for h in ['1','2','3','4','5','6','7','8','10','11','12','14','15','23','31','44']:
    s_avg_burstiness.append(np.mean(s_data[h]['Burstiness']))
    burstiness = s_data[h]['Burstiness']
    t_burst = s_data[h]['Burstiness_bins']
    last_star_form = s_Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<s_Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    s_avg_active_burstiness.append(np.mean(new_burstiness))

r_avg_burstiness , r_avg_active_burstiness = [],[]
for h in ['1','3','7','8','10','11','12','15','16','17','28','31','37']:
    r_avg_burstiness.append(np.mean(r_data[h]['Burstiness']))
    burstiness = r_data[h]['Burstiness']
    t_burst = r_data[h]['Burstiness_bins']
    last_star_form = r_Data[h]['Last Star']
    t_burst=np.array(t_burst)
    active = np.where(t_burst<r_Data[h]['Last Star'])[0]
    new_t_burst = t_burst[active]
    new_burstiness = burstiness[active]
    r_avg_active_burstiness.append(np.mean(new_burstiness))


print("Creating plots...")
# Plotting of star formation rate and burstiness
# activate latex text rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
fig, ax1 = plt.subplots()
c = cptmarvel_gradients
t = cm_avg_active_burstiness
im = ax1.scatter(cptmarvel_gradients,cm_avg_active_burstiness, c=t, cmap='twilight_shifted')
ax1.set_ylabel('Mean Active Burstiness')
#ax1.set_ylabel('Mean Burstiness')
fig.suptitle('Cpt. Marvel')
#ax1.set_xlim([-10, 2])
fig.colorbar(im, ax=ax1)
ax1.set_xlabel(r'Age Gradients')
plt.savefig('avg_active_burstiness_agegradients_cptmarvel.jpg')
plt.show()



