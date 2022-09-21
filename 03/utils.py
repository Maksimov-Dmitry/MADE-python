import json
import time


def parse_json(json_str: str, required_fields=None, keywords=None, *, keyword_callback):
    if not json_str or (not required_fields and not keywords):
        return

    json_doc = json.loads(json_str)
    for key, value in json_doc.items():
        if not required_fields or key in required_fields:
            for word in value.split():
                if not keywords or word in keywords:
                    keyword_callback(word)


def mean(last_k):
    def _mean(func):
        run_time_history = []
        def wrapper(*args, **kwargs):
            start_ts = time.time()
            res = func(*args, **kwargs)
            end_ts = time.time()
            run_time = round(end_ts - start_ts, 5)
            if len(run_time_history) < last_k:
                run_time_history.append(run_time)
            else:
                run_time_history.insert(0, run_time)
                run_time_history.pop()
            wrapper.mean_run_time = {'mean_run_time': sum(run_time_history)/len(run_time_history),
                                     'last_k': min(last_k, len(run_time_history))}
            return res
        return wrapper
    return _mean


if __name__ == "__main__":
    func_results = []
    def func(word):
        func_results.append(word)

    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', keyword_callback=func)
    assert [] == func_results
    parse_json('', required_fields=["key1"], keywords=["word2"], keyword_callback=func)
    assert [] == func_results
    parse_json('', required_fields=["key3"], keywords=["word2"], keyword_callback=func)
    assert [] == func_results
    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', required_fields=["key1"], keywords=["word2"], keyword_callback=func)
    assert ['word2'] == func_results
    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', required_fields=["key2"], keyword_callback=func)
    assert ['word2', 'word2', 'word3'] == func_results
    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', keywords=["word2"], keyword_callback=func)
    assert ['word2', 'word2', 'word3', 'word2', 'word2'] == func_results

    last_k_foo = 10
    last_k_boo = 5

    @mean(last_k_foo)
    def foo(sleep_time_s):
        time.sleep(sleep_time_s)

    @mean(last_k_boo)
    def boo(sleep_time_s):
        time.sleep(sleep_time_s)

    sleep_time_foo = 0.7
    sleep_time_boo = 0.3
    for i in range(1, 14):
        foo(sleep_time_foo)
        boo(sleep_time_boo)
        assert abs(foo.mean_run_time['mean_run_time'] - sleep_time_foo) < 1e-2
        assert foo.mean_run_time['last_k'] == min(last_k_foo, i)
        assert abs(boo.mean_run_time['mean_run_time'] - sleep_time_boo) < 1e-2
        assert boo.mean_run_time['last_k'] == min(last_k_boo, i)
