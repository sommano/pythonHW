import scipy.linalg as sl
class PolyNomial:
 base='monomial'
 def __init__(self,**args):
 if 'points' in args:
 self.points = array(args['points'])
 self.xi = self.points[:,0]
 self.coeff = self.point_2_coeff()
 self.degree = len(self.coeff)-1
 elif 'coeff' in args:
 self.coeff = array(args['coeff'])
 self.degree = len(self.coeff)-1
 self.points = self.coeff_2_point()
 else:
 self.points = array([[0,0]])
 self.xi = array([1.])
 self.coeff = self.point_2_coeff()
 self.degree = 0
