import os
import h5py
from openfermion.hamiltonians import MolecularData
from openfermionpsi4 import run_psi4



def create_molecule(geometry, basisset, multiplicity, charge, description, moleculefilename):

    molecule = MolecularData(geometry, basis, multiplicity, charge, description, filename=moleculefilename)    
    # openfermion's run_psi4
    molecule = run_psi4(molecule, run_scf=1, run_mp2=1, run_cisd=0, run_ccsd=0, run_fci=0, verbose=1, tolerate_error=1)
    molecule.save()

    #return molecule