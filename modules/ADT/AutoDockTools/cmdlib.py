cmdlist = [
("AutoDockTools","autoanalyzeCommands","ADanalyze_readDLG","""allows the user to select a filename for the docking log"""),
("AutoDockTools","autoanalyzeCommands","ADanalyze_deleteDLG","""allows the user to delete docking """),
("AutoDockTools","autoanalyzeCommands","ADanalyze_selectDLG","""allows the user to change current docking """),
("AutoDockTools","autoanalyzeCommands","ADanalyze_chooseDockedConformations",""""""),
("AutoDockTools","autoanalyzeCommands","ADanalyze_readMacromolecule","""this class is used to load the macromolecule specified in the docking log"""),
#("AutoDockTools","autoanalyzeCommands","ADanalyze_showHistogram",""""""),
("AutoDockTools","autoanalyzeCommands","ADanalyze_readAllDLGInDirectory","""allows the user to read all the docking logs in a chosen directory"""),
#("AutoDockTools","autoanalyzeCommands","ADanalyze_getChart",""""""),
#("AutoDockTools","autoanalyzeCommands","ADanalyze_showResultsOutput","""When the docking log is parsed, summary lines are detected and saved in  """),
("AutoDockTools","autoanalyzeCommands","ADanalyze_showGridIsocontours",""" toplevel GUI with one row per grid_type allowing: \n            loading a grid (first, then->),  \n            toggling the visiblity of its isosurface,\n            changing sampling rate, \n            changing isocontour isovalue,\n            changing the render mode between LINE and FILL\n            visibility of the grid's bounding box\n    """),
("AutoDockTools","autoanalyzeCommands","ADanalyze_addExtraGridIsocontour",""" adds a row to the toplevel GUI of ADMakeAllGrids enabling:\n            loading a USER grid (first, then->),  \n            toggling its visiblity,\n            changing sampling rate, \n            changing isocontour value,\n            changing the render mode between lines and fill\n    """),
("AutoDockTools","autodpfCommands","ADdpf_setDpo",""""""),
("AutoDockTools","autodpfCommands","ADdpf_read",""" allows user to select a file containing a set of defaults"""),
("AutoDockTools","autodpfCommands","ADdpf_chooseMacromolecule",""" allows user to choose a molecule already present for the macromolecule"""),
("AutoDockTools","autodpfCommands","ADdpf_readMacromolecule",""" allows user to select a filename for the macromolecule"""),
("AutoDockTools","autodpfCommands","ADdpf_chooseFormattedLigand",""" allows user to choose a molecule already present for the ligand"""),
("AutoDockTools","autodpfCommands","ADdpf_readFormattedLigand",""" allows user to choose a PDBQ file for the ligand"""),
("AutoDockTools","autodpfCommands","ADdpf_initLigand","""initializes the ligand"""),
("AutoDockTools","autodpfCommands","ADdpf_setSAparameters",""" allows user to set necessary parameters for simulated annealing-based autodock job"""),
("AutoDockTools","autodpfCommands","ADdpf_setGAparameters",""" allows user to set necessary parameters for genetic algorithm-based autodock job"""),
("AutoDockTools","autodpfCommands","ADdpf_setLSparameters",""" allows user to set necessary parameters for local search-based autodock job"""),
("AutoDockTools","autodpfCommands","ADdpf_setDockingParameters",""" allows user to set these parameters for  autodock job: step sizes, energy parameters and format for the output"""),
("AutoDockTools","autodpfCommands","ADdpf_writeSA",""" allows user to choose an output filename and write simulated annealing parameters"""),
("AutoDockTools","autodpfCommands","ADdpf_writeGA",""" allows user to choose an output filename and write it"""),
("AutoDockTools","autodpfCommands","ADdpf_writeLS",""" allows user to choose an output filename and write it"""),
("AutoDockTools","autodpfCommands","ADdpf_writeGALS",""" allows user to choose an output filename and write it"""),
("AutoDockTools","autodpfCommands","ADdpf_writeCluster",""" allows user to write a dpf to cluster many dockings """),
("AutoDockTools","autodpfCommands","ADdpf_edit",""" allows user to edit current output file and write it"""),
("AutoDockTools","autogpfCommands","ADgpf_setGpo",""" Command to set values in gpo object using gui input results"""),
("AutoDockTools","autogpfCommands","ADgpf_initLigand","""initializes the ligand:\n        checkCharges\n        getTypes\n        getSideLengths\n        setAutoDockElements\n        colorByAtom + color aromatic C's green\n        \n        GUI allows user to:\n            decide which types of hydrogen bonds to model\n            modify list of atom types detected in ligand\n        \n        """),
("AutoDockTools","autogpfCommands","ADgpf_initMacro","""receptor is initialized as specified in parameters:\n            autodock_element field added\n            charges may be added (either Kollman or Gasteiger)\n            charges are checked\n            lone pairs merged\n            non-polarhydrogens merged\n            macro sidelengths set\n            types of atoms in receptor added as '.mset'\n                possibility of adding new atom types to Rij/epsij dicts\n            solvation parameter fields are added: AtVol + AtSolPar\n                which is written to newfilename if specified \n                otherwise to mol.name+'.pdbqs'\n            receptor is colored by Atom Type"""),
("AutoDockTools","autogpfCommands","ADgpf_checkMacroTypes","""detect types of atoms in receptor; \n        \n       for non-standard types (limited to 2:'X' and 'M'):\n            define new energy parameters: \n                Rij and epsij\n            write file substituting X or M for non-standard element """),
("AutoDockTools","autogpfCommands","ADgpf_chooseMacromolecule",""" allows user to choose a molecule already present for the receptor"""),
("AutoDockTools","autogpfCommands","ADgpf_readMacromolecule",""" allows user to select the receptor via a file browser"""),
("AutoDockTools","autogpfCommands","ADgpf_mergeNonPolarHydrogens",""""""),
("AutoDockTools","autogpfCommands","ADgpf_addSolvationParameters",""" allows user to add solvation parameters to a receptor """),
("AutoDockTools","autogpfCommands","ADgpf_setMapTypes",""" allows user to enter types of maps to be calculated, directly"""),
("AutoDockTools","autogpfCommands","ADgpf_chooseFormattedLigand",""" allows user to choose a molecule already present for the ligand"""),
("AutoDockTools","autogpfCommands","ADgpf_readFormattedLigand",""" allows user to choose a ligand file via a file browser"""),
("AutoDockTools","autogpfCommands","ADgpf_defineAtomParameters",""""""),
("AutoDockTools","autogpfCommands","ADgpf_setUpCovalentMap",""""""),
("AutoDockTools","autogpfCommands","ADgpf_setGrid",""" allows user to set center, spacing, and extent of \n        grids (number of pts in each dimension) to be calculated"""),
("AutoDockTools","autogpfCommands","ADgpf_setOtherOptions",""" allows user to set smooth factor, whether to calculate\n        floating point and electrostatic maps AND whether to \n        use a constant or a distance-dependent dielectric constant"""),
("AutoDockTools","autogpfCommands","ADgpf_writeGPF",""" allows user to choose an output filename and write it"""),
("AutoDockTools","autogpfCommands","ADgpf_editGPF",""" allows user to edit current output file and write it"""),
("AutoDockTools","autogpfCommands","ADgpf_readGPF",""" allows user to select a file containing a set of defaults"""),
("AutoDockTools","autogpfCommands","ADgpf_selectCenter",""" allows user to pick an atom to be the center of the grid"""),
("AutoDockTools","autostartCommands","ADstart_autogrid","""Interactive usage: \n            The user chooses host and parameter file and starts the Autogrid job. \n            If the host has an interactive queue, launching the job opens \n            a 'ADstart_manage' widget which allows the user to follow the job \n            and to kill it, if necesary. A 'job file' is written when a parameter \n            file is selected in combination with the selection of a 'nqe'-type host.\n        Scripting usage:\n            'doIntRemoteCommand' and 'doNqeRemoteCommand' methods allow starting \n            AutoGrid with the specified parameter file on a host with\n            a appropriate queue type. (if not specified, host is assumed\n            to be the local host and must be of appropriate queue type).\n            All other parameters are optional"""),
("AutoDockTools","autostartCommands","ADstart_autodock","""Interactive usage: \n            The user chooses host and parameter file and starts the Autodock job. \n            If the host has an interactive queue, launching the job opens \n            a 'ADstart_manage' widget which allows the user to follow the job \n            and to kill it, if necesary. A 'job file' is written when a parameter \n            file is selected in combination with the selection of a 'nqe'-type host.\n        Scripting usage:\n            'doIntRemoteCommand' and 'doNqeRemoteCommand' methods allow starting \n            Autodock with the specified parameter file on a host with\n            a appropriate queue type. (if not specified, host is assumed\n            to be the local host and must be of appropriate queue type).\n            All other parameters are optional"""),
("AutoDockTools","autostartCommands","ADstart_manage",""""""),
("AutoDockTools","autostartCommands","ADstart_editHostMacros",""" this class allows user to add entries to hosts dictionary \n        and write them to a file"""),
("AutoDockTools","autotorsCommands","ADtors_readLigand","""allows user to select a file for the ligand via a file browser"""),
("AutoDockTools","autotorsCommands","ADtors_chooseLigand","""allows user to choose as ligand  a molecule already in the viewer"""),
("AutoDockTools","autotorsCommands","ADtors_rigidLigand","""allows user to write molecule with ROOT, ENDROOT + TORSDOF 0 added"""),
("AutoDockTools","autotorsCommands","ADtors_setRoot","""allows user to pick an atom to be ROOT, the rigid portion \n    of ligand which has rotatable BRANCHES """),
("AutoDockTools","autotorsCommands","ADtors_autoRoot","""causes program to pick an atom to be ROOT: the one which has\nthe smallest 'largest sub-tree'"""),
("AutoDockTools","autotorsCommands","ADtors_markRoot","""shows current extent of root portion of the molecule:it includes all contiguous atoms starting with those adjacent to the designated root atom out to first active torsion """),
("AutoDockTools","autotorsCommands","ADtors_defineRotBonds",""" """),
("AutoDockTools","autotorsCommands","ADtors_setBondRotatableFlag","""set the flag that tells whether a bond is rotatable in aan AutoDock\n    ligand"""),
#("AutoDockTools","autotorsCommands","ADtors_changePlanarCarbonsToA","""checks rings for planarity and changes carbons in planar rings to\nelement type and name: 'A'"""),
#("AutoDockTools","autotorsCommands","ADtors_changeAromaticCarbonsToC","""restores carbons in aromatic rings to element type 'C' and name: 'C...'"""),
("AutoDockTools","autotorsCommands","ADtors_setCarbonNames","""toggles Carbon names between 'A' + 'C'"""),
("AutoDockTools","autotorsCommands","ADtors_changePlanarityCriteria","""allows user to change requirement for aromaticity of cycles:\ndefault is < 5 degrees between normals to adjacent atoms.  User enters a new angle in degrees"""),
("AutoDockTools","autotorsCommands","ADtors_mergeNonPolarHydrogens","""merges non-polar hydrogen atoms w/ their carbons"""),
("AutoDockTools","autotorsCommands","ADtors_restoreMergedNonPolarHydrogens","""restores non-polar hydrogen atoms and their charges"""),
("AutoDockTools","autotorsCommands","ADtors_writeFormattedPDBQ","""allows user to select and write an output file for the formatted ligand"""),
("AutoDockTools","autotorsCommands","ADtors_showRootSphere","""lets user toggle rootSph visibility"""),
("AutoDockTools","autotorsCommands","ADtors_automaticLigandFormatting","""preforms default actions on designated molecule"""),
]
