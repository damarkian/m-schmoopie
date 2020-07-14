import os
import h5py
from openfermion.hamiltonians import MolecularData
from openfermionpsi4 import run_psi4

def make_geometry():
    # boilerplate

    geometry = [
                ['H', [0.0, 0.0, 0.0]], 
                ['H', [0.0, 0.0, 0.8]]
               ]

    return geometry

def create_molecule():

    geometry = make_geometry()
    basis = 'sto-3g'
    charge = 0
    multiplicity = 1

    filename = '/app/moleculedata.hdf5'

    molecule = MolecularData(geometry, basis, multiplicity, charge, description, filename=filename)
    
    # openfermion's run_psi4
    molecule = run_psi4(molecule, run_scf=1, run_mp2=1, run_cisd=0, run_ccsd=0, run_fci=0, verbose=1, tolerate_error=1)
    molecule.save()
    
    #return molecule