## Day 12: The Secret Number Guessing Game

- functions that call themselves.
- scope of variables.

Python primarily uses function-level scope. This means that variables declared inside a function are local to that function and are not accessible outside of it. Unlike languages like C++ or Java, Python does not create a new scope for blocks like if, for, or while statements. Variables defined within these blocks are still accessible outside the block, within the scope they were defined.

```
def my_function():
    if True:
        x = 10
    print(x)
# output 10
```

![image](https://github.com/user-attachments/assets/ef16bb35-0caf-4d71-b01d-8b67a6c69383)
