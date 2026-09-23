.. _sec:BobImport:

Marine Magnetics BOB
====================

Surveys acquired using the Bob acquisition software will be present as a single file named ``CV_YY_NN_*.txt``, where YY denotes the year of the survey and NN the number of the survey and ``*`` denotes an arbitrary number unique for the survey.

Currently, the software has two assumptions on the ``CV_YY_NN_*.txt`` files.
First, a homogeneous number of columns within each file is expected since at the moment the software is not able to process files whose number of columns changes mid-file.

Second, the software assume the existence of the following columns names:
``Reading_Date,Reading_Time,Magnetic_Field,Longitude,Latitude,UTM_Easting,UTM_Northing``.
An example of the required format for a ``*.txt`` file to be successfully imported by the BOB-importer is provided in :numref:`lst:BobSnippet`.

.. _lst:BobSnippet:

.. literalinclude:: data/snippetBob.txt
   :language: text
   :caption: Preview of a raw Bob CSV file.
