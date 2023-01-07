# Domoticz_Victor_Mousetrap_Cloud
Python plugin 

## Compability
VICTOR® SMART-KILL™ WI-FI ELECTRONIC MOUSE TRAP

Tested on Rasbian Bullseye.
Domoticz:
Version: 2022.2. 
Python Version: 3.9.2

The plugin is only tested with one trap but may work for more.

## Futures
Fetches information from www.victorsmartkill.com about your traps.

## Support
Not likley, I only do this in the winter.

# Usage
Copy folder "Victor" to Domotics/Plugins/

Get your personal API-Token by running the Token.py script.

Restart Domoticz.

Add "Victor smartkill API cloud" in the Hardware tab.

Enter your authorization Token and add the device.

After one minute you should receive the first update.



### Build Status
0.1.0 Initial release. API revealed by https://github.com/toreamun/victor-smart-kill/tree/main/victor_smart_kill


Todo\:
- [ ] Cleanup code
- [x] Finish basic README
- [ ] Initial upload
