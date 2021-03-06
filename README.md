#starshot_lib
Python library relating to the Starshot Breakthrough project.

Currently the library is not very accessible; I will fix this up over the semester break. Including:
• Using classes
• Making code more efficient
• Removing unnecessary stuff

###
A circular sail is propelled by a laser beam, produced from a circular laser array, to a target velocity.
###

###

This directory should be placed in the same directory as the file using it.

###

To use the functions, one must define parameters for the spacecraft in this format and order:
	
	params = { "material": 'SiO2',
			 "m_sail": 1e-3,
			 "thickness": None,
			 "area": 10,
			 "density": 1400,
			 "abs_coeff": 1e-3,
			 "absorptance": None,
			 "reflectance": None,
			 "transmittance": None,
			 "k": 1,
			 "power": 1e11,
			 "laser_size": 1e4, 
			 "wavelength": 1064e-9,
			 "alpha": 1}

========================================================================================================
Parameter							Defintion
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"material"  	---------------------------- 	sail material; see the list below
								Input: 	string
								List of materials and their corresponding strings
       			 						Material              	String
        			 						Silica    	------------ 'SiO2'
									Germania ------------ 'GeO2'
        			 						Will be updated
									
"m_sail"     	---------------------------- 	mass of the sail
								Input:	int, float
								Units:	kg
								
"thickness"	----------------------------		thickness of the sail, or thickness of layers in multilayer sail
								Input:	list containing ints, floats
								Units:	m

"area"		----------------------------		surface area of one side of the sail
								Input:	int, float
								Units:	m^2
								
"radius"		----------------------------		radius of the circular sail
								Input:	int, float
								Units:	m
								
"density"		----------------------------		volume density of sail material (not including the payload)
								Input:	int, float
								Units:	kgm^-3

"abs_coeff"	----------------------------		absorption coefficient of the material
								Input:	int, float
								Units:	cm^-1
								
"absorptance"	----------------------------		fraction of radiant flux absorbed by the sail, specifically at the non-doppler-shifted laser wavelength
								Input:	None
								
"reflectance"	----------------------------		fraction of radiant flux reflected off the sail, specifically at the non-doppler-shifted laser wavelength
								Input:	None
								
"transmittance"	----------------------------		fraction of radiant flux transmitted through sail, specifically at the non-doppler-shifted laser wavelength
								Input:	None
								
"W"			----------------------------		Square root of RAAD ('reflectivity-adjusted area density') which is the figure of merit in Ilic 2018.
								Input:	None
								Units:	\sqrt(g)/m
								
"power"		----------------------------		laser power from the DE (directed energy) system
								Input:	int, float
								Units:	W

"diameter"		----------------------------		diameter of the transmitter system; must be at least the diameter of the sail (to minimise diffraction losses)
								Input:	int, float, None
								Units:	m

"wavelength"	----------------------------		wavelength of the laser, not including relativistic doppler shift
								Input:	int, float
								Units:	m
								
"target"		----------------------------		target speed as a fraction of the speed of light
								Input:	int, float
								Units:	Unitless
								
"accel_dist"	----------------------------		distance at which target speed is reached
								Input:	int, float
								Units:	m
								
"max_temp"	----------------------------		maximum temperature that the sail should reach
								Input:	int, float
								Units:	K
========================================================================================================

