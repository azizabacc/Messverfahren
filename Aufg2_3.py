# script test_readColumnData.py
# -*- coding: utf-8 -*-

import numpy as np
import PhyPraKit as ppk

# -----example Code illustrating usage --------------------
if __name__ == "__main__":
  import sys, numpy as np, matplotlib.pyplot as plt
  from PhyPraKit import odFit, labxParser, readColumnData
  from scipy import interpolate
  from scipy import signal

  def Imp(f,r,l,C):
      return np.sqrt(r**2+(2.*np.pi*f*l-1/(2.*np.pi*f*C))**2)
  
  def myFunction(n,As,wnull=9000,beta=1428.571):
      F = As/((wnull**2-(2*np.pi*n)**2)**2+(4*np.pi*n*beta)**2)**0.5
      return F

  fname='Aufg2_3.dat'
  ncols=3

  data_array, info_dict =\
    readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
  freqa=data_array[:,0] # 1st column
  U=data_array[:,1]
  deltat=data_array[:,2]
  Stroma=U
  
  phasv=np.zeros(len(deltat))
  i=0
  for i in range(len(deltat)):
      phasv[i]=freqa[i]*deltat[i]
##################################################################
# ALLE Phaseversch- Resonanz plot

  
# aus pylab_examples example code: multiple_yaxis_with_spines.py  
  fig4, ax4 = plt.subplots()
  fig4.subplots_adjust(right=0.75)

  par1 = ax4.twinx()
  
  #p1, = ax4.plot(freqc, Stromc, 'r')
  p1, = ax4.plot(freqa, Stroma, 'r')
  p1, = ax4.plot(freqa, Stroma, 'r.')
  p2, = par1.plot(freqa,phasv,'b')
  p2, = par1.plot(freqa,phasv,'b.')
  #p2, = par1.plot(freqc,Imp(freqc,100,0.035,0.000000320),'g')

  ax4.set_xlabel('$Frequenz$ $f$ (Hz)', size='large')
  ax4.set_ylabel('$Amplitude$ $I$ (mA) ', size='large')
  par1.set_ylabel('$Phasenwinkel$ (Grad)  ', size='large')

  ax4.yaxis.label.set_color(p1.get_color())
  par1.yaxis.label.set_color(p2.get_color())

  tkw = dict(size=4, width=1.5)
  ax4.tick_params(axis='y', colors=p1.get_color(), **tkw)
  par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
  ax4.tick_params(axis='x', **tkw)
  ax4.grid()
  
  plt.savefig('Aufgabe2_3.pdf')
  



plt.show()

