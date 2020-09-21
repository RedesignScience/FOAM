"""
This file holds the container for the foam file format.
"""
import os
import warnings
from mdtraj.formats.hdf5 import HDF5TrajectoryFile, _check_mode
import pickle
import parmed


class FOAMTrajectoryFile(HDF5TrajectoryFile):
    """
    This is the file object for the Foam Trajectory file (extension .ft).
    The class is based on the HDF5TrajectoryFile class from MDTraj, with added methods for easy to use access to
    additional storage of array like or non array like data.

    This class is created to address a drawback of the .h5 format in mdtraj, where even though the topology is stored
    with the trajectory, you still cannot initiate an MD simulation directly from the file and require parameterization
    tool. This drawback limited the usability in the setting for MSM adaptive sampling where restarting of simulation
    is common place.
    """

    def __init__(self, filename, mode='r', force_overwrite=True, compression='zlib'):
        super().__init__(filename, mode, force_overwrite, compression)

    @property
    def pmd(self):
        """Get the parmed object out from the file

        Returns
        -------
        topology : mdtraj.Topology
            A parmed.Structure() object
        """

        try:
            raw = self._get_node('/', name='parmed')[0]
            parmed_state = pickle.loads(raw)
        except self.tables.NoSuchNodeError:
            print("Warning: Parmed not set for this trajectory")
            return None

        pmd_obj = parmed.Structure()
        pmd_obj.__setstate__(parmed_state)

        return pmd_obj

    @pmd.setter
    def pmd(self, pmd_obj: parmed.Structure):
        _check_mode(self.mode, ('w', 'a'))

        try:
            self._remove_node(where='/', name='parmed')
        except self.tables.NoSuchNodeError:
            pass

        data = pickle.dumps(pmd_obj.__getstate__())

        if self.tables.__version__ >= '3.0.0':
            self._handle.create_array(where='/', name='parmed', obj=[data])
        else:
            self._handle.createArray(where='/', name='parmed', object=[data])
