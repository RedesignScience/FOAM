import pickle
import parmed
import os
import sys


def save_parmed_pickle(top, xyz, pickle_path):
    pmd = parmed.load_file(top, xyz)

    pmd_state = pmd.__getstate__()

    with open(pickle_path,'wb') as handle:
        pickle.dump(pmd_state,handle)


if __name__ == '__main__':
    if len(sys.argv[1:]) != 3:
        print("Usage: python save_parmed.py topology_file coordinate_file pickle_path")
    else:
        save_parmed_pickle(sys.argv[1],sys.argv[2],sys.argv[3])