import grpc
import pytest
from grpc_interceptor.testing import raises, dummy_client, DummyRequest

from grpc_interceptor import ServerInterceptor


class ErrorLogger(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        try:
            return method(request, context)
        except Exception as e:
            self.log_error(e)
            raise

    def log_error(self, e: Exception) -> None:
        pass


class MockErrorLogger(ErrorLogger):
    def __init__(self):
        self.logged_exception = None

    def log_error(self, error: Exception):
        self.logged_exception = error


def test_log_error():
    mock = MockErrorLogger()

    ex = Exception()
    special_cases = {"error": raises(ex)}

    with dummy_client(special_cases, interceptors=[mock]) as client:
        # Test no exception
        assert client.Execute(DummyRequest(input="foo")).output == "foo"
        assert mock.logged_exception is None

        # Test exception
        with pytest.raises(grpc.RpcError) as e:
            client.Execute(DummyRequest(input="error"))
        assert mock.logged_exception is ex
