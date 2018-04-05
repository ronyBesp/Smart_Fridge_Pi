# SmartFridge_Pi
The Pi code of the Smart Fridge Project. 

The Pi will take photos of the fridge/cupboard using the Pi camera module
and will send it to the Server using a POST request every 10 minutes.

This interval can be changed in the take_picture.py

In the POST request, the user_name must be specified i.e. iosAcct

Also, the image it took will be sent in the POST request as a base64 encoded string.


The launch.sh script is used to ensure that the take_picture script runs on Pi's bootup.

The take_picture script will run continously.



The POST request points to the server right now, but the 'url' string in take_picture can be modified to work locally.

The other repositories for the Smart Fridge Project are found:

**Server**: 

**iOS App**: 
