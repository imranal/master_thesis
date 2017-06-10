from sympy.diffgeom import Manifold, Patch, CoordSystem, TensorProduct
from sympy import sin, trigsimp, simplify
from sympy.abc import r
from sympy.diffgeom import metric_to_Riemann_components

dim = 2
m = Manifold("M",dim)
patch = Patch("P",m)

cartesian = CoordSystem("cartesian",patch, ["x", "y"])
flat_sphere = CoordSystem("flat_sphere", patch, ["theta", "phi"])

x, y = cartesian.coord_functions()
theta, phi = flat_sphere.coord_functions()
dtheta,dphi = flat_sphere.base_oneforms()

metric_diff_form = r**2*TensorProduct(dtheta, dtheta) + r**2*sin(theta)**2*TensorProduct(dphi, dphi)
R = metric_to_Riemann_components(metric_diff_form)

def tuple_to_list(t):
    return list(map(tuple_to_list, t)) if isinstance(t, (list, tuple)) else t
simpR = tuple_to_list(R)
for m in range(dim):
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                expr = str(R[m][i][j][k])
                expr = trigsimp(expr)
                expr = simplify(expr)
                simpR[m][i][j][k] = expr

# Find the Ricci tensor
from sympy.diffgeom import metric_to_Ricci_components
RR = metric_to_Ricci_components(metric_diff_form)
simpRR = tuple_to_list(RR)
for m in range(dim):
    for i in range(dim):
        expr = str(RR[m][i])
        expr = trigsimp(expr)
        expr = simplify(expr)
        simpRR[m][i] = expr
print simpR, simpRR
