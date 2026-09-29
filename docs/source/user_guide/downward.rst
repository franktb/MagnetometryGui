.. _sec:DownwardOverview:

Downward continuation
=====================

The Downward-Window is a wrapper around the downward integral

.. Todo:Reference!!!
.. math::

   U(x,y,\Delta z)    = \frac{-\Delta z}{2\pi} \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} \frac{U(x', y', z_0)}{\left[(x-x')^2+(y-y')^2+\Delta  z^2\right]^{3/2}} dx' dy',

which calculates based on a 2D-measured magnetic field the 2D field for a given distance :math:`\Delta z`.

.. Todo:Expand theory!!!

Using the transformation for positive :math:`z` is a smoothing operation and stable and therefore no problem.
However for negative :math:`z` the operation becomes a ill-posed problem due to :math:`e^{-\Delta z \sqrt{u^2+v^2}}` and the integral numerical very unstable.


.. toctree::
   :maxdepth: 3

   downward_layer
   downward_bath
   downward_export