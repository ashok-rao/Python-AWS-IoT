# Python-AWS-IoT

Thanks to Mario Cannistra's getting started with AWS IoT sample code and documentation. This project uses his code
for most MQTT functionality.


AWS CLI needs to be configured, up and running before using this application.
More information on how to configure AWS CLI can be found from http://docs.aws.amazon.com/iot/latest/developerguide/installing-aws-cli.html

To run, open 2 terminal windows. Run the awsiotsub.py in 1 and the awsiotpub.py in another. You should see MQTT messages being sent
out in the publish window and subsequently being received in the subscribe window.
