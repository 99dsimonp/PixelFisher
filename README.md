# PixelFisher

This repository contains two pixel-based bots for fishing in WoW: One acting on sound to detect when to click the bobber, and one acting on movement of the bobber. These python scripts most likely do not work out of the box, and have solely been published for others to learn.

The bots function by rapidly screenshotting the monitor and detecting the fishing bobber. Thus, there is no need for reading memory or injection. 

Basic use:
1. Place your character where you want to fish. Make sure no mobs are nearby.
2. Place fishing key on 1.
3. Zoom in.
4. Take a screenshot, crop it to just include the bobber, name it bobber.jpg and place in same folder. See file in repo as example.
5. Run python script.


The bots use template matching with opencv2 to find the bobber. 
To use the audio version you will need to install a separate program (https://vb-audio.com/Cable/index.htm) for a virtual audio output. WoW has to be outputting sound unto this virtual audio device. Meanwhile, sounddevice on Python has to hook up to this device - it may not automatically be doing so. Make sure to turn off music in wow. 

All code in repository is based on Python3.

THIS REPOSITORY EXISTS FOR EDUCATIONAL PURPOSES ONLY AND NO FURTHER SUPPORT WILL BE GIVEN TO MAKE THINGS WORK.
