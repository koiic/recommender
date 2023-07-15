# Description: Main file for the server
from concurrent import futures
from signal import signal, SIGTERM

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

import recommendations_pb2_grpc
from recommendations import RecommendationService


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=interceptors)
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print('The server has started.....................')

    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
