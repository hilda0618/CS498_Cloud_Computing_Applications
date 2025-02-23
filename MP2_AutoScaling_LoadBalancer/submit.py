import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "hilda0618@gmail.com" # <put your coursera account email>,
#I used my personal email for coursera, my Illinois email is hildal2@illinois.edu

YOUR_SECRET = "IUEqBZfLXqYjGS26" # <put your secret token from coursera>

# <To get full credits, leave this blank. It will run both section 1 and section 2 tests>
SECTION = "" # <put "1" to test section 1 in isolation; put "2" to test section 2 in isolation>

# Section 1
IP_ADDRESS1 = "13.57.250.45:5000" # <put your first EC2 instance's IP address:port>
IP_ADDRESS2 = "52.53.197.108:5000" # <put your second instance's IP address:port>
# Do not add "https://" to your loadbalancer address.
YOUR_LOAD_BALANCER1 = "cs498-try4-632816500.us-west-1.elb.amazonaws.com" # <put your load_balancer address for section 1 (explicitly add :port if port is not 80)>
# Section 2
YOUR_LOAD_BALANCER2 = "s2t3-1456336326.us-west-1.elb.amazonaws.com" # <put your load_balancer address for section 2 (explicitly add :port if port is not 80)>, 

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
#payload = { "num": 12345}
headers = {"Content-Type": "application/json"}

input = {
            'ip_address1': IP_ADDRESS1,
            'ip_address2': IP_ADDRESS2,
			'load_balancer1': YOUR_LOAD_BALANCER1, 
            'load_balancer2': YOUR_LOAD_BALANCER2,
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
			'section': SECTION
		}
payload = { "input": json.dumps(input),
    		"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
        }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)