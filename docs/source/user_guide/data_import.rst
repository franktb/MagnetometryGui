Data import
===========



Data can be imported through a file dialogue that could be opened within the drop-down menu ``File``.
Originally, the software was targeted at INFOMAR's magnetometry data acquired using Marine Magnetics' SeaLink and `Bob Survey Software <https://bob.marinemagnetics.com/>`_.
Therefore, we provide two custom imports that directly can process a majority of raw files created by either software.
For details on assumptions of the raw files we refer to section :ref:`sec:SeaLinkImport` and :ref:`sec:BobImport`.

Additionally, the software supports :ref:`sec:SensysImport` files, as well as a :ref:`sec:CustomImport` import where the user can specify the desired columns.

The imported surveys appear in a tree structure on the left-hand site of the main window (see \ref{fig:tree_import}).
Upon completion the imported surveys will appear in the file tree.


.. note::
   The import of large ``*.csv`` / ``*.txt`` or many ``*.XYZ`` files might take some time.



.. toctree::
   :maxdepth: 3

   sealink
   bob
   sensys
   custom_csv