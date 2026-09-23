.. _sec:SensysImport:

SENSYS
======


Surveys acquired using a SENSYS system will be present as a single file ``.csv`` file.


Second, the software assume the existence of the following columns names:
``Timestamp (s) UTC+0,Corrected Longitude (deg),Corrected Latitude (deg),Depth (m),Sensys MagX 1 (T),Sensys MagY 1 (T),Sensys MagZ 1 (T)``
SENSYS directly captures the vector components of the magnetic field.
To ensure consistency with the other data formats, the importer calculates the magnitude of the magnetic field from these components using the Euclidean norm:

.. math::

   \bar{B} = \sqrt{B_x^2 + B_y^2 + B_z^2}.

An example of the required format for a ``*.csv`` file to be successfully imported by the SENSYS-importer is provided in :numref:`lst:SensysSnippet`.

.. _lst:SensysSnippet:

.. literalinclude:: data/snippetSensys.txt
   :language: text
   :caption: Preview of a raw Sensys CSV file.
