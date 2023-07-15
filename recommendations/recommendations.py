import random

import grpc
from grpc_interceptor.exceptions import NotFound

import recommendations_pb2_grpc
from recommendations_pb2 import BookCategory, BookRecommendation, RecommendationResponse

books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(
            id=4, title="The Hitchhiker's Guide to the Galaxy"
        ),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
    BookCategory.CHILDREN: [
        BookRecommendation(
            id=9, title="The chronicles of Riddick"
        ),
        BookRecommendation(
            id=10, title="Game of Thrones"
        ),
        BookRecommendation(id=11, title="Kid's Say the Darndest things"),
    ],
}


class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            raise NotFound("Category not found")
        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)
        return RecommendationResponse(recommendations=books_to_recommend)
