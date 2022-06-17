function output = LatinSq_Whitening(input,L,opt)
%=============================================================
% FUNCTION: LatinSq_Whitening
% -- Generates n Latin square of order d dependent on key K
% Input:
%       input = a 256x256 matrix, 
%           L = a 256x256 Latin square with symbol set {0,1,...,255}
% Ouptut:
%      output = a 256x256 matrix
%=============================================================
% BSD licence 
%=============================================================
% By Yue (Rex) Wu (ywu03@tufts.ece.edu)
% ECE Department, Tufts University
% Mar 10, 2012
%=============================================================

if ~exist('opt','var')
    opt = 'encryption';
end

switch opt
    case 'encryption'
        switch mod(L(1),3)
            case 1
                input = flipud(input);
            case 2
                input = fliplr(input);
        end
        output = mod(input+L,256);
    case 'decryption'
        output = mod(input-L,256);
        switch mod(L(1),3)
            case 1
                output = flipud(output);
            case 2
                output = fliplr(output);
        end
end
        
        