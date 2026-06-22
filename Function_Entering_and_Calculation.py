def ef(func_str, **variables):
    import math
    env = {k: v for k, v in math.__dict__.items() if not k.startswith('_')}
    env.update(variables)
    return eval(func_str, {"__builtins__": None}, env)
