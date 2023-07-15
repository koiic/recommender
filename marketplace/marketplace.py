# create a flask app to fetch books from the recommendation service
import os

import grpc
from flask import Flask, render_template

from marketplace.recommendations_pb2_grpc import RecommendationsStub
from marketplace.recommendations_pb2 import BookCategory, RecommendationRequest

app = Flask(__name__)


class GRPCClient:


    def __init__(self):
        self.host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
        self.channel = grpc.insecure_channel(f"{self.host}:50051", options=(("grpc.enable_http_proxy", 0),))
        self.client = RecommendationsStub(self.channel)

    def make_request(self, data):
        request = RecommendationRequest(**data)
        response = self.client.Recommend(request)
        return response


# create a channel to the recommendation service
client = GRPCClient()


# create a flask route that will serve the recommendations
@app.route("/")
def render_home():
    data = dict(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    response = client.make_request(data)

    print(response.recommendations)

    return render_template("homepage.html", recommendations=response.recommendations,
                           category=BookCategory.Name(data['category']).lower())
