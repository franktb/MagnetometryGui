.. _sec:TimeSeriesProcessing:

Time series processing
======================

Next, we recommend inspecting the time-series through the \enquote{timeseries}-window, which can be opened through the dropdown menu {\em view}.
The \enquote{timeseries}-window facilitates two key tasks: displaying the time-series and manipulating it.
The time series itself can be displayed by clicking on \inlinegraphics{./../../src/ui_elements/icons/area-chart-icon.png}.
This also replicates the time-series on the main window and vice versa if \inlinegraphics{./../../src/ui_elements/icons/area-chart-icon.png} is clicked on the main window.
Moreover, this operation internally smooths the time series and calculates the residuals as the difference between the ambient field, estimated as a slow running mean, and the current field, estimated as a fast running mean.
The used window size of both means is preset upon preliminary work.
However, it can be adjusted through the text fields on the right-hand sight of either the main window ot the times series window. 