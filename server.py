from flask import Flask, abort
from flask_cors import CORS
import time
import RPi.GPIO as GPIO

app = Flask(__name__)
CORS(app)
valid_channels = [19, 26, 20, 21]  # note that these are gpio numbers f.e. value 13 => pin 33
pulse_time = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(valid_channels, GPIO.OUT)


def validate_channel_arg(channel):
    if channel not in valid_channels:
        abort(400)


@app.route('/gpio/<int:channel>/pulse', methods=['GET'])
def gpio_pulse(channel):
    validate_channel_arg(channel)
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(pulse_time)
    GPIO.output(channel, GPIO.LOW)
    return str(channel)


@app.route('/gpio/<int:channel>/on', methods=['GET'])
def gpio_on(channel):
    validate_channel_arg(channel)
    GPIO.output(channel, GPIO.HIGH)
    return str(channel)


@app.route('/gpio/<int:channel>/off', methods=['GET'])
def gpio_off(channel):
    validate_channel_arg(channel)
    GPIO.output(channel, GPIO.LOW)
    return str(channel)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

