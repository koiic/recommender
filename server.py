# create a singleton class for GRPC requests
import os

import grpc

from marketplace import recommendations_pb2_grpc
from marketplace.recommendations_pb2_grpc import RecommendationsStub


class GRPCClient:
    def __init__(self):
        self.host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
        self.channel = grpc.insecure_channel(f"{self.host}:50051")
        self.client = recommendations_pb2_grpc.RecommendationsStub(self.channel)

    def make_request(self, data):
        request = RecommendationsStub(data)
        response = self.client.Recommend(request)
        return response
