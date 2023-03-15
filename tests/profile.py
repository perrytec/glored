"""
Profiles the asynchronous calls of glored
"""
import unittest.mock as mock
import timeit

from glored import redis_client


def profile_set():
    """
    Returns the run duration of the function in microsecond
    """
    with mock.patch.object(redis_client, '_executor') as executor:
        duration = timeit.timeit(lambda: redis_client.asynchronous.set('somekey', 'somevalue'), number=1000)
        return duration * 1000


def profile_publish():
    """
    Returns the run duration of the function in microsecond
    """
    with mock.patch.object(redis_client, '_executor') as executor:
        duration = timeit.timeit(lambda: redis_client.asynchronous.publish('somechannel', 'somemessage'), number=1000)
        return duration * 1000


if __name__ == '__main__':
    set_duration = profile_set()
    publish_duration = profile_publish()
    print(f'Set: {set_duration}us')
    print(f'Publish: {publish_duration}us')

