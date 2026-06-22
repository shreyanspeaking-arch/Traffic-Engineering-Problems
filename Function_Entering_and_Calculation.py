def ef(func_str, **variables):
    import math
    
    # Load all math functions into our safe environment
    env = {k: v for k, v in math.__dict__.items() if not k.startswith('_')}
    
    # Add your variables into the environment
    env.update(variables)
    
    # Evaluate and return the result
    return eval(func_str, {"__builtins__": None}, env)
