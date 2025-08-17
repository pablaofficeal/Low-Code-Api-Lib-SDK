import requests

class user:
    def __init__(self, token):
        self.token = token
        self.url = "https://soundrush.live/api_dev"
        
    def _handle_json_response(self, response, method_name=""):
        """Helper method to handle JSON responses and errors consistently"""
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Could not decode JSON response from {method_name}. Status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return {"error": "Invalid JSON response", "status_code": response.status_code}


    def get(self, endpoint):
        response = requests.get(self.url+endpoint, headers={"Authorization": self.token})
        return self._handle_json_response(response, "GET")
    def post(self, endpoint, data):
        response = requests.post(self.url+endpoint, headers={"Authorization": self.token}, json=data)
        return self._handle_json_response(response, "POST")
        
    def put(self, endpoint, data):
        response = requests.put(self.url+endpoint, headers={"Authorization": self.token}, json=data)
        return self._handle_json_response(response, "PUT")
        
    def delete(self, endpoint):
        response = requests.delete(self.url+endpoint, headers={"Authorization": self.token})
        return self._handle_json_response(response, "DELETE")
        
    def patch(self, endpoint, data):
        response = requests.patch(self.url+endpoint, headers={"Authorization": self.token}, json=data)
        return self._handle_json_response(response, "PATCH")


if __name__ == "__main__":
    user = user("123")
    # Get user data
    get_result = user.get("/user")
    print("GET result:", get_result)
    
    # Post user data
    post_result = user.post("/user", {"name": "Pavlo"})
    print("POST result:", post_result)
