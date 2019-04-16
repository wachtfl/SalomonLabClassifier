#import matplotlib.pyplot as plt
import numpy as np
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import make_pipeline
# from sklearn.svm import SVC
# from sklearn.linear_model.logistic import LogisticRegression
import mne
from mne.decoding import (SlidingEstimator, cross_val_multiscore)
import scipy as sc
from scipy import io

data_path = 'data/'

subj_ids = ['1/']
for sid in subj_ids:
    #epoched = mne.read_epochs_eeglab(data_path+sid+'Hod_rec_26_9_18_v12018.09.26_16.53.13_CleanBeforeICA_method__trig2_5_hfRej_allChan_ADUJSTRej.set')
    data = io.loadmat(data_path + sid + 'data.mat')['EEG']['data'][0][0]
    data0 = data[0]
    data1 = data[1]
    print(len(data))


