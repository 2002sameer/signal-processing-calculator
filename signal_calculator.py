import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.signal import convolve, butter, filtfilt

def display_menu():
    print("\nSignal Processing Calculator")
    print("1. Convolution of two signals")
    print("2. Fourier Transform of a signal")
    print("3. Inverse Fourier Transform of a signal")
    print("4. Low-pass Filter")
    print("5. High-pass Filter")
    print("6. Exit")

def get_signal_input():
    n = int(input("Enter the number of samples for the signal: "))
    signal = []
    print(f"Enter {n} samples:")
    for _ in range(n):
        sample = float(input())
        signal.append(sample)
    return np.array(signal)

def plot_signals(signal, title):
    plt.figure()
    plt.plot(signal)
    plt.title(title)
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def perform_convolution():
    print("Enter the first signal:")
    signal1 = get_signal_input()
    print("Enter the second signal:")
    signal2 = get_signal_input()
    
    result = convolve(signal1, signal2, mode='full')
    print("Convolution Result:", result)
    plot_signals(result, "Convolution Result")

def perform_fourier_transform():
    print("Enter the signal for Fourier Transform:")
    signal = get_signal_input()
    
    result = fft(signal)
    print("Fourier Transform Result (Magnitude):", np.abs(result))
    plot_signals(np.abs(result), "Fourier Transform (Magnitude)")

def perform_inverse_fourier_transform():
    print("Enter the signal for Inverse Fourier Transform (in frequency domain):")
    n = int(input("Enter the number of samples: "))
    signal = []
    print(f"Enter {n} complex samples (use 'a+bj' format):")
    for _ in range(n):
        sample = input()
        signal.append(complex(sample))  
    
    signal = np.array(signal)
    result = ifft(signal)
    print("Inverse Fourier Transform Result (Real part):", np.real(result))
    plot_signals(np.real(result), "Inverse Fourier Transform (Real part)")

def butter_filter(signal, cutoff_frequency, fs, btype='low'):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(1, normal_cutoff, btype=btype, analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def apply_low_pass_filter():
    print("Enter the signal for low-pass filtering:")
    signal = get_signal_input()
    cutoff = float(input("Enter cutoff frequency: "))
    fs = float(input("Enter sampling frequency: ")) 
    result = butter_filter(signal, cutoff, fs, btype='low')
    print("Low-pass Filtered Result:", result)
    plot_signals(result, "Low-pass Filter Result")

def apply_high_pass_filter():
    print("Enter the signal for high-pass filtering:")
    signal = get_signal_input()
    cutoff = float(input("Enter cutoff frequency: "))
    fs = float(input("Enter sampling frequency: ")) 
    result = butter_filter(signal, cutoff, fs, btype='high')
    print("High-pass Filtered Result:", result)
    plot_signals(result, "High-pass Filter Result")

def run_calculator():
    while True:
        display_menu()
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            perform_convolution()
        elif choice == 2:
            perform_fourier_transform()
        elif choice == 3:
            perform_inverse_fourier_transform()
        elif choice == 4:
            apply_low_pass_filter()
        elif choice == 5:
            apply_high_pass_filter()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_calculator()