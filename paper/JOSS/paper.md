---
title: "InfoMag: A graphical user interface for magnetometry data"
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
In the context of maritime geoscience, these variations are primarily caused by large-scale geological formations, shipwrecks, and unexploded ordnance (UXO). The latter are of particular interest for marine development.
We present a graphical user interface (GUI) that wraps a processing pipeline to help users read raw magnetometry data, process it, and export an anomaly grid for further analysis.
Although InfoMag was originally designed for INFORMAR, it can also be used to process custom marine magnetometry datasets and similarly shaped data, such as aerial data.

![The proposed user interface is designed to help users process raw magnetometry data and export anomaly grids, such as the one shown here.
\label{fig:ui}](Magnetometry_GreenRebel.png)


# Statement of need
The INFOMAR programme is Ireland’s national seabed mapping initiative, tasked with mapping the country’s marine territory in support of sustainable development, environmental protection, and marine resource management. 
Over the past two decades, INFOMAR has acquired a wide range of geophysical datasets, including bathymetry, sub-bottom profiler, and magnetometry data.
While substantial portions of the bathymetry and backscatter data have been processed and released publicly, the magnetometry data remain largely unprocessed in their raw format.

Processing raw magnetometry data poses several challenges, including sensor noise, acquisition artifacts, and corrupted measurements during sensor deployment or recovery.
An interactive visualisation of the raw data is essential for identifying such issues and enabling more efficient and comfortable cleaning.
Consequently, there is an urgent need for a user interface that allows users to visualise and interact with the raw data.
Moreover, the absence of an end-user processing software for magnetometry data is not limited to the INFOMAR dataset.

Additionally, INFOMAR data is surface-acquired.
To enable meaningful comparisons with industry datasets, which are typically obtained close to the seabed, an additional step called downward continuation is necessary.
This process estimates the magnetic field close to the seabed based on surface-acquired data.
However, downward continuation is prone to noise due to its amplification during the process.
This will be discussed further in a separate publication.


# Methods and functionality
To target a broad audience, including researchers, and to facilitate extensibility, the software is implemented in Python. 
It provides a graphical wrapper around widely used scientific libraries, including NumPy, SciPy, Pandas, and Matplotlib.
The software is structured into three main packages: an I/O module, a processing module, and a graphical user interface (GUI).
The GUI follows the Model–View–Controller (MVC) design pattern and is implemented using the Qt framework, exposed to Python through PySide6, to guide users through the processing workflow.
The main processing pipeline consists of four core stages: **CSV import**, **processing**, **gridding and visualization**, and **CSV/TIFF export**.
Two additional optional stages, **bathymetry import** and **downward continuation**, are available if desired.
An overview of the pipeline is shown in \autoref{fig:pipeline}, and each stage is described in more detail below.

![The software implements a processing pipeline that helps users read, process, and visualise magnetometry data, as well as export an anomaly grid.
\label{fig:pipeline}](pipeline.png)

## CSV import
In 2016, INFOMAR transitioned from using Marine Magnetics SeaLink to using Marine Magnetics BOB for its acquisition software, resulting in differences in the structure and content of the recorded data files.
The I/O module supports both formats and provides end users with a unified, single-action import mechanism.
Additionally, a custom import is available for arbitrary, text-based, comma-separated files, enabling the use of magnetometry data from external sources.


## Processing, gridding and visualisation

Marine magnetometry data is acquired by towing a magnetometer behind a survey vessel and measuring the total magnetic field $|B(x,y,z_0)|$.
As the vessel moves along a survey line, this produces a one-dimensional time series $|B(x,y,z_0,t)|$, with spatial coordinates associated with each measurement.
This time series can be inspected in the lower panel of the main application window and examined, magnified, and processed further in a dedicated window.

To isolate the local magnetic anomalies, we have to subtract the large-scale contributions caused by geological structures or diurnal variations of the Earth’s magnetic field from the original time series $|B(x,y,z_0,t)|$ [@blakely1996potential]. 
We assume that these large-scale contributions occur on a slower timescale than the (fast) changes in $|B|(x,y,z_0,t)$, which are caused by moving over a local ferromagnetic object, such as a shipwreck.
Therefore, we approximate the ambient field $|\bar{B}(x,y,z_0,t)|$ using a (slowly) running mean of the measured signal $|B|(x,y,z_0,t)$ and subtract it from the measured signal to obtain the residual time series:
\begin{equation}
    U(x,y,z_0,t) = |\Bar{B}(x,y,z_0,t)|-|B(x,y,z_0,t)|.
    \label{eq:anomalies_time}
\end{equation}
Any significant deviations of $U(x,y,z_0,t)$ from zero are interpreted as local magnetic anomalies.
To place these anomalies in spatial context, we interpolate the residual time series onto a spatial grid. This yields the final anomaly grid, which can be used for visualisation and further analysis.


## Export
Both the surface anomaly grid and the downward-continued anomaly grid can be exported as gridded datasets.
Currently, we support text-based (CSV) and image-based (GeoTIFF) file formats, which allow for direct integration with standard geographic information system (GIS) software.
Furthermore, users can export a snapshot of the intermediate processed data to CSV at any stage of the processing pipeline.

# Future work
To improve performance and circumvent limitations imposed by the Python Global Interpreter Lock, an incremental replacement of selected modules with compiled C code is planned.
To validate the downward continuation module, magnetometry data will be collected at multiple altitudes using a Sensys FGM3D/100 fluxgate magnetometer.
The validation results will be presented in a separate publication, together with a theoretical review and a case study using INFOMAR magnetometry data, and the incorporation of bathymetric information.

# Acknowledgements
This research was funded by Geological Survey Ireland under the Short Call 2024 programme (Project 2024‑SC‑007).

# References




