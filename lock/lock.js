var util = require('util');
var bleno = require('bleno');
var amqp       = require('amqp');
var amqp_hacks = require('./amqp-hacks');


var Gpio = require('onoff').Gpio,
	greenLed = new Gpio(23, 'out'),
	redLed = new Gpio(25, 'out'),
	lock = new Gpio(18, 'out');

var PrimaryService = bleno.PrimaryService;
var Characteristic = bleno.Characteristic;
var Descriptor = bleno.Descriptor;

var connection = amqp.createConnection({ host: "localhost", port: 5672 });
var secret = 12345;

connection.on('ready', function(){
    //connection.publish('task_queue', 'Hello World!');
    console.log(" Connected");

    //amqp_hacks.safeEndConnection(connection);
});
var UnlockCharacteristic = function(){
	UnlockCharacteristic.super_.call(this, {
		uuid: 'd271',
		properties: ['write'],
		descriptor: [
			new Descriptor({
				uuid: '2901',
                                value: 'Unlock'
				})
			]
		});
	};

util.inherits(UnlockCharacteristic, Characteristic);

UnlockCharacteristic.prototype.onWriteRequest = function(data, offset, withoutResponse, callback){
	var status;

	if(secret == secret){
		status = 'unlocked';
		greenLed.writeSync(1);
		lock.writeSync(1);
	} else {
		status = 'invalid code';
		redLed.writeSync(1);
}

setTimeout(this.reset.bind(this), 4000);
connection.publish('task_queue', data.toString());
console.log('unlock. data=' + data.toString());

console.log('status: ' + status);

callback(this.RESULT_SUCCESS);

this.emit('status', status);
};

UnlockCharacteristic.prototype.reset = function(){
	this.emit('status', 'locked');
	lock.writeSync(0);
	redLed.writeSync(0);
	greenLed.writeSync(0);
}

var StatusCharacteristic = function(unlockCharacteristic){
	StatusCharacteristic.super_.call(this, {
		uuid: 'd272',
		properties: ['notify'],
		descriptors: [
			new Descriptor({
				uuid: '2901',
				value: 'Status Message'
			})
		]
	});
	unlockCharacteristic.on('status', this.onUnlockStatusChange.bind(this));
	};
	util.inherits(StatusCharacteristic, Characteristic);

StatusCharacteristic.prototype.onUnlockStatusChange = function(status){
	if(this.updateValueCallback){
		this.updateValueCallback(new Buffer(status));
	}
};

var unlockCharacteristic = new UnlockCharacteristic();
var statusCharacteristic = new StatusCharacteristic(unlockCharacteristic);

var lockService = new PrimaryService({
	uuid: 'd270',
	characteristics: [
		unlockCharacteristic,
		statusCharacteristic
		]
});

bleno.on('stateChange', function(state){
	console.log('on -> stateChange: ' + state);

	if(state == 'poweredOn'){
		bleno.startAdvertising('RPi Lock', [lockService.uuid]);
	} else {
		bleno.stopAdvertising();
	}
});

bleno.on('advertisingStart', function(error){
	console.log('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));

	if(!error){
		bleno.setServices([lockService]);
	}
});

function exit(){
	greenLed.unexport();
	redLed.unexport();
	lock.unexport();
	process.exit();
}

process.on("SIGINT", exit);
