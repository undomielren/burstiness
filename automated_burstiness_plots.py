import os 
import numpy as np
import pynbody as pb
import starlifetime as slt
import imf
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
import pickle

cptm_halo_dir_path = "/myhome2/users/azartash/sncalc/cptmarvel_halos/"
elektra_halo_dir_path = "/myhome2/users/azartash/sncalc/elektra_halos/"
storm_halo_dir_path = "/myhome2/users/azartash/sncalc/storm_halos/"
rogue_halo_dir_path = "/myhome2/users/azartash/sncalc/rogue_halos/"

    #cpt_marvel_halos = [1,2,3,5,6,7,10,11,13,14,24]
    #elektra_halos = [1,2,3,4,5,8,9,10,11,12,17,36,64]
    #storm_halos = [1,2,3,4,5,6,7,8,10,11,12,14,15,22,23,31,37,44,48,55,118]
    #rogue_halos = [1,3,7,8,10,11,12,15,16,17,28,31,37,58,116] 

###---uncomment SIM you want to plot:---###

#CptM_Data = pickle.load(open(cptm_halo_dir_path + 'cpt_marvel_burstiness.pickle', 'rb'))
#cm_burstiness, cm_t_burst = [],[]
#for h in ['1','2','3','5','6','7','10','11','13','14','24']:
    #cm_burstiness = CptM_Data[h]['Burstiness'] 
    #cm_t_burst = CptM_Data[h]['Burstiness_bins'] 

#Elektra_Data = pickle.load(open(elektra_halo_dir_path + 'elektra_burstiness.pickle', 'rb'))
#e_burstiness, e_t_burst = [],[]
#for h in ['1','2','3','4','5','8','9','10','11','12','17','36','64']:
    #e_burstiness = Elektra_Data[h]['Burstiness'] 
    #e_t_burst = Elektra_Data[h]['Burstiness_bins'] 

#Storm_Data = pickle.load(open(storm_halo_dir_path + 'storm_burstiness.pickle', 'rb'))
#s_burstiness, s_t_burst = [],[]
#for h in ['1','2','3','4','5','6','7','8','10','11','12','14','15','22','23','31','37','44','48','55','118']:
    #s_burstiness = Storm_Data[h]['Burstiness']    
    #s_t_burst = Storm_Data[h]['Burstiness_bins']  

#Rogue_Data = pickle.load(open(rogue_halo_dir_path + 'rogue_burstiness.pickle', 'rb'))
#r_burstiness, r_t_burst = [],[]
#for h in ['1','3','7','8','10','11','12','15','16','17','28','31','37','58','116'] :
    #r_burstiness = Rogue_Data[h]['Burstiness']
    #r_t_burst = Rogue_Data[h]['Burstiness_bins']
    
    print("Creating plots...")
    # Plotting of star formation rate and burstiness
    # activate latex text rendering
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)
    plt.figure()    
    #fig, ax1 = plt.subplots()
    plt.plot(r_t_burst, r_burstiness, color='darkmagenta', label='Burstiness') #change to match SIM
    plt.ylabel('Burstiness')
    plt.title('Rogue ' + str(h)) #change title for each SIM (Cpt Marvel, Elektra, Storm, Rogue)
    plt.xlabel(r'Time [\textit{Gyr}]')
    plt.xlim(0,14)
    plt.ylim(-1,1)
    os.chdir(rogue_halo_dir_path) #change to where you want plots saved 
    plt.savefig('burstiness_rogue_halo' + str(h) + '.jpg') #change filename to match SIM
    plt.show()

