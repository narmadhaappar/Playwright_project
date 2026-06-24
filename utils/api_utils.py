class APIUtils:
    def __init__(self, request_context):
        self.request = request_context

    def post(self, endpoint, payload):
        return self.request.post(endpoint, data=payload)
    
    def get(self,endpoint):
        response=self.request.get(endpoint)
        return response

    def put(self,endpoint,payload):
        response=self.request.put(endpoint,data=payload)
        return response
    
    def delete(self,endpoint):
        response=self.request.delete(endpoint)
        return response
