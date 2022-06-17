function [varargout] = LatinSqEnc2(P,K)

%% Initial Settings
P = double(P);
% Generate a random key
if nargin == 1
    K = RandomKey;
    opt = 'NPE';
end

%% Probabilistic encryption
% Generate a random 256x256 Latin
M = round(rand(size(P)));
% Random masking
B = bitget(P,1);
X = xor(B,M);
PP = P-B+X;
% Generate 8-keyed Latin squares
L = KeyedLatin(K,9);

%% Cipher rounds
for i = 1:8
    % Extract a Keyed Latin Square
    tL = L(:,:,i);
    if i == 1
        CP = PP;
    end
    % Latin Square Whitening
    CW = LatinSq_Whitening(CP,tL,'encryption');
    % Latin Square Substitution
    if mod(i,2) == 0
        CS = LatinSq_Substitution(CW,tL,'row','encryption');
    else
        CS = LatinSq_Substitution(CW,tL,'col','encryption');
    end
    % Latin Square Permutation
    CP = LatinSq_Permutation(CS,tL,'encryption');
end
C =  LatinSq_Whitening(CP,L(:,:,9),'encryption');

%% Output Control
if nargin >= 2
    varargout = {C};
else
    varargout = {C,K};
end

