---
title: "InfoMag: A graphical user interface for INFOMAR's magnetometry data"
tags:
  - Python
  - Infomar
  - Magnetic anomaly
authors:
  - name: Frank Bastian
    orcid: 0000-0000-0000-0000
    corresponding: true
    affiliation: "1, 2" 
  - name: Mohit Tunwal
    affiliation: 2
  - name: Aaron Lim
    corresponding: 
    affiliation: 2
affiliations:
 - name: Dr. Margarete Fischer-Bosch-Institut für Klinische Pharmakologie, Germany
   index: 1
 - name: University College Cork, Ireland
   index: 2

---


# Summary


Here, we present an free and open open-source graphical user interface (GUI), built on python that can process magnetometry data set and enables a subsequent analysis through its exported magnetic anomaly grids.



# Statement of need
The INFOMAR programme is Ireland’s national seabed mapping programme that maps the country’s marine territory to support sustainable development, environmental protection, and marine resource management.
Over the last 20 years, various geological data sets such as bathymetry, sub-bottom profiler, and magnetometry data have been acquired, with significant portions of the bathymetry and backscatter data processed and made publicly available.
However, this has not been the case for the magnetometry data, which remains largely unprocessed in its raw format.


# Methods and functionality
The architecture consists of three packages: the IO module, the processing module, and the Graphic User Interface.
The Graphical User Interface implements the Model-View-Control pattern through the QT framework, which is exposed to Python through Pyside6.
To target a wider audience, including researchers and to allow for easy extensions, the software is purposely written in Python, serving as a graphical wrapper around standard scientific libraries such as matplotlib, numpy, scipy, and pandas.

The user interface consists of three windows assisting the user through the processing pipeline.
The main pipeline consists of four main steps: "csv import", "processing", "gridding and visualisation", and "CSV/Tiff export".
Optionally, there are two additional steps: "bathymetry import" and "downward continuation".
A visual representation of the pipeline is given in~\autoref{fig:pipeline} and a detailed description of each step is provided in the following paragraphs.


![The UI implements a processing pipeline that reads Infomar data, processes it, visualises it, potentially downward continues the anomaly grid and eventually exports the final result.
\label{fig:pipeline}](pipeline.png)

## CSV Import
In 2016, Infomar switched the acquisition software from SeaLink to Marine Magnetics BOB, resulting in a difference in the recorded files.
The IO module can handle both formats and provide a convenient single-action import for end users.
In addition, a custom import for arbitrary text-based (comma-separated) files is also provided.


## Processing, gridding and visualisation

Magnetometry data is obtained though towing a magnetometer behind a vessel.
Moving the vessel (along a line) creates a one dimensional time series of magnetometry data $|B(x,y,z_0,t)|$ with spacial data attached to each measuring point.
The timeseries $|B|(x,y,z_0,t)$ can be inspected in the bottom of the main window, and magnified in the "timeseries representation" window.
Next, $|B|(x,y,z_0,t)$ is used to estimate the total field magnetic anomalies
\begin{equation}
    U(x,y,z_0,t) = |\Bar{B}(x,y,z_0,t)|-|B(x,y,z_0,t)|.
    \label{eq:anomalies_time}
\end{equation}
To reduce noise, the user can smooth $|B(x,y,z_0,t)|$ using a running mean with a short, i.e. local, window size.


Additionally, we assume that changes in the ambient field $|\bar{B}(x,y,z_0,t)|$ caused by geological changes of the seabed or the diurnal changes of the magnetic field are on a slower timescale than the (fast) changes in $|B|(x,y,z_0,t)$, caused by moving over ferromagnetic objects such as ship wrecks.
Therefore, we estimate the ambient field $|\bar{B}(x,y,z_0,t)|$ akin to $|B(x,y,z_0,t)|$ as running mean but with a larger window size.
Based on preliminary work, we preset both parameters to initial values and leave them to the user to be further adjusted.

In the next step, the processed time series $U(x,y,z_0,t)$ is gridded using either a linear or nearest-neighbour interpolation, yielding a two dimensional representation, which we refer to as "anomaly grid".


## Export
Eventually, both the downward-continued field and the surface field, represented as a grid, can be exported.
This can either be text-based (CSV) or as a GeoTiff for further usage in another Geographic Information System (GIS) software.
Additionally, at any given moment during the processing pipeline, a snapshot of the underlying data that has been processed until this point can be exported into a CSV file as well.
 


# Future work
To enhance the performance and to bypass the global interpreter lock, an incremental replacement of modules with compiled C code is planned.
In order to verify the implementation of the downward continuation, we will collect magnetometry data on different altitudes using a fluxgate magnetometer Sensys FGM3D/100.
This will be featured in an additional paper, combined with a theoretical review of downward continuation, a case study on INFOMAR magnetometry data, and bathymetry imports for seabed depth.


# Acknowledgements
Financial support by the Geological Survey Ireland is gratefully acknowledged.


