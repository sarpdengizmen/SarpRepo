import numpy as np


r_wing = 350 # mm
g = 9.81 # m/s^2
# Values subjected to change 
# --------------------
w = 300 # rpm
wrad = w*2*np.pi/60 # rad/s
alpha = 0 #rad/s^2 angular acceleration
b = 24 # mm
h = 4 # mm
m_wing = 1 # kg
d_bolt = 4 # mm
d_t = 10 # mm moment arm of tangential force
d_b = 5*d_bolt # mm distance between bolts
# --------------------
sigma_yield_st = 215 # MPa STEEL 304
sigma_bearing_st = 1.5*sigma_yield_st # MPa
#For Bolt
sigma_yield_b =200 # MPa Bolt material tensile strength
tau_yield_b = 0.5*sigma_yield_b
I_bolt = np.pi*(d_bolt/2)**4/4 # mm^4


# Import the data from the excel file
data = np.genfromtxt('Normal_Tang.csv', delimiter=',', skip_header=1)
data = data[:,1:]
FOS_shear = float('inf')
FOS_bearing = float('inf')
FOS_bending = float('inf')

for i in range(0,len(data[:,0])):
    Fn = data[i,0]
    Ft = data[i,1]

    F_iax = m_wing*wrad**2*(r_wing/1000) # N axial inertial force
    F_it = m_wing*alpha*(r_wing/1000) # N tangential inertial force
    M_t = (Ft+F_it)*d_t # Nmm 

    F_x = (Ft+F_it)/4 # N
    F_y = (Fn+F_iax)/4 + M_t/(2*d_b)# N
    F_tot = np.sqrt(F_x**2+F_y**2) # N
    #Shear Failure of bolt
    tau_shear = F_tot/(np.pi*(d_bolt/2)**2) # MPa
    FOS_shear = min(FOS_shear,tau_yield_b/tau_shear) # FOS for shear failure
    #Bending Failure of bolt
    sigma_bending = (F_tot*h)*d_bolt/2/I_bolt # MPa
    FOS_bending = min(FOS_bending,sigma_yield_b/sigma_bending) # FOS for bending failure
    #Bearing Failure of part
    sigma_bearing = F_tot/(h*d_bolt) # MPa
    FOS_bearing = min(FOS_bearing,sigma_bearing_st/sigma_bearing) # FOS for bearing 
    #Debug Print
    #print(f"Fn: {Fn}\nFt: {Ft}\nF_iax: {F_iax}\nF_it: {F_it}\nM_t: {M_t}\nF_x: {F_x}\nF_y: {F_y}\nF_tot: {F_tot}\ntau_shear: {tau_shear}\nsigma_bending: {sigma_bending}\nsigma_bearing: {sigma_bearing}\n")
    
    
print("-----------------------------\nBolt Loading Results\n-----------------------------")
print(f"Rotation speed of wing: {w} rpm\nAngular acceleration of wing: {alpha} rad/s^2\nThickness of connecting parts: {h} mm\nBolt diameter: {d_bolt} mm\nDistance between bolts: {d_b} mm\nMoment arm for tangential force: {d_t} mm\nMass of wing: {m_wing} kg\n")
if FOS_shear > 1 and FOS_bearing > 1 and FOS_bending > 1:
    print("Bolts are safe")
    print(f"Shear failure of Bolt FOS: {FOS_shear}\nBending failure of Bolt FOS: {FOS_bending}\nBearing failure of part FOS: {FOS_bearing}")

else:
    print("Bolts are not safe")
    if FOS_shear < 1:
        print(f"Shear failure of Bolt FOS: {FOS_shear}")
    if FOS_bearing < 1:
        print(f"Bearing failure of part FOS: {FOS_bearing}")
    if FOS_bending < 1:
        print(f"Bending failure of Bolt FOS: {FOS_bending}")




