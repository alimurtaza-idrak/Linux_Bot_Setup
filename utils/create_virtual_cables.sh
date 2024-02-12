#!/bin/bash

# This script is to create virtual devices to reroute audio in Linux

# Create a virtual microphone that your AI model will read from as its input
pactl load-module module-null-sink sink_name=ai_virtmic sink_properties=device.description=AI_Virtual_Microphone_Sink

# Create another virtual microphone that Chrome will read from as its input
pactl load-module module-null-sink sink_name=chrome_virtmic sink_properties=device.description=Chrome_Virtual_Microphone_Sink

# Remap source for AI model
# This virtual microphone will take input from whatever audio is playing in Chrome
pactl load-module module-remap-source master=ai_virtmic.monitor source_name=ai_virtmic_input source_properties=device.description=AI_Model_Microphone_Input

# Remap source for Chrome
# This virtual microphone will take input from whatever audio is playing on your local PC
pactl load-module module-remap-source master=chrome_virtmic.monitor source_name=chrome_virtmic_input source_properties=device.description=Chrome_Microphone_Input

#Some Manual Work Needed:

# You will likely need to use 'PulseAudio Volume Control' to manually select the correct playback/recording devices for each application (Chrome and your AI model).
# For Chrome, when it asks for microphone permission, you'll want to select the "Chrome_Microphone_Input".
# For your AI model, set its microphone input as "AI_Model_Microphone_Input".

