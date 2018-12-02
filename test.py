## -*- coding: utf-8 -*-
import pickle
import numpy as np
#train =[]

with open("dictionary.pkl", "rb") as f:
	base = []
	try:

		while True:
			base.append(pickle.load(f))

	except (EOFError, pickle.UnpicklingError):
		pass
#train =np.zeros(len(base))

train  = [[0] * 2 for i in range(len(base))]


for i in range(len(base) ):
    train[i]=base[i][1:3]
print train
