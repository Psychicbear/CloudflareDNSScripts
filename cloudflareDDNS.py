import sys
import json
import requests as client
import io
token = "Bf24nttfRk9pVqn9-0bvIKDOF8Vq0aRMd0fKdyTs"
api = "https://api.cloudflare.com/client/v4/"


class configManager:
    def __init__(self):
        self.config = "config.json"
        self.token = ""
        self.records = []
        self.loadConfig(self)

    def setToken(self):
        self.token = input("Please enter your token:\n")

    def addRecord(self):
        pass

    def removeRecord(self):
        pass

    def loadConfig(self):
        try:
            with open(self.config) as f:
                data = json.load(f)
                self.token = data.get('token')
                self.records = data.get('records', [])
                
        except FileNotFoundError:
            print("File does not exist, creating JSON now!")
        
        except json.JSONDecodeError:
            print("An Error occurred when reading the file.")
        
        except Exception as e:
            print("An unexpected error has occurred: ", str(e))
    



class DNS_API:
    def __init__(self, ip, token, zone, email):
        self.ip = ip
        self.token = token
        self.zone = zone
        self.email = email

    def test_token(self):
        headers: _HeadersMapping = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }
        req: Response = client.get( api + "user/tokens/verify", headers= headers)
        return req.json()["success"]
    
    def check_zone(self):
        headers: _HeadersMapping = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        print(headers)
        req: Response = client.get(api + "/zones/" + self.zone + "/dns_records", headers=headers)
        print(json.dumps(req.json(), indent=4))

def who_am_i():
    req = client.get("http://www.ipecho.net/plain")
    print(req.text)
    return req.text

def main():
    print("Running program")
    ip = who_am_i()
    dns = DNS_API(ip, token, "f562bba76bee62974aab7fdc93ca5a86", "rjscho@live.com.au")
    dns.check_zone()
    
    print("Your IP is:", ip)
    

if __name__ == "__main__":
    main()




