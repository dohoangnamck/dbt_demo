import pandas as pd
import numpy as np
from pprint import pprint

import matplotlib.pyplot as plt
#%matplotlib inline
plt.rcParams['figure.figsize'] = (15,12)

# skip row 1 so pandas can parse the data properly.
loans_2007 = pd.read_csv('lending_club_loans.csv', low_memory=False) #skiprows=1, low_memory=False
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
#loans_2007 = loans_2007.drop(['url','desc'],axis=1)      # Don't need these columns.

print(loans_2007.shape)
loans_2007.head()