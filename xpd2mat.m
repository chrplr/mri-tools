% convert a xpd file into a conditions file for SPM
% Time-stamp: <2016-12-14 22:06:32 cp983411>

input = 'data/RealLocalizer_V2_03.xpd'
output = 'data/RealLocalizer_V2_03.mat'

%%
fileID = fopen(input);

% this is specific to the xpd and may need to be changed for a new experiment:
HEADER = 10;            % number of lines to skip at the beginning of the file
template = '%f%s%f%f';  % template for data lines
condcol = 2;            % index of the column containing the condition identifiers
onscol = 3;             % index of the column containing the onsets
durcol = 4;             % index of the column containing the durations

%%
C = textscan(fileID, template, 'Delimiter', ',', 'HeaderLines', HEADER);
fclose(fileID);

cond = C{condcol};
ons = C{onscol};
dur = C{durcol};

%% 
names = unique(cond)';

onsets = {};
durations = {};
for j = 1:size(names, 2)
            onsets{j}  =  ons(find(strcmp(cond, names{j}))) / 1000;
            durations{j}  =  dur(find(strcmp(cond, names{j}))) / 1000;
end

%%
save(output, 'names', 'onsets', 'durations');

