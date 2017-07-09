

1) The publisher and subscriber.py programs are used to subscribe and publish the motion sensor data to the topic in AWS IOT

2) S3-upload folder contains the javascript file to upload the captured pictures to the S3 database. It also contains configuration JSON files contaning the AccesskeyID and SecretAccessKey

3) The motion-config folder contains the configuration files for the motion libraries to send email-alerts with the captured picture.

4) DoorLatch.py is used to lock/unlock the doorlatch. The GPIO pin is toggled high/low using the Android Blynk mobile App.

References

https://utbrudd.bouvet.no/2017/01/05/building-a-motion-activated-security-camera-with-the-raspberry-pi-zero/

https://utbrudd.bouvet.no/2017/01/10/smarten-up-your-pi-zero-web-camera-with-image-analysis-and-amazon-web-services-part-2/

[1]	AWS IOT http://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html

[2] AWS S3
http://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html

[3] Blynk Server and APP
http://docs.blynk.cc/
