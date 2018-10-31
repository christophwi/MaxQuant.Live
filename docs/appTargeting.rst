Targeting
=========
The Targeting app allows the realization of various targeting strategies within on user interface.
First, the list of targeting peptides has to be populated and afterward the targeting strategy has 
to be defined and the parameters have to be set. 

Quick start guide
-----------------

1. Populate the peptide list (Sec. 7.3.1)
2. Set up targeting action (Sec. 7.3.2)
3. Set global parameters(Sec. 7.3.2)

Peptide list
------------
The targeting should comprise a set of peptides of interest and a set of high abundant peptides used for the 
real-time corrections of mass-to-charge values, expected retention times and peptide intensities. 
In order to get a reliable correction around 100 correction peptides per minute of the gradient is recommended.
If the set of targeting peptides is large enough, it is sufficient to only use them as correction peptides.

+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Method parameter   | Description                                                                   |                                               |
+====================+===============================================================================+===============================================+
| Id                 | Identification number used in log messages                                    | optional                                      |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Modified sequence  | String containing the modified sequence                                       | optional; Needed if isotopic labeling is used |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Mass               | Ion mass                                                                      | mandatory                                     |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Charge             | Ion charge state                                                              | mandatory                                     |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Retention time     | Expected retention time (min)                                                 | mandatory                                     |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Retention length   | Expected elution time (min)                                                   | mandatory but can be set to 1.0               |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Intensity          | Expected intensity                                                            | mandatory but can be set to 1.0               |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| Collision Energies | Collision energies for fragmentation (white space separated: 11 21            | optional; if empty the global NCE is used     |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+
| NCE                | List of NCE scaling factor for fragmentation (white space separated: 1.2 2.3) | optional;                                     |
+--------------------+-------------------------------------------------------------------------------+-----------------------------------------------+


