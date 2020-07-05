## this all library i use for this Speaker identification
import tkinter as tk
from tkinter import Canvas
import matplotlib.pyplot as plt
import numpy as np
import voiceit2
from PIL import ImageTk, Image

root = tk.Tk()
userDict = {}
import pyaudio
import wave

my_voiceit = voiceit2.VoiceIt2('key_6b2e0f83c191421e84805577ed6869b5',
                               'tok_bbeffc44a65d41f287b1b002136879b9')  # auth key and auth token
print(my_voiceit.get_phrases("en-US"))
print(my_voiceit.get_all_users())
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5


def train():
    userID = \
        userIdEntry.get()
    phrase = phraseEntry.get()

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(userID + '.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    data = my_voiceit.create_voice_enrollment(userID, "en-US", phrase, userID + '.wav')
    print(data)
    if (data['responseCode'] == "SUCC"):
        print("Sucessfully Trained")
        userDict[userID] = nameEntry.get()
    else:
        print("Failed To Train")


def imgShow(img):
    ##------------this as function----------------------------
    # convert lena.jpg into tkinter photo image
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)

    # create canvas to display picture
    w = Canvas(root)
    w.photo = photo
    w.create_image(0, 0, image=w.photo, anchor='nw')
    w.pack(fill=tk.BOTH, expand=tk.YES)


def detect():
    userID = userIdEntry.get()
    phrase = phraseEntry.get()
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(userID + 'detect.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    frames = b''.join(frames)

    ## it will plot the voice and FFT for coming data
    fig = plt.figure()
    fig.suptitle("Voice")
    fig2 = plt.figure()
    fig2.suptitle("FFT")
    s = fig.add_subplot(111)

    fft = fig2.add_subplot(111)

    amp = np.frombuffer(frames, np.int16)
    s.plot(amp)
    print(len(np.fft.fft(amp)));
    fft.plot(np.fft.fft(amp))
    plt.show()

    data = my_voiceit.voice_verification(userID, "en-US", phrase, userID + 'detect.wav')
    print(data)
    if (data['responseCode'] == "SUCC"):
        print("Sucessfully Detected")
        name = userDict[userID]
        imgShow(name + '.jpg')
        print(name)
    else:
        print("Failed To Detect")


def main():
    root.title("Voice Recognition App")
    root.mainloop()


button_train = tk.Button(root, width=25, height=1, text='Train', bg='green', fg='white', command=train)
button_detect = tk.Button(root, width=25, height=1, text='Detect', bg='green', fg='white', command=detect)
nameLabel = tk.Label(root, text="Enter UserID")
userIdEntry = tk.Entry(root, bd=5, width=50)
phraseLabel = tk.Label(root, text="Enter Phrase")
phraseEntry = tk.Entry(root, bd=5, width=50)

nameUserLabel = tk.Label(root, text="Enter User Name")
nameEntry = tk.Entry(root, bd=5, width=50)
nameDetectedLabel = tk.Label(root, text="Detected User Name")
nameShowEntry = tk.Entry(root, bd=5, width=50)
namePhotoLabel = tk.Label(root, text="Detected User Photo")

nameLabel.pack()
userIdEntry.pack()
phraseLabel.pack()
phraseEntry.pack()

nameUserLabel.pack()
nameEntry.pack()
button_train.pack()
button_detect.pack()
nameDetectedLabel.pack()
nameShowEntry.pack()
namePhotoLabel.pack()
if __name__ == '__main__':
    main()
