from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# sandbox credentials
username = "fridahk"
apikey = "33769fdf07dc3d6c016aca76074937540ad1203cc967f9f4862b1d201eeea139"

# Create a new instance of the gateway class
gateway = AfricasTalkingGateway(username, apikey)


# function to send sms
def send_sms(to, message):
    try:
        results = gateway.sendMessage(to, message)
        return results[0]['status']
    except AfricasTalkingGatewayException, e:
        return e
