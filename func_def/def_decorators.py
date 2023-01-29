def function(func):
    def decorator(*args, **kwargs):
        return func(*args, **kwargs)
    return decorator


def run(name: str):
    print("run %s" % name)

# 推荐使用 注解类型的装饰器
@function
def go(name: str):
    print("go %s" % name)


go("dnslin")

function(run)("dnslin")

# Path: func_def\def_decorators.py
