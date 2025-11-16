import functools
import time

def async_timeit(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time

        print(f"函数 {func.__name__} 完成，耗时：{total_time:.2f} 秒")
        return result

    return wrapper