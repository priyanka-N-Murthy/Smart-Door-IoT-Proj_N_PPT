

1) The publisher and subscriber.py programs are used to subscribe and publish the motion sensor data to the topic in AWS IOT

2) S3-upload folder contains the javascript file to upload the captured pictures to the S3 database. It also contains configuration JSON files contaning the AccesskeyID and SecretAccessKey

3) The motion-config folder contains the configuration files for the motion libraries to send email-alerts with the captured picture.

4) DoorLatch.py is used to lock/unlock the doorlatch. The GPIO pin is toggled high/low using the Android Blynk mobile App.

