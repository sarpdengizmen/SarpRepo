import numpy as np

def principal_stress_3d(sigma_x = 0, sigma_y = 0, sigma_z = 0, tau_xy = 0, tau_xz = 0, tau_yz = 0):
    '''
    Calculates and returns the principal stresses given the stress tensor
    '''
    stress_tensor = np.array([[sigma_x, tau_xy, tau_xz],
                                [tau_xy, sigma_y, tau_yz],
                                [tau_xz, tau_yz, sigma_z]])
    eigenvalues, eigenvectors = np.linalg.eig(stress_tensor)
    return eigenvalues

r_wing = 350 # mm
r_rod = 190  # mm
g = 9.81 # m/s^2
# Values subjected to change 
# --------------------
w = 600
alpha = 200 #rad/s^2 angular acceleration
wrad = w*2*np.pi/60 # rad/s
b = 15 # mm
h = 4 # mm
l = 328 # mm
m_wing = 0.4 # kg From NX
m_rod = 7.9*10**-6*b*h*l # kg
# --------------------
Iy = (b*h**3)/12 # mm^4
Iz = (h*b**3)/12 # mm^4
sigma_yield = 215 # MPa STEEL 304
E_mod = 193*10**3 # MPa

# Import the data from the excel file
data = np.genfromtxt('Normal_Tang.csv', delimiter=',', skip_header=1)
data = data[:,1:]
max_stress = 0
for i in range(0,len(data[:,0])): 
    Fn = data[i,0] 
    Ft = -1*data[i,1]
    #print(Fn,Ft) 

    Fx = (Fn+m_wing*wrad**2*(r_wing/1000)+2*m_rod*wrad**2*(r_rod/1000))/2  
    Fy = Ft/2+m_wing*alpha*(r_wing/1000)/2+m_rod*alpha*(r_rod/1000)
    Fz = (2*m_rod*g+m_wing*g)/2
    Mz = (Ft*r_wing)/2+m_wing*alpha*(r_wing/1000)*r_wing/2+m_rod*alpha*(r_rod/1000)*r_rod # Nmm
    My = (2*m_rod*g*r_rod+m_wing*g*r_wing)/2  # Nmm
    #print(Fx,Fy,Fz,Mz,My)

    # Section A
    sigma_xA = (Fx/(b*h))+(My*(h/2)/Iy)+(Mz*(b/2)/Iz) # MPa
    #print(sigma_xA)
    eigenvals = principal_stress_3d(sigma_x = sigma_xA)
    max_stress = max(max_stress,eigenvals[0])

    # Section B
    sigma_xB = (Fx/(b*h))-(My*(h/2)/Iy)+(Mz*(b/2)/Iz) # MPa
    #print(sigma_xB)
    eigenvals = principal_stress_3d(sigma_x = sigma_xB)
    max_stress = max(max_stress,eigenvals[0])

    # Section C
    sigma_xC = (Fx/(b*h))-(My*(h/2)/Iy)-(Mz*(b/2)/Iz) # MPa
    #print(sigma_xC)
    eigenvals = principal_stress_3d(sigma_x = sigma_xC)
    max_stress = max(max_stress,eigenvals[0])

    # Section D
    sigma_xD = (Fx/(b*h))+(My*(h/2)/Iy)-(Mz*(b/2)/Iz) # MPa
    #print(sigma_xD)
    eigenvals = principal_stress_3d(sigma_x = sigma_xD)
    max_stress = max(max_stress,eigenvals[0])

    # # Section E
    # sigma_xE = Fx/(b*h) # MPa
    # tau_xyE = -3/2*Fy/(b*h) # MPa
    # tau_xzE = -3/2*Fz/(b*h) # MPa
    # #print(sigma_xB,tau_xyB,tau_xzB)
    # eigenvals = principal_stress_3d(sigma_x = sigma_xE, tau_xy = tau_xyE, tau_xz = tau_xzE)
    # print(eigenvals)
print("-----------------------------\nConnection Rod Loading Results\n-----------------------------")
print(f"Rot. Speed = {w} rpm \nAng. Acc. = {alpha} rad/s^2\n Rod width = {b} mm \nRod height = {h} mm \nWing mass = {m_wing} kg\nRod mass = {m_rod} kg\nMax. Eq. Stress @ Critical C.S.= {max_stress} MPa")  
FOS = sigma_yield/max_stress
print(f"FOS = {FOS}")
print("Max deflection of rod due to weights = ", (m_rod*g*l**3)/(8*E_mod*Iy) + (m_wing*g*l**3)/(8*E_mod*Iy), "mm")