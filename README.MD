This project includes the code for self-balancing robot. The goal of this project is to learn programming with python. The robot is controlled with WebSocket connection.

*How does it work:*
- The Raspberry board hosts a webpage for controlling the robot. The webpage sends the gamepad positions to the Raspberry board with a WebSocket protocol.

- The Raspberry board reads all sensor values, combines them with controller values and calculates the motor speeds

- The raspberry board sends the motor speed values to the Teensy board via I2C bus

- The Teensy board receives the motor speed values and controls the motors by calculating and sending motor step signals to the motor drivers

*Parts:*
- Raspberry Pi 2 Model B
- Teensy 3.0
- 2x NEMA17 Stepper motor
- 2x DRV8825 Stepper driver (Or similar)
- GY-87 Sensor board (BMP180, HMC5883L and MPU6050)
- TeraRanger One
