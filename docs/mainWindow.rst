MaxQuant.Live User Interface 
============================
The main window of MaxQuant.Live consists of three sections, which you can open by clicking on the symbols in the main menu.

Instrument 
----------

.. figure:: figures/image008.jpg
    :align: left
The instrument type can be selected here connected using the “connect instrument” button. 
In this ver-sion, only Thermo Fisher Scientific Q Exactive HF-X mass spectrometers are supported (Tune Version 2.9).

Main Module
-----------

.. figure:: figures/image010.jpg
    :align: left
This part of the software is the link between the instrument and the scan protocol Library. 
It consists of a log message window and the configuration of the log directory. 
It is recommended to always load the log directory before connecting the instrument.
The files written to this directory contain all log messages that were also shown in the graphical user interface. There are two types of log file written out by MaxQuant.Live 
Global log file: MaxQuant.Live will create global log files on every day. 
The filename is the date itself. These files contain all the log messages that were thrown when no scan protocol was running. 
Specific log files: During the execution of a scan protocol, the log messages are written to scan proto-col specific log file. The file name starts with the four-digit identification number, followed by the date and the time of execution. When the scan protocol ended, the log messages are again written into the global log file. 

Scan Protocol Library  
---------------------

.. figure:: figures/image014.jpg
    :align: left 
.. figure:: figures/image011.png
    :width: 250px
    :align: right    
Scan protocols implement various the acquisition strategies supported by our software. Every scan proto-col has a certain type (BoxCar, EasiTag…), a unique four-digit identification number and a short experiment description. All scan protocols are stored in a library. 
In the scan protocol section of the software you can manage the library. 
 
