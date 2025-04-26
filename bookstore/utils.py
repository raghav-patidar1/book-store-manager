# ------------------ Custom decorator -------------------

def log_action(func):
    """Decorator to log the execution of a method with its arguments."""

    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args[1:]}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


# ------------------ Custom validators -------------------

def validate_field_type(value, field_name, field_type,):
    """ Function to validate the datatype of an object (field_value). """
    
    try:
        return field_type(value)
    except ValueError:
        raise ValueError(f"Invalid type for {field_name}. Must be {field_type.__name__}.")

