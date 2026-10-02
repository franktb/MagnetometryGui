.. _sec:DepthClipping:

Time series depth clipping
==========================

Time-series data containing depth information (see :ref:`sec:SensysImport`) can be separated into distinct depth layers.
When ``Clip layer`` is selected without specifying a depth, the bottom plot displays the depth values of the complete time series in black.
This overview can be used to identify the layers.

A layer is defined in the menu on the right-hand side (see :numref:`fig:depthClipZoom`) by specifying a depth :math:`z` (in m) and a tolerance :math:`\epsilon`.
These parameters define the interval defines an interval :math:`(z-\epsilon, z+\epsilon)`.
All data points with depth values within this interval are assigned to the same depth layer.
To exclude isolated points and points belonging to descending trajectories toward greater depths, a neighborhood size can additionally be specified.
Only points with at least the required number of neighboring points within the interval :math:`(z-\epsilon,\,z+\epsilon)` are retained.
Points that do not satisfy this criterion are discarded.

.. note::
   Neighboring points are evaluated in both the positive and negative time directions relative to the current point.

.. _fig:depthClipZoom:

.. figure:: pics/depths_clip_input.png
   :width: 40%

   Using ``+ Add values`` allows the insertion of an additional depth value that can also be deleted by clicking on the corresponding ``x``.


The clipped layers are displayed in different colors ontop of the full time series for the user to check (see :numref:`fig:depthClipOverview`).

.. _fig:depthClipOverview:

.. figure:: pics/time_series_window_depths_clip.png
   :width: 100%

   The bottom plot displays the whole series in black.
   Clipped depth-layers are highlighted in color.




