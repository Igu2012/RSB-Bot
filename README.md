RSB bot

yo, igu here, just popping in to say a quick thanks:

i give huge credit to r2 (the original genius behind this code).
i basically just took his work, fixed a few things, and made it way more user-customizable.

so, before you fire up the scripts, you just need to make sure python is installed and you run these commands in your terminal:

---

# modules to download
# If you're having trouble using PIP, I highly recommend that you follow this guy's steps (he saved me many hours): https://www.youtube.com/watch?v=nj8gVMH6yR8&t=62s

first, install the core python modules:

pip install pynput

pip install keyboard

pip install speechrecognition

next up is pyaudio. this one needs system stuff, so hit it with the command for your specific operating system:

* windows:
    python -m pip install pyaudio

* macos:
    brew install portaudio
    pip install pyaudio

* gnu/linux:
    sudo apt install python3-pyaudio

---

# configuration and execution

1. this part is key: change the number for device_index in config.py until running the script prints out "stereo mix" or whatever your roblox audio output is. (if this is wrong, the bot won't hear a thing.)

if you feel like tweaking things, you can change these optional settings in config.py:

* change recordingTime if you want it to record for a longer or shorter duration.
* change prefixKeyStart for the key that kicks off the recording, and prefixKeyStop for the key that kills the program.
* change min and max to fine-tune the delay between each letter the bot types.

---

once you've got step 1 done, run it with: python recorder.py
