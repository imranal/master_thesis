import sympy.abc as abc
symbols = ['*','/','(',')',"'",'"']
letters = []
def try_expr(expr):
    try:
        for letter in letters:
            exec('from sympy.abc import %s'%letter)  # re-execute after finding each unknown variable
        l = expr.count('(')
        r = expr.count(')')
        if l == r:  
            eval(expr)
        elif l < r:
            eval((r-l)*'('+expr)
    except NameError as err:
        msg = str(err)
        pos = msg.find("'")
        letter = msg[pos+1]
        pos = pos +1
        found = False
        while (pos+1 < len(msg)) and (not found):
            more = msg[pos+1]
            for symb in symbols:
                if more==symb or more.isdigit():
                    found = True
                    print msg
                    break
            if found is False:
                letter = letter+more       
                pos = pos + 1
        for alphabet in abc.__dict__:
            if letter == alphabet:
                letters.append(alphabet)
                try_expr(expr[expr.find(alphabet):]) # search for the next unknown variable

from sympy import sin, sqrt, log, exp, cos, tanh, sinh, cosh, atan, acos, asin
import sys
if len(sys.argv) == 1:
    expr = '(a**2*cos(v) + u**2)/(-2*G*M*u + a**2 + u**2)'#'(sin(x**2)-log(exp(2*y))/G) + cos(x**2) + a + b +c +theta*eta'
else:
    expr = sys.argv[1]
try_expr(expr)
for letter in letters:
    exec('from sympy.abc import %s'%letter)
print 'The SymPy expression %s contains the following letters : %s' %(eval('%s'%expr), letters)
