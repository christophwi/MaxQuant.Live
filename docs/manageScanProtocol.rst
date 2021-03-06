Create and edit Scan Protocols
------------------------------

New scan protocol
""""""""""""""""""
.. image:: figures/AppStore.png
    :width: 250px
    :align: left

When you click on the “New” button, the app store opens. First, select the acquisition method that should be used in the new scan protocol.
Click on the big symbol to open the settings for the selected app. A green checkmark indicates which app has been selected.
Next, select a unique identification number for your scan protocol. The list in the drop-down menu excludes id numbers that are already present in the library.
Finally fill in a short description of the experiment and click create.
The scan protocol will be saved as file in the scan protocol folder and appear in the scan protocol library.

Edit scan protocols
""""""""""""""""""""
.. image:: figures/image017.png
    :width: 250px
    :align: right

Scan protocols in the library can be edited later by clicking the “Edit” button. It is possible to change the global properties like the ID number and the short description of the scan protocol. Furthermore, it is possible to edit the specific parameters of an acquisition strategy using the respective app. 

Copy and Delete
""""""""""""""""
Existing scan protocols can be easily copied by clicking the “Copy” button. 
The copy gets automatically an ID number assigned, is added to the library and can be edited afterwards by the user. 
Existing Scan Protocols can also be deleted by the user by clicking the “Delete” button.

Storage
"""""""
Scan protocols are saved as files (“.mqlive”) local library, which serves as scan protocol library. 
The path has to be set at when the software is started but can be changed after-wards during runtime. 
Therefore is it possible to use several scan protocol libraries for different experi-ments or users. 

Compatibility
"""""""""""""

Please note that every scan protocol has a version number, which is the version of the MaxQuant.Live that has been
used to create or edit it the last time. Compatibility is not guaranteed if the scan protocols and the MaxQuant.Live version differ.
Possibly incompatible scan protocols are highlighted in red and their settings should be checked carefully and saved
with the new version before running.

.. note:: MaxQuant.Live versions 0.99 and 1.2 are not fully compatible! Check your old scan protocols before running them.

Run scan protocol
""""""""""""""""""
Continue reading `here <runScanProtocol.html>`_
