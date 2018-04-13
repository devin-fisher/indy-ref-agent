import asyncio


def run_async_test(func):
    def _run_test(*args, **kwargs):
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
        c = asyncio.coroutine(func)
        event_loop.run_until_complete(c(*args, **kwargs))
        event_loop.close()
    return _run_test
