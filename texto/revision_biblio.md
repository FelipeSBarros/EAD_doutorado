
# Papers general overview:

[@soria-perpinya_validation_2021] : tested 36 algorithms for key variables for 296 measurements and also explores the complementary of S2 and S3.  
[gholizadeh_comprehensive_2016] : Investigates commonly used approach and sensors in evaluating and quantifying 11 water quality parameters.  

# scrachs
the Secci Disk Depth (SDD) can relate to the eutrophic zone (the layer  of water that has depth where 1% of incident light arrives, concentrating majority of photosynthetic activity. Transparency is correlated with red band (transparent + absorption ?);

**Peak**: Spectral region where the light absorption achieve its highest value.   

**Shoulder**: spectral region where the light absorption is less intense then the peak region, but still being significant.

**Troughs**: Spectral regions where water absorption is less intense, like valley. Can indicate chemical components.

## Importance (Justification) 
Water monitoring is required for sustainable urban water supply. The level of treatment required for human and animal consumption, agriculture, and industry necessitates an understanding of quality of water sources. [gholizadeh_comprehensive_2016]

In-situ measurement of physical, chemical and biological Water Quality Parameters is costly, time consuming and labor intensive despite of having high accuracy. Thus it is not feasible for regional and simultaneous measurement at regional scale. Also, point sampling, as it is also known,  are not able to identify the spatial nor temporal variation of measured parameters.
 
## Remote Sensing  

Water transparency is a key variable because the amount of light penetrating throughout the water column restricts the rate at which benthic algae, phytoplankton and macrophytes can assimilate energy for photosynthesis.

Water monitoring programs in compliance with water framework directive require a minimum frequency data. Remote sensing would serve to perform more frequent monitoring for key variables to determinate water ecological status.

Remote Sensing is a complementary tool for Water Quality monitoring, which differently from in-situ measurement, allows a broader spatial analysis and temporal scale [@soria-perpinya_validation_2021]. Main limitations of optical Remote Sensing are: it is limited to the uppermost part of the water column; it cannot provide information in cloudy days;
When considering multi spectral sensors, which usually has better spatial resolution, the broad spectral range of its bands makes difficult to find the specific feature (peaks, shoulder, troughs caused by water's Optically Active Constituents (OAC) from the water leaving reflectance.

Hyper spectral sensors like, Sentinel 3 (S3), which is specifically designed  for water studies and have Ocean and Land Color Instruments (OLCI) with narrower bands specifically positioned for some of the OAC, despite of having a coarse spatial resolution (300 meters);

S2 study of surface dynamics of large number of water bodies (> spatial resolution but less accurate. [@soria-perpinya_validation_2021]

The S2 position and bandwidth are not optimal to detect most of the features (`peak`, `shoulder` and `troughts`) caused by water Optically Active Constituents, like cyanobacteria how, because of the phycocianin absorption is only detected in S3. 

S3 > spectral and temporal resolution;
> Is S3 the estimation of phytoplankton and cyanobacteria are, uncorrelated as different band set can be used. While S2 there will be always a correlation which does not correspond to actual correlation of variables in water bodies, as phytoplankton type (blue algal, differs than PC-rich cyanobacteria. [@soria-perpinya_validation_2021] ???
Narrower bands of S3 facilitate finding specific features in water leaving radiance. [@soria-perpinya_validation_2021]
S3 algorithms can serve as further validation of S2 when spatial consistency of both is studied.

**Qué son los Water Quality Parameters (WQP)?**  

**Como se los evalúa tradicionalmente?**  

**Qué debilidades tiene el uso de la teledetcción en la evaluación de los WQP?**  

**Qué serían Water Optically Constituent?**  

Are water components that interacts and change water optical property by scattering, reflecting and absorbing light. Example of Water Active Components are: phytoplankton, sediments, among other. 

**Qué quiere decir "Optically Active parameter?**  

**Cuales serían "Optically active? y cuales no serían?**  

**Qué son y como se diferencian los parametros de medición de los WQP "physical", "chemical" y/o "biological"?**  

**Qué es la eutrophication?**  

> nutrient availability (F y P).: > Algae activity and Algae bloom .: > decomposition > oxygen consumption.

The increase of chlorophyll and algal biomass are symptomatic signs of eutrophication, included in the *Normative Definitions of Ecological Status Classes* [@soria-perpinya_validation_2021] 
Chlorophyll a is a proxy of phytoplankton biomass (term referring to all aquatic environmental vegetation organisms), which includes cyanobacteria: photosynthetic organism responsible for toxins that affects water consumption. Phycocianin is the blue-green pigment (PC) responsible for photosynthesis, which absorbs at 620 nm (It is said that S3 can be measured while in S2, no [@soria-perpinya_validation_2021]. 

**Qué actividades pueden favorecer su condición (eutrophication)?**  


**Qué Parámetros son correlacionados entre sí?**  


**OTHER**

> The spectra studied are mostly influenced by Total Suspended Solids (TSS) and phytoplankton, the  main Optical Active Component that affect water transparency, thus determining the bands that better correlates with variable. [@soria-perpinya_validation_2021]

> High correlation between Total Suspended Solids (TSS) and Chlorophyll a (Chl_a) indicates that the main drivers of optical properties is the phytoplankton. [@soria-perpinya_validation_2021]

> CDOM has less influence in water transparency [@soria-perpinya_validation_2021]

> Secci Disk Depth (SDD) is affected by all Optically Active Components, thus is difficult to find conclusion and reasons on adoption of some bands [@soria-perpinya_validation_2021]

