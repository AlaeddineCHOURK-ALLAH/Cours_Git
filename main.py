import pandas
import matplotlib.pyplot as plt
def fibonnaci(n):
  if n==0 :
    return 0 
  elif n==1 : 
    return 1 
  return fibonnaci(n-1)+fibonnaci(n-2)
