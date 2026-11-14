from mpi4py import MPI

from pytimewarp.engine import Engine

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class Conservative(Engine):
    pass
