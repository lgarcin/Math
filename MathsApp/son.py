from scipy.io.wavfile import read, write
from numpy.fft import fft, ifft, rfft, irfft
from numpy import int16, mean

rate, data = read('Tropic Of Cancer - More Alone.wav')

f = fft(data.T)
print(f.shape)
f[:, f.shape[1] // 2:] = 0
test = ifft(f).astype(int16).T

write('toto.wav', rate, test)

from playsound import playsound

playsound('toto.wav')
