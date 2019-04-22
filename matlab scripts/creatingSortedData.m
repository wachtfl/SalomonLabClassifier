function x = creatingSortedData(sbjNumber, fileName1, fileName2) %fileName without the '.set' extension

x = 1;
cd '../raw data'

file1 = strcat(fileName1, '.set');
EEG1 = pop_loadset(file1);
data1= EEG1.data;

file2 = strcat(fileName2, '.set');
EEG2 = pop_loadset(file2);
data2 = EEG2.data;

% Flip first and second dimensions of dataset to conform to DDTBOX format
sorted_data1 = permute(data1, [2, 1, 3]);
sorted_data2 = permute(data2, [2, 1, 3]);

%eeg_sorted_cond{run, condition}(timepoints, channels, epochs)
eeg_sorted_cond{1,2} = {};

eeg_sorted_cond{1, 1} = data1
eeg_sorted_cond{1, 2} = data2

path = strcat('../results/EEG_data/sbj', num2str(sbjNumber));
pathToSave = strcat(path, '/eeg_sorted_cond.mat');
if ~exist(path, 'dir')
   mkdir(path)
end
save(pathToSave, 'eeg_sorted_cond');

