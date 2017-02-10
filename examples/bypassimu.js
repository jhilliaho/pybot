var five = require("johnny-five");
var Raspi = require("raspi-io");
var board = new five.Board({
  io: new Raspi()
});
var SerialPort = require("serialport");

board.on("ready", function() {
	board.io.i2cConfig();
	board.io.i2cWrite(0x68, [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00]);
	var imu = new five.IMU({controller: "MPU6050"});

	console.log("MPU6050 CONFIGURED");
	process.exit();

});
