import math
import numpy as np

S = 50000 # Yearly Salary in $
K = S * 0.163 # Expenses on children
L = S * 0.03 # Expenses on loved one
delta = 4 # Joycoin gained for each year of bachelorship
epsilon = 1 # Parameter used to transfer the type of units, negligable in the calculation, but added here for consistency.


def g(Wt):
  # We took apart this function in order to improve readability & prevent code repetition.
  ln_Wt_minus_68_divide_2 = math.log( - (Wt - 68) / 2 )
  sin_ln = math.sin(ln_Wt_minus_68_divide_2)
  cos_ln = math.cos(ln_Wt_minus_68_divide_2)

  g1 = 10 * math.sin( (7 * Wt - 462) / 10 )
  g2 = - sin_ln
  g3 = cos_ln
  g4 = 68 * sin_ln
  g5 = 68 * cos_ln
  return - ( (g1 + g2 + g3 + g4 + 6) * Wt + g4 - g5 - 394 ) / 2

def dg(Wt):
  # Return the derivative of g by Wt
  g1 = 7 * math.cos( (7 * Wt - 462) / 10 )
  g2 = 2 * math.sin( math.log( - (Wt - 68) / 2 ) )
  return - (g1 - g2 + 6) / 2

def ddg(Wt):
  # Return the derivative of g by Wt**2
  g1 = 49 * Wt - 3332
  g2 = math.sin( (7 * Wt - 462) / 10 )
  g3 = 20 * math.cos( math.log( - (Wt - 68) / 2 ) )
  g4 = 20 * Wt - 1360
  return (g1 * g2 + g3) / g4

def cross_dg(Wt):
  # This function returns the derivative of g by:
  # WtCt, WtJ, Ct, Ct**2, CtWt, CtJ, J, J**2
  # Which are all equal to 0.
  return 0

def f(Ct):
  # We took apart this function in order to improve readability & prevent code repetition.
  f5 = 12 * Ct**5
  f4 = 2955 * Ct**4
  f3 = 274600 * Ct**3
  f2 = 11773440 * Ct**2
  f1 = 221739840 * Ct
  f0 = 1253772432
  return (f5 - f4 + f3 - f2 + f1 - f0) / 600000

def df(Ct):
  # Return the derivative of f by Ct
  f4 = Ct**4
  f3 = 197 * Ct**3
  f2 = 13730 * Ct**2
  f1 = 392448 * Ct
  f0 = 3695664
  return (f4 - f3 + f2 - f1 + f0) / 10000

def ddf(Ct):
  # Return the derivative of f by Ct**2
  f3 = 4 * Ct**3
  f2 = 591 * Ct**2
  f1 = 27460 * Ct
  f0 = 392448
  return (f3 + f2 - f1 + f0) / 10000

def cross_df(Ct):
  # This function returns the derivative of f by:
  # CtWt, JCt, CtJ, Wt, Wt**2, JWt, WtJ, J, J**2
  # Which are all equal to 0.
  return 0

def h(Wt):
  return delta * (Wt - 18)

def dh(Wt):
  # Return the derivative of h by Wt
  return delta

def ddh(Wt):
  # Returns the double derivative of h by every kind of combination
  return 0

def cross_dh(Wt):
  # Returns the derivative of h by other variable
  return 0

def U(J):
  return 480 * J - 240 * J**3

def dU(J):
  # Return the derivative of U by J
  return 480 - 720 * J**2

def ddU(J):
  # Returns the double derivative of U by J
  return - 1440 * J

def cross_dU(J):
  # Returns the derivative of U by other variable
  return 0

def y(Wt, Ct, J):
  y1 = ( (48 * J * S - (66 - Wt) * L - (66 - Ct) * K) / 48 ) + 1
  return 120 * epsilon * math.log(y1)

def dy_dWt(Wt, Ct, J):
  # Return the derivative of y by Wt
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return 120 * epsilon * L / y1

def dy_dCt(Wt, Ct, J):
  # Return the derivative of y by Ct
  y1 = (48 * J * S - (66 - Wt) * L - (66 - Ct) * K) / 48 + 1
  return 5 * epsilon * K / ( 2 * y1 )

def dy_dJ(Wt, Ct, J):
  # Return the derivative of y by J
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return 5760 * epsilon * S / y1

def dy_ddWt(Wt, Ct, J):
  # Return the double derivative of y by Wt
  y1 = (L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48)**2
  return - 120 * epsilon * L**2 / y1

def dy_ddCt(Wt, Ct, J):
  # Return the double derivative of y by Ct
  y1 = 96 * ( (48 * J * S - (66 - Wt) * L - (66 - Ct) * K) / 48 + 1 )**2
  return - 5 * epsilon * K**2 / ( 2 * y1 )

def dy_ddJ(Wt, Ct, J):
  # Return the double derivative of y by J
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return - 276480 * epsilon * S / y1**2

def dy_dWtdCt(Wt, Ct, J):
  # Return the derivative of y by Wt and then by Ct
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return - 120 * epsilon * K * L / y1**2

def dy_dWtdJ(Wt, Ct, J):
  # Return the derivative of y by Wt and then by J
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return - 5760 * epsilon * L * S / y1**2

def dy_dCtdJ(Wt, Ct, J):
  # Return the derivative of y by Wt and then by J
  y1 = L * Wt + 48 * J * S - 66 * L + (Ct - 66) * K + 48
  return - 5760 * epsilon * K * S / y1**2

def f_function(Wt, Ct, J, mu):
  return - ( g(Wt) + f(Ct) + h(Wt) + U(J) + y(Wt, Ct, J) )

def N1(Wt, Ct, J):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  return max(0, n1)**4

def dN1_dWt(Wt, Ct, J):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  if n1 < 0:
    return 0
  return - 4 * L * ( (66 - Wt) * L + (66 - Ct) * K - 48 * J * S )**3

def dN1_dCt(Wt, Ct, J):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  if n1 < 0:
    return 0
  return - 4 * K * ( (66 - Wt) * L + (66 - Ct) * K - 48 * J * S )**3

def dN1_dJ(Wt, Ct, J):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  if n1 < 0:
    return 0
  return - 192 * S * ( (66 - Wt) * L + (66 - Ct) * K - 48 * J * S )**3

def N2(Wt, Ct):
  n2 = Wt - Ct + 1
  return max(0, n2)**4

def dN2_dWt(Wt, Ct):
  n2 = Wt - Ct + 1
  if n2 < 0:
    return 0
  return 4 * n2**3

def dN2_dCt(Wt, Ct):
  n2 = Wt - Ct + 1
  if n2 < 0:
    return 0
  return - 4 * n2**3

def dN2_dJ(Wt, Ct):
  return 0

def alpha(Wt, Ct, J):
  return N1(Wt, Ct, J) + N2(Wt, Ct)

def dalpha_dWt(Wt, Ct, J):
  return dN1_dWt(Wt, Ct, J) + dN2_dWt(Wt, Ct)

def dalpha_dCt(Wt, Ct, J):
  return dN1_dCt(Wt, Ct, J) + dN2_dCt(Wt, Ct)

def dalpha_dJ(Wt, Ct, J):
  return dN1_dJ(Wt, Ct, J) + dN2_dJ(Wt, Ct)

def P1(Wt, Ct, J, mu):
  return - ( g(Wt) + f(Ct) + h(Wt) + U(J) + y(Wt, Ct, J) ) + mu * alpha(Wt, Ct, J)

def dP1_dWt(Wt, Ct, J, mu):
  return - ( dg(Wt) + cross_df(Ct) + dh(Wt) + cross_dU(J) + dy_dWt(Wt, Ct, J) ) + mu * dalpha_dWt(Wt, Ct, J)

def dP1_dCt(Wt, Ct, J, mu):
  return - ( cross_dg(Wt) + df(Ct) + cross_dh(Wt) + cross_dU(J) + dy_dCt(Wt, Ct, J) ) + mu * dalpha_dCt(Wt, Ct, J)

def dP1_dJ(Wt, Ct, J, mu):
  return - ( dg(Wt) + cross_df(Ct) + cross_dh(Wt) + dU(J) + dy_dCt(Wt, Ct, J) ) + mu * dalpha_dJ(Wt, Ct, J)

def Zk(Wt, Ct, J, mu):
  return np.array([ dP1_dWt(Wt, Ct, J, mu), dP1_dCt(Wt, Ct, J, mu), dP1_dJ(Wt, Ct, J, mu) ])

def V1(Wt, Ct, J, mu):
  # This function is used only in order to reserve the same names as presented in the paper.
  return dP1_dWt(Wt, Ct, J, mu)

def V2(Wt, Ct, J, mu):
  # This function is used only in order to reserve the same names as presented in the paper.
  return dP1_dCt(Wt, Ct, J, mu)

def V3(Wt, Ct, J, mu):
  # This function is used only in order to reserve the same names as presented in the paper.
  return dP1_dJ(Wt, Ct, J, mu)

def dg_dtheta(Wt, Ct, J, mu):
  v1 = V1(Wt, Ct, J, mu)
  g0 = 2 * math.sin( math.log( (- Wt + 68 ) / 2 ) )
  g1 = 7 * math.cos( ( 7 * Wt - 462) / 10 )
  return v1 / 2 * ( 2 * ( g0 - g1 - 6 ) )

def ddg_ddtheta(Wt, Ct, J, mu):
  v1 = V1(Wt, Ct, J, mu)
  g0 = 49 * v1 * math.sin( ( 7 * Wt - 462) / 10 )/ 10
  g1 = 2 * v1 * math.cos( math.log( (- Wt + 68 ) / 2 ) ) / ( - Wt + 68 )
  return v1 / 2 * ( 2 * ( g0 - g1 ) )

def df_dtheta(Wt, Ct, J, mu):
  v2 = V2(Wt, Ct, J, mu)
  f4 = 60 * v2 * Ct**4
  f3 = 11820 * v2 * Ct**3
  f2 = 823800 * v2 * Ct**2
  f1 = 23546880 * v2 * Ct**1
  f0 = 221739840 * v2
  return ( f4 - f3 + f2 - f1 + f0 ) / 600000

def ddf_ddtheta(Wt, Ct, J, mu):
  v2 = V2(Wt, Ct, J, mu)
  f3 = 240 * v2**2 * Ct**3
  f2 = 35460 * v2**2 * Ct**2
  f1 = 1647600 * v2**2 * Ct**1
  f0 = 23546880 * v2**2
  return ( f3 - f2 + f1 - f0 ) / 600000

def dh_dtheta(Wt, Ct, J, mu):
  return delta * V1(Wt, Ct, J, mu)

def ddh_ddtheta(Wt, Ct, J, mu):
  return 0

def dU_dtheta(Wt, Ct, J, mu):
  v3 = V3(Wt, Ct, J, mu)
  return 480 * v3 - 720 * v3 * J**2

def ddU_ddtheta(Wt, Ct, J, mu):
  v3 = V3(Wt, Ct, J, mu)
  return - 1440 * v3**2 * J

def dy_dtheta(Wt, Ct, J, mu):
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  v3 = V3(Wt, Ct, J, mu)
  y0 = 48 * S * v3 + K * v2 + L * v1
  y1 = 48 * S * J + K * ( Ct - 66 ) - L * ( - Wt + 66 )
  return ( 5 * epsilon * y0 ) / ( 2 * ( y1 / 48 + 1 ) )

def ddy_ddtheta(Wt, Ct, J, mu):
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  v3 = V3(Wt, Ct, J, mu)
  y0 = 48 * S * v3 + K * v2 + L * v1
  y1 = 48 * S * J + K * ( Ct - 66 ) - L * ( - Wt + 66 )
  return - ( 5 * epsilon * y0**2 ) / ( 96 * ( y1 / 48 + 1 ) )

def dN1_dtheta(Wt, Ct, J, mu):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  if n1 < 0:
    return 0
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  v3 = V3(Wt, Ct, J, mu)
  n0 = - 48 * S * v3 - K * v2 - L * v1
  n1 = ( 65 - Wt + 1 ) * L + ( 65 - Ct + 1 ) * K - 48 * J * S
  return 4 * n0 * n1**3

def ddN1_ddtheta(Wt, Ct, J, mu):
  n1 = (65 - Wt + 1) * L + (65 - Ct + 1) * K - 48 * J * S
  if n1 < 0:
    return 0
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  v3 = V3(Wt, Ct, J, mu)
  n0 = - 48 * S * v3 - K * v2 - L * v1
  n1 = ( 65 - Wt + 1 ) * L + ( 65 - Ct + 1 ) * K - 48 * J * S
  return 12 * n0**2 * n1**2

def dN2_dtheta(Wt, Ct, J, mu):
  n2 = Wt - Ct + 1
  if n2 < 0:
    return 0
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  n0 = v1 - v2
  n1 = Wt - Ct + 1
  return 4 * n0 * n1**3

def ddN2_ddtheta(Wt, Ct, J, mu):
  n2 = Wt - Ct + 1
  if n2 < 0:
    return 0
  v1 = V1(Wt, Ct, J, mu)
  v2 = V2(Wt, Ct, J, mu)
  n0 = v1 - v2
  n1 = Wt - Ct + 1
  return 12 * n0**2 * n1**2

def dalpha_dtheta(Wt, Ct, J, mu):
  return dN1_dtheta(Wt, Ct, J, mu) + dN2_dtheta(Wt, Ct, J, mu)

def ddalpha_ddtheta(Wt, Ct, J, mu):
  return ddN1_ddtheta(Wt, Ct, J, mu) + ddN2_ddtheta(Wt, Ct, J, mu)

def dP1_dtheta(Wt, Ct, J, mu):
  p1 = dg_dtheta(Wt, Ct, J, mu) + df_dtheta(Wt, Ct, J, mu) + dh_dtheta(Wt, Ct, J, mu) + dU_dtheta(Wt, Ct, J, mu) + dy_dtheta(Wt, Ct, J, mu)
  p2 = mu * dalpha_dtheta(Wt, Ct, J, mu)
  return - p1 + p2

def ddP1_ddtheta(Wt, Ct, J, mu):
  p1 = ddg_ddtheta(Wt, Ct, J, mu) + ddf_ddtheta(Wt, Ct, J, mu) + ddh_ddtheta(Wt, Ct, J, mu) + ddU_ddtheta(Wt, Ct, J, mu) + ddy_ddtheta(Wt, Ct, J, mu)
  p2 = mu * ddalpha_ddtheta(Wt, Ct, J, mu)
  return - p1 + p2