import numpy as np
from numpy import pi
from scipy.special import erf

def find_beam_waist(params):
    """
    Returns the beam waist (m) that maximises the distance over which the beam
    is smaller than the sail.
    """
    radius = params["radius"]
    beam_waist = radius / np.sqrt(2)
    return beam_waist

def find_rayleigh_length(params):
    """
    Returns rayleigh length (m) - distance from beam waist at which beam is equal to
    the sail size.
    Rayleigh length is maximised by choice of beam waist.
    """
    area = params["area"]
    wavelength = params["wavelength"]
    z_r = area/(2*wavelength) #rayleigh length
    return z_r
#
# def find_focusing_length(params):
#     """
#     Returns the distance (m) from the laser array to the beam waist.
#     """
#     D = params["radius"]
#     d_0 = 0.5*params["diameter"] #radius of laser array
#     wavelength = params["wavelength"]
#     z_0 = pi*D*d_0/(np.sqrt(2)*wavelength) #focusing length
#     return z_0

# def find_start_distance(params):
#     """
#     Returns the distance (m) away from the laser array that the sail should
#     be launched. At this distance the beam width is equal to the sail radius.
#     """
#     z_0 = find_focusing_length(params)
#     z_r = find_rayleigh_length(params)
#     start_d = z_0 - z_r
#     return start_d

# def find_acceleration_distance(params):
#     """
#     By assumption, we make acceleration distance the distance between the
#     two critical points where the size of the beam is equal to the size of
#     the sail. This is 2 times the rayleigh length.
#     """
#     return 2*find_rayleigh_length(params)

def find_crit_dist(params):
    """
    Assume dynamically varying focus of Gaussian beam. Beam is focused such that
    the beam waist is at the sail until a diffraction-limited distance.
    Returns the diffraction-limited distance (m).
    """
    D = 2*params["radius"] #(m) Diameter of sail
    d = params["diameter"] #(m) Diamter of transmitter array
    wavelength = params["wavelength"] #(m) Wavelength of laser
    L = D*d/(2*wavelength)
    return L

def find_beam_width(params, dist):
    """
    Finds beam width at some distance from the transmitter.
    Assumes circular Gaussian beam, dynamically focused until diffraction-limited distance.
    """
    w_0 = find_beam_waist(params)
    try:
        crit_dist = find_crit_dist(params)
    except TypeError: #In the case where trying to find max temp, and diameter not given
        beam_width = w_0 
        return beam_width
    if dist <= crit_dist:
        beam_width = w_0
    elif dist > crit_dist:
        d_waist = dist - crit_dist #(m) Distance from beam waist, which is at diffraction-limited distance
        z_r = find_rayleigh_length(params) #(m) Rayleigh length
        beam_width = w_0*(1+(d_waist/z_r)**2)**0.5
    return beam_width

# def find_beam_width(params, dist):
#     """
#     Finds beam width at some distance from the transmitter.
#     Assumes circular Gaussian beam.
#     """
#     wavelength = params["wavelength"]
#     diameter = params["diameter"]
#     beam_width = np.sqrt(2) * dist * wavelength / diameter #m
#     return beam_width

def find_fraction_incident(params, dist):
    """
    Finds fraction of laser power incident on the sail.
    Assumes circular Gaussian beam and projection of sail is circular.
    """
    r = params["radius"]
    w = find_beam_width(params,dist)
    fraction = 1-np.exp(-2*r**2/w**2)
    return fraction

# #This is from Kulkarni 2018; assumes beam is Bessel. Not relevant to Gaussian beam, and no longer compatible with library.
# def find_crit_dist(params):
#     """
#     Input:  The set of parameters
#     Output: The critical distance at which the laser begins to spill over the sail. (m)
#     """
#     #Get parameters
#     m_sail = params["m_sail"]
#     thickness = params["thickness"]
#     density = params["density"]
#     k = params["k"]
#     diameter = params["diameter"]
#     wavelength = params["wavelength"]
#     alpha = params["alpha"]
#
#     #Calculate the critical distance
#     sail_size = np.sqrt(m_sail / (k*density*thickness))
#     critical_dist = diameter * sail_size / (2*wavelength*alpha)
#     return critical_dist
