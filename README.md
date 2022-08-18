# WiFi-Stealer
Simple WiFi passwords stealer based on Digispark and smtplib

# How to use

1. Install [Python](https://www.python.org/) and [Arduino IDE](https://www.arduino.cc/en/donate/).

2. Buy Digispark somewhere in Aliexpress.

3. [Set up the Arduino IDE for Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)

4. Change login, password and mail server settings in `payload/payload.py`.

5. Run `build_payload.py`.

6. Upload `dist/payload.exe` somewhere with direct link to the file (for example, GitHub)

7. Copy the link for downloading the file and paste it in the firmware file (there should be notes where specifically you should paste it)

8. Upload the firmware to Digispark.

That's it!!!

If you have some questions, feel free to write me in Discord (asimonov#0119).
