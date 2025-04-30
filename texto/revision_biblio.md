---
title: "Draft"
format: 
  html:
    toc: true
    code-fold: true
bibliography: Bibliography.bib
---

# Papers general overview:

[@soria-perpinya_validation_2021] : tested 36 algorithms for key variables for 296 measurements and also explores the complementary of S2 and S3.  
[@gholizadeh_comprehensive_2016] : Investigates commonly used approach and sensors in evaluating and quantifying 11 water quality parameters.  
[@Agustina_Sismande] : Análisis de la concentración de clorofila a en los embalses del Río Negro.  


# scratchs

the Secci Disk Depth (SDD) can relate to the eutrophic zone (the layer  of water that has depth where 1% of incident light arrives, concentrating majority of photosynthetic activity. Transparency is correlated with red band (transparent + absorption ?);

**Peak**: Spectral region where the light absorption achieve its highest value.

**Shoulder**: spectral region where the light absorption is less intense then the peak region, but still being significant.

**Troughs**: Spectral regions where water absorption is less intense, like valley. Can indicate chemical components.


## Land use/land cover

[@Agustina_Sismande]: Land use -> main trigger in contamination source. Agriculture's fertilizers runoff are the main nutrient source that contributes tot the eutrophication. While high Phosphorus and Nitrogen concentration promotes the eutrophication, the low water interchange rate also affects.


## Importance (Justification) 

Water quality monitoring is the process of determining the chemical, physical, and biological characteristics of water bodies and identifying the possible contamination source that degrade the water quality. [@gholizadeh_comprehensive_2016]

Water monitoring is required for sustainable urban water supply. The level of treatment required for human and animal consumption, agriculture, and industry necessitates an understanding of quality of water sources. [@gholizadeh_comprehensive_2016]

In-situ measurement of physical, chemical and biological Water Quality Parameters is costly, time consuming and labor intensive despite of having high accuracy. Thus it is not feasible for regional and simultaneous measurement at regional scale. Also, point sampling, as it is also known,  are not able to identify the spatial nor temporal variation of measured parameters. [@gholizadeh_comprehensive_2016]


## Water Quality Assessment
 *More & Gordon (apud. @gholizadeh_comprehensive_2016)* distinguished three different approaches for estimating concentration of water quality parameters:
 
 1. Empirical: Seeks statistical relationship between spectral bands or band combinations and the in-situ measured water parameter.
 2. Semi-empirical: Utilize the physical and spectral information to develop the algorithms, which are then correlated to the measured constituents (**parameter?**).
 3. Analytical (physical @gholizadeh_comprehensive_2016): Determine the constituents concentration by modeling the reflectance of surface water and utilizing the inherent and apparent optical characteristics. However, the semi-analytical approach use simplified analytical model.
 
 > The empirical approaches are easy to implement and requires less math skills. [gholizadeh_comprehensive_2016]
 
 
### Classification {#sec-water_class}

According to @gholizadeh_comprehensive_2016:
**Case 1:** Waters whose optical properties are determined primarily by phytoplankton and related colored dissolved organic matter [CDOM](#cdom) and detritus degradation products;
**Case 2:** Waters whose optical properties are significantly influenced by other constituents such as mineral particles, [CDOM](#cdom), or micro bubbles, whose concentrations do not co-variate with phytoplankton concentrations.


### Remote Sensing  

Water transparency is a key variable because the amount of light penetrating throughout the water column restricts the rate at which benthic algae, phytoplankton and macrophytes can assimilate energy for photosynthesis.

Water monitoring programs in compliance with water framework directive require a minimum frequency data. Remote sensing would serve to perform more frequent monitoring for key variables to determinate water ecological status.

Remote Sensing technique make it possible to have spatial and temporal view of surface water quality parameters and more effectively and efficiently monitor the water bodies and quantify water quality issue [@gholizadeh_comprehensive_2016].

Remote Sensing technique used alone for Water Quality Monitoring is not sufficient and must be used in conjunction with traditional sampling methods and field survey [@gholizadeh_comprehensive_2016]. On the other hand, Remote Sensing has four advantages on water quality monitoring, when applied with traditional sampling:
* It gives a synoptic view of the entire water body spatially and temporally;
* It allows a synchronized view of vast areas;
* Provides historical record and represents trends over time;
* Prioritizes sampling locations and field surveying times;

Remote Sensing is a complementary tool for Water Quality monitoring, which differently from in-situ measurement, allows a broader spatial analysis and temporal scale [@soria-perpinya_validation_2021]. 

specifically designed  for water studies and have Ocean and Land Color Instruments (OLCI) with narrower bands specifically positioned for some of the OAC, despite of having a coarse spatial resolution (300 meters);

S2 study of surface dynamics of large number of water bodies (> spatial resolution but less accurate. [@soria-perpinya_validation_2021]

The S2 position and bandwidth are not optimal to detect most of the features (`peak`, `shoulder` and `troughts`) caused by water Optically Active Constituents, like cyanobacteria how, because of the phycocianin absorption is only detected in S3. 

S3 > spectral and temporal resolution;
> Is S3 the estimation of phytoplankton and cyanobacteria are, uncorrelated as different band set can be used. While S2 there will be always a correlation which does not correspond to actual correlation of variables in water bodies, as phytoplankton type (blue algal, differs than PC-rich cyanobacteria. [@soria-perpinya_validation_2021]  **???**
Narrower bands of S3 facilitate finding specific features in water leaving radiance. [@soria-perpinya_validation_2021]
S3 algorithms can serve as further validation of S2 when spatial consistency of both is studied.

#### Remote Sensing limitations 
Main limitations of optical Remote Sensing are: it is limited to the uppermost part of the water column; it cannot provide information in cloudy days;[^11]

When considering multi spectral sensors, which usually has better spatial resolution, the broad spectral range of its bands makes difficult to find the specific feature (peaks, shoulder, troughs caused by water's Optically Active Constituents (OAC) from the water leaving reflectance. [^11]

Hyper spectral sensors like, Sentinel 3 (S3), which is [^11] 
[^11]: Confirmar si info is from @soria-perpinya_validation_2021 o @gholizadeh_comprehensive_2016.

@gholizadeh_comprehensive_2016 mentions as Remote Sensing limitations:

* Developed models from RS requires adequate calibration and validation using in-situ measurements;
* Can be used only in absence of clouds;
* Spatial, temporal, and spectral resolution limitations can confine the application of RS to assess water quality;
* The atmospheric interference also restricts the optical signals coming from water bodies.
* Most studies focuses on optically active variables: [$Chl_{a}$](#ref-chla), [CDOM](#ref-cdom), [TSS](ref-tss) and [TUR](#ref-tur).


#### SAR


## Study Area (Río Negro)

[@Agustina_Sismande]: Río Negro is a lotic system with the biggest water flow in Uruguay, with 930 m³/s and approximate length of 750 km. Its main land use are dedicated to agriculture (celulosis production). Its water is mainly used for human consumption, irrigation and industrial use (energy generation).
Reservoir:
  * Rincón del Bonete: 1,070 km²;
  * Palmar: 320 km²;
  * Baygorria: 100 km²;


## Variables

[@Agustina_Sismande]: Kaz90 is the depth on which 90% of incident light is absorbed by water and can be obtained by S2 `C2RCC` (Case 2 Regional Coastal Colour). Due to the low reflectivity of water, atmospheric correction in water quality remote sensing is a key process. S2-2A (sen3cor); 1C (TOA) using C3RCC version 2x for turbid water was used.


## Optically Active Constituents {#sec-oac}

Interacts with electromagnetic energy and change the spectral of leaving energy, thus, can be measured using remote sensing. Non OAC, although has no effect on leaving radiance, can be intractable and inferable from those OAC with which they has strong correlation. [@gholizadeh_comprehensive_2016]

Most commonly measured qualitative parameters:

|Variable|Abbreviation|OAC (yes/no) | description|
|---|---|---|--- |
|Chlorophyll a|Chl_a||
|secchi disk depth|SDD||
|temperature|Temp||
|Colored Disolved Organic Matter|CDOM||
|Total Organic Carbon|TOC||
|Disolved Organic Carbon|DOC||
|Total Suspended Matters|TSM||
|Turbidity|Tur||
|Sea Surface Salinity||
|Total phosphorus|TP||
|Chemical Oxigen Demand|COD||
|Biochemical Oxigen Demand|BOD||
|Eletrical Conductivity|EC||
|Amonia Nitrogen|AN||
: My Caption {#tbl-variables}

There are several other important water quality to variables (*Ph*, *Nitrogen*, etc) which existing literature omit due to their weak optical characteristics and low **signal-noise ratio**.


### Chlorophyll a {#sec-chl_a}

[@gholizadeh_comprehensive_2016] 
Algal blooms are directly related to $Chl_{a}$ concentration. It is essential for photosynthesis. It is found in plants, algae and cyanobacterias [^1] . $Chl_{a}$ is the mayor water  trophic indicator, as it acts as a link between nutrient concentrations (phosphorus, for instance) and algal production. While reflecting in green wave length, it absorbs energy from violet-blue and orange-red wave lengths.  [@gholizadeh_comprehensive_2016];

[^1]: buscar diferença.

In case 1 waters (see @sec-water_class), the empirical empirical model adequately estimates $Chl_{a}$ concentrations, according to @gholizadeh_comprehensive_2016 [^2], while on case 2 water are more complex and requires advanced approaches and techniques as optical properties are determined also by composition of *Dissolved Organic (and inorganic) Matter*.  Thus, algorithms developed for case 1 are not applicable for case 2 waters.

**Gelbstoff absorption** (caused by CDOM) *mask* [^3] blue-green region in casse 2 waters [@gholizadeh_comprehensive_2016].

[^2]: **confirm if this came from bibliography review.**

[^3]: Confirmar sentido de "mask". O que quer dizer?

It is known that $Chl_{a}$ has strong absorption between 450-475 nm (blue region) and at 670 nm (red); It has a refelction peak at 550 nm (green) and 700 nm (NIR).

As expected, *NDVI* ration have been used to retrieve $Chl_{a}$ [^4];
[^4]: Confirmar se o que é mencionado se referee a realmente usar Diferença normalizada o um simple ratio.

Thru a extensive literature review suggested that $Chl_{A}$ concentrations need wavelength near 675 and 700 nm.


### Colored Dissolved Organic Matter (CDOM) {#sec-cdom}

[@gholizadeh_comprehensive_2016] 
It is also known as *Gelbstoff and gilvin* absorption (?) is present in both fresh and saline waters. Together with [$Chl_{a}$](@sec-chl_a) dominate the water color. CDOM absorption can be several times and overlaps with the [$Chl_{a}$](#sec-chl_a) absorption [^5]. It can account for 50% of total absorption at 443 nm (blue wave length).
[^5]: confirmar!

the increase in CDOM concentration affects reflectance in the blue-green spectral region (below 500 nm) and its absorbance increases exponentially with decreasing wave length. This effect can complicate the use of $Chl_{a}$ and phytoplankton models.  [^6]
[^6]: Investigar o por qué dessa complicação.

* CDOM is important in ecology and carbon dynamics.
* Can affect water Inherent Optical Properties (IOP);
* Can be measured with the assumption that it co-variate with chlorophyll.
* CDOM is referred as color and PCU color (Platinum-Cobalt_Units);
* In recent study CDOM is reported as light absorption coefficients at given wave length (**???**);
* Hyperspectral presents advantages for their broad spectrum of narrow bands. The challenge is to identify the band to use;
* CDOM is reported as indicator for Dissolved Organic Carbon (DOC);


### Secchi Disk Depth {#sec-sdd}

[@gholizadeh_comprehensive_2016] 
* Is an optical property of water of water strongly related to water constituents. It exhibits inverse correlation with [Total Suspended Solids](#tss). 
* It can be used to study the relative **nutrient and solids loading** situations. 
* Its measurements is based on light attenuation principles and is also relative to water [tubidity](#tur).
* It has a significant correlation with atmospherically corrected satellite radiance.

Is is considered as a reasonable indicator of trophic  conditions ( except in high colored lakes with low [$Chl_{a}$](#chla).

*Lee et al.* (apud. @gholizadeh_comprehensive_2016) has developed a model that  relies only on the diffuse attenuation coefficient at a wavelength corresponding to the maximum transparency for such interpretation. The classic one relies on the beam attenuation coefficient [^7]
[^7]: Confirmar o que é **difuse attenuation**, **beam attenuation**, em que comprimento de onda atuam e cáculo.


#### Turbidity and Total Suspended Sediments {#sec-turtss}

[@gholizadeh_comprehensive_2016] 
* Are an optical water property which scatters and absorbs the light rather than transmit it in straight lines;
* Absorption is controlled by [$Chl_{a}$](#chla) and [CDOM](#cdom) or **Particulate Matter**.
* The more suspended particles, the more difficult for light to travel through the water and, therefore, the higher water turbidity.
* **Interpretation of remotely Sensed data just based on the color not adequate and accurate.
* It is linked to incoming sunlight that affects photosynthesis and also associated with [SDD](#sdd).
* Seven bands can be used for [TSS](#tss) due to complex substances [^8]
[^8]: . Confirmar essa frase; Qué bandas seriam?
* An increase of Dissolved Inorganic Materials causes the **peak** reflectance to shift from **green** to **red** region. 


### Total Phosphorus {#sec-tp}

[@gholizadeh_comprehensive_2016] 
* Consist of the measurement of all inorganic, organic and dissolved form of phosphorus whose increased quantity helps plants and algae to grow quickly.
* Directly related to [$Chl_{a}$](#chla) concentration and indirectly to transparency ([SDD](#sdd)).
* Is influenced by land use as agriculture by fertilizer-rich run off or effluent from waste water treatment plants.
* Challenging measurement due to spatial heterogeneity of field samples.
* Remote Sensing estimation of TP is based on its high correlation with (Optically Active Constituents)[#OAC].
* It is closely related to phytoplankton, (turbidity)[tur] and (Total Suspended Matter)[#tsm] and (Secchi Disk Transparency)[^9].
[^9]: Confirmar se é a mesma coisa: SDD e SDT. **Confirmar construção da frase com ands...**
* Hyperspectral airborne or spaceborne provides more potential to detect TP.
* Studies have shown that increasing TP results in tendency of increasing [$Chl_{A}$](#chla) may play a role as a proxy of phosphorus concentration.
* [$Chl_{A}$](#chla) and [TSS](#tss) can be used as the potential theoretical parameters for indirect prediction of TP.
* As phosphorus does not present optically Diagnostic, empirical modeling is considered the most applicable approach.
* There is a time lag for phytoplankton to consume phosphorus, making relationship between TP and $Chl_{A}$ or SD [^10] complicated.
[^10]: Confirmar o que seria o SD


### Water Temperature {#sec-temp}

[@gholizadeh_comprehensive_2016] 
* Water temperature regulates physical and biological processes in water.
* It influences the solubility and availability of chemicals.
* Affects [Dissolved Oxigen](#do) concentration.
* Is affected by seasonal variation (?)
* Must be evaluated with care when the water is stratified: No relation can be expected between surface and underwater surface.

### Dissolved Oxygen, Biochemical Oxygen Demand, Chemical Oxygen Demand {#sec-do} {#sec-bod} {#sec-cod}

[@gholizadeh_comprehensive_2016] 
* **Dissolved Oxygen (DO)** is crucial. It influences the living conditions. Can be affected by anthropogenic activities.
* **Biochemical Oxygen Demand (BOD)** is an measure of the amount of oxygen that bacteria will consume under aerobic conditions while decomposing organic matters. By exploiting DO, the bacteria decompose these organic materials resulting in a reduction in the level of DO necessary for supporting aquatic life.
* **Chemical Oxygen Demand (COD)** is the quantity of matter measured which chemical method that need to be oxygenized in water.
* Any discharge of effluent with high **BOD** accelerated bacterial growth which, in turn, consumes and thus, reduces the oxygen levels.
* No single identified and or recommended sensors can be used with high confidence to perform an appropriate model measure the reflectance of water from **DO**, **COD**, **BOD**. Several water quality models were developed to relate exponential, and logarithmic regression.

According to @gholizadeh_comprehensive_2016, there is no single identified or recommended sensor to be used to perform water reflectance model to measure DO, COD, BOD.


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

