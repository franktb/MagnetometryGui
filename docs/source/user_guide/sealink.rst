.. _sec:SeaLinkImport:

Marine Magnetics SeaLink
========================

.. Workaround for RST being unable to render inline literals ending with a space.
   Directly inject "/ " as HTML.

.. |slash-space| raw:: html

   <code>/&nbsp;</code>

Surveys acquired using the Sealink acquisition software will be present as a folder named ``CV_YY_NN``, where YY denotes the year of the survey and NN the number of the survey.
The folder ``CV_YY_NN`` itself should contain a folder called ``raw``.
Inside the ``raw``-folder are several files sharing the same filename but differ in their ending such as ``*.txt``, ``*.mag``, ``*.XYZ``.
The software is looking for files ending with ``*.XYZ``.

To deal with the huge heterogeneity among SeaLink files the software assume a minimal standard of the imported files which will be outlined in the following.
This has to be ensured by the user or the custom csv-import (see \ref{sec:customCSVimport}) might be tried.

Currently, the software has two assumptions on the ``*.XYZ`` files.
First, a homogeneous number of columns within each file is expected since at the moment the software is not able to process files whose number of columns changes mid-file.

Second, the software assume the existence of the following columns names:
``/Date,Time,Field_Mag1,Longitude,Latitude``.
Note that due to Sealinks exported file structure the column name is ``/Date`` without a space.
Moreover, |slash-space| with a space is used to filter for mid-file headers, i.e. all lines starting with |slash-space|  will be ignored.

During the import, the Software will probe for ``UTM_Easting,UTM_Northing``.
If these columns are not present in the raw file they will be estimated form ``Longitude,Latitude``.
An example how a ``*.XYZ`` files is suppose to be formatted is given in :numref:`lst:SeaLinkSnippet`.

If both requirement are meet, the user can open a file dialogue through the dropdown menu ``File`` (see Fig.~\ref{fig:dropdown_import}).
Within the spawned file dialogue the user can select either directly the desired survey folder ``CV_YY_NN`` or its contained ``raw`` folder and all files matching the requirements above will be imported.

.. _lst:SeaLinkSnippet:

.. literalinclude:: data/snippetSealink.txt
   :language: text
   :caption: Preview of a raw SeaLink CSV file.
