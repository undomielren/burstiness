# Import packages 
import numpy as np
import pynbody as pb
import starlifetime as slt
import imf
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
import time
print("Loading packages...")
t1 = time.time()
import sys, os, time, gc
import numpy as np
sys.path.append(os.path.abspath("."))
t2 = time.time()
print("Packages loaded in " + str( round(t2-t1, 3) ) + "s.")
gc.collect()
print("Working directory:", os.getcwd())
machine = "Glaurung"
import pickle


cptmarvel_path = f"/myhome2/users/munshi/dwarf_volumes/cptmarvel.cosmo25cmb.4096g5HbwK1BH/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096"
        #halos : [1,2,3,5,6,7,10,11,13,14,24]
elektra_path = f"/myhome2/users/munshi/dwarf_volumes/elektra.cosmo25cmb.4096g5HbwK1BH/elektra.cosmo25cmb.4096g5HbwK1BH.004096/elektra.cosmo25cmb.4096g5HbwK1BH.004096"
        #halos : [1,2,3,4,5,8,9,10,11,12,17,36,64]
storm_path = f"/myhome2/users/munshi/dwarf_volumes/storm.cosmo25cmb.4096g5HbwK1BH/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096"
        #halos : [1,2,3,4,5,6,7,8,10,11,12,14,15,22,23,31,37,44,48,55,118]
rogue_path = f"/myhome2/users/munshi/dwarf_volumes/rogue.cosmo25cmb.4096g5HbwK1BH/rogue.cosmo25cmb.4096g5HbwK1BH.004096/rogue.cosmo25cmb.4096g5HbwK1BH.004096"
        #halos: [1,3,7,8,10,11,12,15,16,17,28,31,37,58,116] 

# Loading halo
print("Loading halo of interest...")
s = pb.load(rogue_path) #load marvel_path 
s.physical_units()
h = s.halos()

###--- Select from following halos:---###
#halos = [1,2,3,5,6,7,10,11,13,14,24] #cpt marvel
#halos = [1,2,3,4,5,8,9,10,11,12,17,36,64] #elektra
#halos = [1,2,3,4,5,6,7,8,10,11,12,14,15,22,23,31,37,44,48,55,118] #storm
#halos = [1,3,7,8,10,11,12,15,16,17,28,31,37,58,116] #rogue

halo_dir_path = "/myhome2/users/azartash/sncalc/rogue_halos" # change pathway to where you want the output file saved
os.chdir(halo_dir_path)
 

def last_star_formation(halo):
    tform = halo.star['tform'].in_units("Gyr")
    return np.max(tform)

   
def get_stellar_mass(halo):
    stellar_mass = halo.star['mass'].in_units("Msol").sum()
    return stellar_mass


def get_virial_mass(halo):
    virial_mass = halo['mass'].sum()
    return virial_mass

Data = {}

# Calculations
print('Calcualting last star formation, virial mass, stellar mass')

for hnum in halos:
    star_form_bins = last_star_formation(h[hnum]) 
    M_star = get_stellar_mass(h[hnum])
    M_vir = get_virial_mass(h[hnum])
    Data[str(hnum)] = {}
    Data[str(hnum)]['Last Star'] = star_form_bins
    Data[str(hnum)]['Stellar Mass'] = M_star
    Data[str(hnum)]['Virial Mass'] = M_vir
out = open('rogue_avg_burstiness.pickle', 'wb') #change to match SIM
pickle.dump(Data,out)
out.close

