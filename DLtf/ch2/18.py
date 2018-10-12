import numpy as np
Y = lb.fit_transform(Y)

array([[0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [1, 0, 0, 0, 0]])
Yp = model.predict(X[0])
array([[0.002, 0.991, 0.001, 0.005, 0.001]])
Ypr = np.round(Yp)
array([[ 0., 1., 0., 0., 0.]])
lb.inverse_transform(Ypr)
array(['Female'], dtype='|S6')
