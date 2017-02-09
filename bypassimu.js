var five = require("johnny-five");
var Raspi = require("raspi-io");
var board = new five.Board({
  io: new Raspi()
});

board.on("ready", function() {
	board.io.i2cConfig();
	board.io.i2cWrite(0x68, [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00]);

	// Configurate the imu module
	board.io.i2cWrite(0x68, [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00]);

	var imu = new five.IMU({controller: "MPU6050"});
	var compass = new five.Compass({controller: "HMC5883L"});	

	var lidar = new SerialPort("/dev/ttyUSB0", {
		baudRate: 115200,
		parser: SerialPort.parsers.readline('\r\n')
	});

	compass.on("change", function() {
		console.log("COMPASS: ", exports.moduleState.compass);
	});

	imu.on("change", function() {
		exports.moduleState.gyro = this.gyro.yaw.angle;
		console.log("YAW: ", exports.moduleState.gyro);
	});		

	// Event handlers
	lidar.on('data', function (num) {
		num = parseInt(num);
		console.log("LIDAR: ", num);
	});

	console.log("Lidar, imu and compass initialized");

});
