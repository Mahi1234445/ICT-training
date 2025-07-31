import builtins
import inspect

# Get all names from the builtins module
all_builtins = dir(builtins)

# Filter names that are classes and are subclasses of BaseException
error_classes = [
    name for name in all_builtins
    if inspect.isclass(getattr(builtins, name)) and issubclass(getattr(builtins, name), BaseException)
]

# Sort and print the list
error_classes.sort()
for error in error_classes:
    print(error)
