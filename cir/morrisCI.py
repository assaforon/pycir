# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import pandas as pd
from scipy.stats import binom

### Morris and Morris-style CI: functions and accessories

# First evaluation functions used by recursive algorithm 
# This is G(t_j,theta_j) in Morris (1988) equation (4.3), with typo correction

def Gupper(theta,y,n,j):
    y=np.asarray(y).copy()
    n=np.asarray(n).copy()
    
    if(j==len(y)-1): return (binom.cdf(k=y[j],n=n[j],p=theta))
    
    return (binom.cdf(k=y[j]-1,n=n[j],p=theta)+binom.pmf(k=y[j],n=n[j],p=theta)*Gupper(theta=theta,y=y,n=n,j=j+1))
    ## The typo in Morris (88) is the use of G_{j+1} rather than G_j throughout

def Glower(theta,y,n,j):
    y=np.asarray(y).copy()
    n=np.asarray(n).copy()
    
    if(j==0): return (binom.sf(k=y[j]-1,n=n[j],p=theta))
    
    return (binom.sf(k=y[j],n=n[j],p=theta)+binom.pmf(k=y[j],n=n[j],p=theta)*Glower(theta=theta,y=y,n=n,j=j-1))



def emptee(): pass