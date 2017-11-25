from pprint import pprint
import sys
import pickle
import rllab

data = pickle.load(open(sys.argv[1], 'rb'))

pprint(data)


