import numpy as np

def superimpose_sine_waves(sine_list, sampling_rate, start_idx, end_idx):
    n = np.arange(start_idx, end_idx, 1)
    t = n / sampling_rate
    signal = np.zeros_like(t)
    # For each sine in the list:
    for sine_dict in sine_list:
        # get the samples by applying the formula. 
        amplitude = sine_dict['amplitude']
        frequency = sine_dict['frequency']
        phase = sine_dict['phase']
        sine_wave = amplitude * np.sin(2*np.pi*frequency*t + phase)
        # Add / superimpose the samples. 
        signal += sine_wave # add sine wave to signal 
    # Return them. 
    return signal, t
