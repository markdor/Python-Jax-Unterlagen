# https://www.linode.com/docs/guides/mock-testing-using-the-python-unittest-library/
# https://queirozf.com/entries/python-unittest-examples-mocking-and-patching
# https://changhsinlee.com/pytest-mock/
# https://santexgroup.com/wp-content/uploads/2014/10/mock_python.html#slide16
# https://alpopkes.com/posts/python/mocking/
# https://write.agrevolution.in/python-unit-testing-mock-and-patch-8ba9c796c9c2
# https://jingwen-z.github.io/how-to-apply-mock-with-python-unittest-module/
# https://dev.classmethod.jp/articles/mocking-around-with-python-and-unittest/
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
# https://docs.python.org/3/library/unittest.mock-examples.html
# https://realpython.com/python-mock-library/

from unittest.mock import Mock

myMock = Mock()
print(myMock)

myMock.setResult(1, 2)
print(myMock.getResult())

myMock.getResult.assert_called()

# print(myMock.getResult())
# myMock.getResult.assert_called_once()

myMock.setResult(2, 7)
myMock.setResult.assert_called_with(2, 7)

myMock.getResult.return_value = 3
print(myMock.getResult())

myMock.setResult()
myMock.getResult()
myMock.getResult()
myMock.getResult()
print("myMock.call_count", myMock.call_count)
print("myMock.setResult.call_count", myMock.setResult.call_count)
print("myMock.getResult.call_count", myMock.getResult.call_count)

print(myMock.setResult.call_args)
print(myMock.setResult.call_args_list)

print(myMock.method_calls)
