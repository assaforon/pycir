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

 Confidence intervals for ordered Binomial, based on Morris 1988: recursive algorithm (not exported)


### The actual CI algorithms calling the Gupper,Glower utilities
 
def morrisUCL(y,n,halfa=None):
    
    y=np.asarray(y).copy()
    n=np.asarray(n).copy()
    m=len(y)
    if(len(n)!=m): stop("Mismatched lengths in Morris.\n")
    if halfa is None: halfa=0.05

    # weird prep...
    uout=np.repeat(1,m)
    a=m-1
    ### At uppermost doses as long as phat=1, no need for algorithms
    while(y[a]==n[a] && a>=0) a=a-1
    if(a<0) return(uout)
    
    for b in np.arange(a,0,-1):
    {
    	uout[b]=uniroot(function(theta,h,d,alpha,...) h(theta=theta,...)-alpha,interval=c(0,1),
    		alpha=halfa,j=b,h=Gupper,n=n,y=y)$root
    }
    return(uout)
    

def emptee(): pass