---
title: "InfoMag: A graphical user interface for INFOMAR's magnetometry data"
tags:
  - Python
  - INFOMAR
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
bibliography: paper.bib
---


# Summary
Magnetometry measures variations in the Earth’s magnetic field caused by ferromagnetic objects.
In the context of maritime geoscience, these are mostly caused by large-scale geological formations or shipwrecks and unexploded ordnance (UXO), whereas the latter are of particular interest for marine development.
Here, we present a graphical user interface (GUI) that wraps a processing pipeline to assist users in reading raw magnetometry data, processing it and eventually exporting an anomaly grid for further processing.


# Statement of need
The INFOMAR programme is Ireland’s national seabed mapping initiative, tasked with mapping the country’s marine territory in support of sustainable development, environmental protection, and marine resource management. 
Over the past two decades, INFOMAR has acquired a wide range of geophysical datasets, including bathymetry, sub-bottom profiler, and magnetometry data.
While substantial portions of the bathymetry and backscatter data have been processed and released publicly, the magnetometry data remain largely unprocessed in their raw format.

Processing raw magnetometry data presents several challenges, including sensor noise, acquisition artefacts, and corrupted measurements during sensor deployment or recovery.
An interactive visualisation of the raw data is essential for identifying such issues and enabling more efficient and comfortable cleaning.
Consequently, there is an urgent need for a user interface that allows users to visualise and interact with the raw data.

Furthermore, since INFOMAR data is surface-acquired, an additional step is needed to downward-continue the estimated anomaly grid to the seabed.
This enables a meaningful comparison to industry datasets, which are typically obtained close to the seabed.

# Methods and functionality
To target a broad audience, including researchers, and to facilitate extensibility, the software is implemented in Python. 
It provides a graphical wrapper around widely used scientific libraries, including NumPy, SciPy, pandas, and Matplotlib.
The software is structured into three main packages: an I/O module, a processing module, and a graphical user interface (GUI).
The GUI follows the Model–View–Controller (MVC) design pattern and is implemented using the Qt framework, exposed to Python through PySide6, to guide users through the processing workflow.
The main processing pipeline consists of four core stages: **CSV import**, **processing**, **gridding and visualization**, and **CSV/TIFF export**.
Two additional optional stages, **bathymetry import** and **downward continuation**, are available if desired.
An overview of the pipeline is shown in \autoref{fig:pipeline}, and each stage is described in more detail below.

![The UI implements a processing pipeline that reads INFOMAR data, processes it, visualises it, potentially downward continues the anomaly grid and eventually exports the final result.
\label{fig:pipeline}](pipeline.png)

## CSV import
In 2016, INFOMAR transitioned its acquisition software from SeaLink to Marine Magnetics BOB, resulting in differences in the structure and content of the recorded data files.
The I/O module supports both formats and provides a unified, single-action import mechanism for end users.
In addition, a custom import is available for arbitrary text-based (comma-separated) files, enabling the use of magnetometry data from external sources.


## Processing, gridding and visualisation

Marine magnetometry data are acquired by towing a magnetometer behind a survey vessel and measuring the total magnetic field $|B(x,y,z_0)|$.
As the vessel moves along a survey line, this produces a one-dimensional time series $|B(x,y,z_0,t)|$, with spatial coordinates associated with each measurement.
The raw time series $|B(x,y,z_0,t)|$ can be inspected in the lower panel of the main application window and further examined, magnified, and processed in a dedicated window.


To isolate the local magnetic anomalies, we need to subtract the large-scale contributions caused by geological structures or diurnal variations of the Earth’s magnetic field from the original timeseries $|B(x,y,z_0,t)|$ [@blakely1996potential]. 
We assume that these large-scale contributions occur on a slower timescale than the (fast) changes in $|B|(x,y,z_0,t)$, caused by moving over a local ferromagnetic object such as ship wrecks.
Therefore, we approximate the ambient field $|\bar{B}(x,y,z_0,t)|$ using a (slowly) running mean of the measured signal $|B|(x,y,z_0,t)$ and subtract it from the measured signal to obtain the residual timeseries
\begin{equation}
    U(x,y,z_0,t) = |\Bar{B}(x,y,z_0,t)|-|B(x,y,z_0,t)|,
    \label{eq:anomalies_time}
\end{equation}
where any significant deviations of $U(x,y,z_0,t)$ from zero are interpreted as local magnetic anomalies
To place these anomalies into a spatial context, the residual time series is interpolated onto a spatial grid, yielding the final anomaly grid, which can be used for visualisation and further analysis.


## Export
Both the surface and the downward-continued anomaly grid can be exported as a gridded dataset.
Currently, text-based (CSV) or image-based (GeoTIFF) file formats are supported, allowing direct integration with standard geographic information system (GIS) software.
Furthermore, at any stage of the processing pipeline, users may export a snapshot of the intermediate processed data to CSV, facilitating reproducibility, debugging, and external analysis.


# Future work
To improve performance and circumvent limitations imposed by the Python Global Interpreter Lock, an incremental replacement of selected modules with compiled C code is planned.
To validate the downward continuation module, magnetometry data will be collected at multiple altitudes using a Sensys FGM3D/100 fluxgate magnetometer.
The validation results will be presented in a separate publication, together with a theoretical review and a case study using INFOMAR magnetometry data, and the incorporation of bathymetric information.

# Acknowledgements
Financial support by the Geological Survey Ireland is gratefully acknowledged.

# References




