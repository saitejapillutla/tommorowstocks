#import necessary packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn 
%matplotlib inline
from google.colab import drive
drive.mount('/content/drive')
Mevents2015=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/MEvents2015.csv")
