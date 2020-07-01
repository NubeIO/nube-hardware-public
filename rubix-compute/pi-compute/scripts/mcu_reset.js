const Gpio = require('pigpio').Gpio;

const mcu_reset = new Gpio(12, {mode: Gpio.OUTPUT});

mcu_reset.digitalWrite(0);

setTimeout(function(){ mcu_reset.digitalWrite(1);}, 2000);

