# PixelFisher

This repository contains two bots for fishing in WoW: One acting on sound to detect when to click the bobber, and one acting on movement of the bobber.

To use:
1. Place your character where you want to fish. Make sure no mobs are nearby.
2. Place fishing key on 1.
3. Zoom in.
4. Take a screenshot, crop it to just include the bobber, name it bobber.png and place in same folder.
5. Run python script.


The bots use template matching with opencv2 to find the bobber. 
To use the audio version you will need to install a separate program (https://vb-audio.com/Cable/index.htm) for a virtual audio output. WoW has to be outputting sound unto this virtual audio device. Meanwhile, sounddevice on Python has to hook up to this device - it may not automatically be doing so. Make sure to turn off music in wow. 


THIS REPOSITORY EXISTS FOR EDUCATIONAL PURPOSES ONLY AND NO FURTHER SUPPORT WILL BE GIVEN TO MAKE THINGS WORK.
