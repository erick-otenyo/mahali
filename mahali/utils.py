from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# sandbox credentials
username = "otenyo"
apikey = "3d98d8b4b518429e3b7fd440395c80f3afa3c73470b145d26309fab38bf1c952"

# Create a new instance of the gateway class
gateway = AfricasTalkingGateway(username, apikey, "sandbox")


# function to send sms
def send_sms(to, message):
    try:
        results = gateway.sendMessage(to, message)
        return results[0]['status']
    except AfricasTalkingGatewayException, e:
        return e
