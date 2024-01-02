import numpy as np

r_wing = 350 # mm
r_rod = 203  # mm
g = 9.81 # m/s^2
# Values subjected to change 
# --------------------
w = 600
alpha = 0 #rad/s^2 angular acceleration
wrad = w*2*np.pi/60 # rad/s
width = 24 # mm
b = 4 # mm
a = 4 # mm
m_wing = 1 # kg
m_rod = 3 # kg
d_bolt = 4 # mm
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
FOS_tensile = float('inf')

for i in range(0,len(data[:,0])): 
    Fn = data[i,0] 
    Ft = -1*data[i,1]
    #print(Fn,Ft) 

    Fx = (Fn+m_wing*wrad**2*(r_wing/1000)+2*m_rod*wrad**2*(r_rod/1000))/2  # N
    Mz = (Ft*r_wing+m_wing*alpha*r_wing+2*m_rod*alpha*r_rod)/2  # Nmm
    Ftot = np.sqrt((0.35*Fx)**2+(Mz/(d_b*2))**2) # N
    
    #Shear Failure of bolt
    tau_shear = Ftot/(np.pi*(d_bolt/2)**2) # MPa
    FOS_shear = min(FOS_shear,tau_yield_b/tau_shear) # FOS for shear failure
    #Bending Failure of bolt
    sigma_bending = (Ftot*(a+b)/2)*d_bolt/2/I_bolt # MPa
    FOS_bending = min(FOS_bending,sigma_yield_b/sigma_bending) # FOS for bending failure
    #Bearing Failure of part
    sigma_bearing = 2*Ftot/(b*d_bolt) # MPa
    FOS_bearing = min(FOS_bearing,sigma_bearing_st/sigma_bearing) # FOS for bearing
    #Tensile Failure of part
    sigma_tensile = Fx/(b*width-d_bolt*b) # MPa
    FOS_tensile = min(FOS_tensile,sigma_yield_st/sigma_tensile) # FOS for tensile
    #Debug Print
    #print(f"Fn: {Fn}\nFt: {Ft}\nFx: {Fx}\nMz: {Mz}\nFtot: {Ftot}\ntau_shear: {tau_shear}\nsigma_bending: {sigma_bending}\nsigma_bearing: {sigma_bearing}\nsigma_tensile: {sigma_tensile}\n")

print("-----------------------------\nBolt Loading Results\n-----------------------------")
print(f"Rotation speed of wing: {w} rpm\nAngular acceleration of wing: {alpha} rad/s^2\nThickness of connecting parts: {b} mm\nBolt diameter: {d_bolt} mm\nDistance between bolts: {d_b} mm\nMass of wing: {m_wing} kg\nMass of rod: {m_rod} kg\n")
if FOS_shear > 1 and FOS_bearing > 1 and FOS_bending > 1 and FOS_tensile > 1:
    print("Bolts are safe")
    print(f"Shear FOS: {FOS_shear}")
    print(f"Bearing FOS: {FOS_bearing}")
    print(f"Bending FOS: {FOS_bending}")
    print(f"Tensile FOS: {FOS_tensile}")

else:
    print("Bolts are not safe")
    if FOS_shear < 1:
        print(f"Shear FOS: {FOS_shear}")
    if FOS_bearing < 1:
        print(f"Bearing FOS: {FOS_bearing}")
    if FOS_bending < 1:
        print(f"Bending FOS: {FOS_bending}")
    if FOS_tensile < 1:
        print(f"Tensile FOS: {FOS_tensile}")


