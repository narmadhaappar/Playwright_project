import json
class APIUtils:
    def __init__(self, request_context):
        self.request = request_context

    def post(self, endpoint, payload):
        response = self.request.post(endpoint, headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps(payload))
        print("request url:", response.url)
        print("status code:", response.status)
        print("response body:", response.text())
        return response
    
    def get(self,endpoint):
        response=self.request.get(endpoint)
        return response

    def put(self,endpoint,payload):
        response=self.request.put(endpoint,headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps(payload))
        return response
    
    def delete(self,endpoint):
        response=self.request.delete(endpoint)
        return response
