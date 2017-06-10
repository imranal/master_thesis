import find_metric as fm
g = fm.kerr_metric()
import tensor as t
R = t.Riemann(g,'kerr_metric',4)
RC = R.Christoffel_tensor()
RR = R.Ricci_tensor()
scalarRR = R.scalar_curvature()

print "\nThe Kerr curve element has the following metric"
print g
print "\nThe Ricci tensor is given as"
print RR
print "\nand the scalar curvature is"
print scalarRR 
