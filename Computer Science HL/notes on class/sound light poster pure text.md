## Original Version

Interesting to consider: Alarm Conditions 

They typically include inputs from other building 
control systems like the fire alarm or the HVAC system. 
Input of the kind could trigger an emergency “all lights on” 
or “all lights flashing” command. 

 PROGRAM LOGIC: 

There is a microcontroller that the system takes advantage 
of to process all input signals from the sensors. It then makes 
decisions that are based on the program logic. They output control actions.

A control system manages and regulates devices or systems using the 
Input-Process-Output (IPO) model, where sensors detect input, a 
microprocessor processes data, and actuators execute actions. Systems can be 
open-loop(no feedback) or closed-loop(using feedback to correct errors, e.g., 
negative feedback for stability). Control can be centralized(one processor) or 
distributed(multiple processors).

This centralized system is a open-loop sound-activated automatic light 
switch that detects both sound intensity and ambient lighting conditions. 
The VU meter senses sound, while the LDR monitors light levels, converting 
these analog inputs into digital signals processed by a processor. When a
 person approaches (and makes a sound), the system turns the light ON for 
1 minute if it is dark(sensed by LDR and determined by processor). This 
 system is suitable for settings like hotels, corridors, garages, and basements.

 Detects whether there 
is any movement in the 
corridor. If there is, it 
triggers the system.

 It toggles the system 
by a sound pulse, 
detects a present sound 
pressure level. Sound 
sensor is defined as a 
module that detects sound 
waves through its intensity 
and converting it to electrical 
signals. 

Generally, Delixi may use ADCs in order to process 
inputs from the sensors and DACs to control the 
outputs. 

ADC – Convert analog output (LDRs) into some digital 
value; system assesses ambient light levels or, if in 
the case of the motion sensor, it converts the signal 
to determine whether motion is being detected. 

DAC – dimming control by converting didgtal signals 
from the cs into analog signals. Could be mentioned 
that if the system has RGB, DACs could potentially 
control the intensity of each color channel on 
‘digital input values’. 

---

## Modified Version

Interesting to consider: Alarm Conditions

They typically include inputs from other building control systems like the fire alarm or the HVAC system. Input of the kind could trigger an emergency “all lights on” or “all lights flashing” command (_Legrand CP Electronics_).

PROGRAM LOGIC:

There is a microcontroller that the system takes advantage of to process all input signals from the sensors. It then makes decisions that are based on the program logic. They output control actions (_Wikipedia, Lighting Control System_).

A control system manages and regulates devices or systems using the Input-Process-Output (IPO) model, where sensors detect input, a microprocessor processes data, and actuators execute actions. Systems can be open-loop (no feedback) or closed-loop (using feedback to correct errors, e.g., negative feedback for stability). Control can be centralized (one processor) or distributed (multiple processors) (_Delixi Electric User Manual_).

This centralized system is an open-loop sound-activated automatic light switch that detects both sound intensity and ambient lighting conditions. The VU meter senses sound, while the LDR monitors light levels, converting these analog inputs into digital signals processed by a processor. When a person approaches (and makes a sound), the system turns the light ON for 1 minute if it is dark (sensed by LDR and determined by processor). This system is suitable for settings like hotels, corridors, garages, and basements (_Electro Schematics_; _Delixi Electric Selection Guide_).

Detects whether there is any movement in the corridor. If there is, it triggers the system (_IJNIET_).

It toggles the system by a sound pulse, detects a present sound pressure level. Sound sensor is defined as a module that detects sound waves through its intensity and converts it to electrical signals (_Wikipedia, Electret Microphone_).

Generally, Delixi may use ADCs in order to process inputs from the sensors and DACs to control the outputs (_Delixi Electric Selection Guide_).

ADC – Convert analog output (LDRs) into some digital value; system assesses ambient light levels or, in the case of the motion sensor, it converts the signal to determine whether motion is being detected (_Electrical Counter_).

DAC – dimming control by converting digital signals from the control system into analog signals. Could be mentioned that if the system has RGB, DACs could potentially control the intensity of each color channel on ‘digital input values’ (_Legrand CP Electronics_).

## Reference

"Lighting Control System." _Wikipedia_, [https://en.wikipedia.org/wiki/Lighting_control_system](https://en.wikipedia.org/wiki/Lighting_control_system). Accessed 1 Dec. 2024.

"Products." _Delixi Electric_, [https://www.delixi-electric.com/en/jjcpzx/index.html](https://www.delixi-electric.com/en/jjcpzx/index.html). Accessed 1 Dec. 2024.

"What Are Lux Levels?" _The Electrical Counter_, [https://www.electricalcounter.co.uk/articles/what-are-lux-levels](https://www.electricalcounter.co.uk/articles/what-are-lux-levels). Accessed 1 Dec. 2024.

"Electret Microphone." _Wikipedia_, [https://en.wikipedia.org/wiki/Electret_microphone](https://en.wikipedia.org/wiki/Electret_microphone). Accessed 1 Dec. 2024.

_Delixi Electric User Manual._

"Sound Activated Switch Circuits." _Electro Schematics_, [https://www.electroschematics.com/sound-activated-switch/](https://www.electroschematics.com/sound-activated-switch/). Accessed 1 Dec. 2024.

"Light Activating Sound Detecting Switch." _International Journal of New Innovations in Engineering and Technology (IJNIET)_, [https://www.ijniet.org/wp-content/uploads/2024/04/1.1.pdf](https://www.ijniet.org/wp-content/uploads/2024/04/1.1.pdf). Accessed 1 Dec. 2024.

_Delixi Electric Selection Guide._

"Corridor Lighting Control Solutions." _Legrand CP Electronics_, [https://www.legrand.co.uk/sites/g/files/ocwmcr866/files/2023-05/22143%20CP%20Electronics%20Corridor%20Lighting%20Brochure%20-%20Issue%201.3%20V1.pdf](https://www.legrand.co.uk/sites/g/files/ocwmcr866/files/2023-05/22143%20CP%20Electronics%20Corridor%20Lighting%20Brochure%20-%20Issue%201.3%20V1.pdf). Accessed 1 Dec. 2024.