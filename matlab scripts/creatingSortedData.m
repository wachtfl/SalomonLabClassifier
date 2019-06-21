function [numOfElectrodes, samplingRate] = creatingSortedData(fromMatlab, sbjNumber, fileName1, fileName2, electrodesToRemove) %fileName WITH the '.set' extension

% fromMatlab = 1
% sbjNumber = 109
% fileName1 = 'Hod_rec_26_9_18_v12018.09.26_16.53.13_trig2_secondRound_ChansRemoved_hfnoiserej.set';
% fileName2 = 'Hod_rec_26_9_18_v12018.09.26_16.53.13_trig5_secondRound_ChansRemoved_hfnoiserej.set';

EEG1 = pop_loadset(fileName1);
data1= EEG1.data;


EEG2 = pop_loadset(fileName2);
data2 = EEG2.data;


% create Channels info:
chaninfo = EEG1.chaninfo
chanlocs = EEG1.chanlocs

if nargin == 5 %we have electrodes to remove -CHANGE THIS TO IF ELECTRODES TO REMOVE NOT EMPTY OR SOMTHING..
    for i=1:length(electrodesToRemove)
        data1(electrodesToRemove(i),:,:)=[];
        data2(electrodesToRemove(i),:,:)=[];
        
        channel_inf.chanlocs(electrodesToRemove(i)) = []
    end
end

[numOfElectrodes, duumy, dummy] = size(data1);
samplingRate = EEG1.srate

% Flip first and second dimensions of dataset to conform to DDTBOX format
sorted_data1 = permute(data1, [2, 1, 3]);
sorted_data2 = permute(data2, [2, 1, 3]);

%eeg_sorted_cond{run, condition}(timepoints, channels, epochs)
eeg_sorted_cond{1,2} = {};

eeg_sorted_cond{1, 1} = data1
eeg_sorted_cond{1, 2} = data2



pathToDir = strcat('../../results/EEG_data/sbj', sbjNumber);
pathToChan = '../../results/Channel Locations/channel_inf.mat'
pwd
if fromMatlab == 1
    pathToDir = strcat('../results/EEG_data/sbj', sbjNumber);
    pathToChan = '../results/Channel Locations/channel_inf.mat'
end


pathToSave = strcat(pathToDir, '/eeg_sorted_cond.mat')
if ~exist(pathToDir, 'dir')
   mkdir(pathToDir)
end
save(pathToSave, 'eeg_sorted_cond');

if ~exist(pathToChan, 'dir')
   mkdir(pathToChan)
end
save(pathToChan,'chaninfo','chanlocs')

