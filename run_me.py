import pandas as pd
from functions import f_function, alpha, P1, Zk, dP1_dtheta, ddP1_ddtheta

df = pd.DataFrame(columns=['k', 'mu', 'Wt', 'Ct', 'J', 'f', 'alpha', 'theta' ]) # DataFrame used to gather the results.

# Default values for parameters:
Wt = 0 # The age of the wedding, set to default as the age at which the simulation starts
Ct = 0 # The age of brining children, set to default as the age at which the simulation starts + 1
J = 1 # Job capacity, default is 1.
theta = 0
mu = 1

for k in range(10): # Limit number of iterations by 10
  for i in range(10): # Run Steep Slope method, limit number of iterations by 10
    zk = - Zk(Wt, Ct, J, mu) # Calculate gradient
    for i in range(10): # Use Newton's method, limit number of iterations by 10
      dP1 = dP1_dtheta(Wt + theta * zk[0], Ct + theta * zk[1], J + theta * zk[2], mu) # Calculate first deriviative
      ddP1 = ddP1_ddtheta(Wt + theta * zk[0], Ct + theta * zk[1], J + theta * zk[2], mu) # Calculate second deriviative
      theta = theta + dP1 / ddP1 # Calculate Theta value
    Wt = min(Wt + theta * zk[0], 68) if Wt + theta * zk[0] > 19 else 18 # Get new Wt, limit by feasible range
    Ct = min(Ct + theta * zk[1], 68) if Ct + theta * zk[1] > 19 else 19 # Get new Ct, limit by feasible range
    J = min(J + theta * zk[2], 2) if J + theta * zk[2] > 0 else 1 # Get new J, limit by feasible range

  # Calculate the value's required for the dataframe
  f_value = f_function(Wt, Ct, J, mu)
  alpha_value = alpha(Wt, Ct, J)
  theta_value = P1(Wt, Ct, J, mu)

  df = df.append(pd.Series([k, mu, Wt, Ct, J, f_value, alpha_value, theta_value], index=df.columns), ignore_index=True) # Add the current state to the dataframe
  
  mu = mu * 10 # Increae Mu by tenfold

print('='*27+" Menny's Parents Presents "+'='*27) # Super-cool team SWAG
print(df) # RESULTS ARE IN!!!!
print('='*26+" Goren's Curiosity Lab Ltd. "+'='*26) # All rights reserved