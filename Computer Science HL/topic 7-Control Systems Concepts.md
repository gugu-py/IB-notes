**Control System**: a device or set of device that controls, manages, commands, directs or regulates the behavior of other devices or systems. e.g. camera

**Key Components**:
- **sensor**+**actuator** (transducers): 
	- *role*: detect physical property and records, feed them to microprocessor; take action based on signal sent by microprocessor
	- convert one energy to another
	- **Analog-to-Digital Converters(ADC)**: literally convert Analog-to-Digital, so that processor can understand
- **microprocessor**: 
	- *role*: process the data and control the actuator to take actiond
	- an integrated chip that contains all functions of a CPU
	- ==compare the reading with pre-set values==

==Keys for Exams==:
- The sensor continuously collects data from the environment. It turns analog data to digital data. The processor/controller compares the readings with pre-set values. If certain requirement is satisfied, it sends signal to actuator. The actuator does something.
- **when talking about the interaction** between sensor, actuator, and microprocessor: divide your answer into three components, sensor reads/detects what, microprocessor compares what and sends what signal, actuator does what

sensor benefit:
- work continuously without losing efficiency
- cheaper than human worker
- react quick to monitored object

![[UWC/CS/_resources/Pasted image 20241114101741.png]]

![[UWC/CS/_resources/Pasted image 20241114101932.png]]


Input-Process-Output(IPO) model:
![[UWC/CS/_resources/Pasted image 20241114102322.png]]


**Feedback**: If (part of) output is used as (part of) input, it is known as feedback.

**Open Loop System**: Doesnt take any feedback into input. e.g. TV remote control

**Closed Loop System**: Take feedback into input; Correct errors

**Negative Feedback Loop**: a system where feedback is given to reduce fluctuation in subsequent output; try to make the output closer to some equilibrium or target value. e.g. airplane stablizer
**Positive Feedback Loop**: a system where feedback is given to make the output further from some equilibrium or target value. 

![[UWC/CS/_resources/Pasted image 20241114103750.png]]

**Centralized and Distributed Control System**
- Centralized: only one processing unit control others
- Distributed: a number of processing units control others(same goal)
![[UWC/CS/_resources/Pasted image 20241114104007.png]]
![[UWC/CS/_resources/Pasted image 20241114104018.png]]

**Autonomous Agents**: software programs that respond to state and events in their environment independent from direct instruction by the user or owner of the agent, but acting on behalf and interest of the owner. e.g. recommendation system
- Autonomy: independently select tasks in order to achieve certain goals
- Reactive: senses environment and reacts based on input
- Concurrency/Sociality: interact with other agents cooperatively, competitively, or in coordination.
- Persistence: an agent consistently acts in pursuit of certain goal
