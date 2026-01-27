import numpy

data = numpy.loadtxt("Data.txt")

vals = data
fft_imag = numpy.fft.fft(vals)
        
fft = numpy.abs(fft_imag)
        
numpy.savetxt("Data_FFT.txt", fft, fmt = '%0.4f', delimiter = '\t')
        