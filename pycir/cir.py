# -*- coding: utf-8 -*-
"""
Centered isotonic regression, generic but more tailored to dose-response and dose-finding data

Assaf Oron, recoded from R 'cir' package
"""

import numpy as np
import pandas as pd


def cirPAVA(y, x=None, wt=None, outx=None, interiorStrict=True, strict=False, ybounds=None, full=False, dec=False):
    """
    Perform regression.

    Args:
        x,y,wt: vectors of equal length with the doses, mean y values (usually response rates in [0,1]), and weights (often sample size)
        outx: ...
    """
    if ybounds is None:
        ybounds = np.asarray([0.0,1.0])

    y = np.asarray(y)
    if y.ndim != 1:
        raise Exception(f'You supplied an array with {y.ndim} dimensions, but must be a vector (i.e. 1 dimension)')

    m = len(y)
    dr = pd.DataFrame(data={'x':x,'y':y, 'weight':wt})
#    if (m <= 1):  ## degenerate case: only one dose level
#        if (not(full)): return (dr.y)
#        return(['output':dr,'input':dr,'shrinkage':dr])

    if outx is None:
        outx = dr.x
    else:
        outx = np.asarray(outx)

    dr0 = dr.copy()
    if dec:
        dr.loc['y'] = -dr.y

    while True:
        viol = np.diff(dr.y)<0
        # This option (default True) makes sure 0s and 1s are not swept into
        # The shrinkage (in case of binary/binomial observations)
        if interiorStrict:
            equals = np.diff(dr.y)==0
            for i in range(0,m-1):
                if dr.y[i] in ybounds and dr.y[i+1] in ybounds:
                    equals[i] = False
            viol = (viol | equals)

        # strict flag overrides interior-strict nuance
        if strict:
            viol = np.diff(dr.y)<=0
 #       print(viol)
        if not(any(viol)):
            break

        i = np.min(np.where(viol==True))
 #       print(i)
 #       print(dr)
        dr.loc[i,'y'] = (dr.y[i]*dr.weight[i]+dr.y[i+1]*dr.weight[i+1]) / (dr.weight[i]+dr.weight[i+1])
        dr.loc[i,'x'] = (dr.x[i]*dr.weight[i]+dr.x[i+1]*dr.weight[i+1]) / (dr.weight[i]+dr.weight[i+1])
        dr.loc[i,'weight'] = dr.weight[i]+dr.weight[i+1]
        dr = dr.drop(i+1).reset_index(drop=True)
        m -= 1
        if m <= 1:
            break

    # extending back to original boundaries if needed
    if dr.x[0]>dr0.x[0]:
        dr = dr0.head(1).append(dr,ignore_index=True).copy()
        dr.loc[0,'y']=dr.y[1]
        dr.loc[0,'weight']=0 # The weight is spoken for though
    if max(dr.x)<max(dr0.x):
        dr = dr.append(dr0.tail(1),ignore_index=True).copy()
        dr.loc[dr.x==max(dr.x),'weight'] = 0 # The weight is spoken for though
        dr.loc[dr.x==max(dr.x),'y'] = max(dr.y)

    # Finish up
    outy = np.interp(x=outx, xp=dr.x, fp=dr.y)
    if not full:
        return(outy)

    # Full-ass return
    else:
        inx = np.repeat(False, len(outx))
        for i in range(len(outx)-1):
            inx[i] = (outx[i] in dr0.x)

        if all(inx):
            drout = dr0
            drout.y = outy
        else:
            drout = pd.DataFrame(data={ 'x':outx,'y':outy, 'weight':0})

        output = {'output':drout,'input':dr0,'shrinkage':dr}
        return output