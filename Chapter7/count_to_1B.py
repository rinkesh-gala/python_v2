import time

start_time = time.time()

# Your Python code here
for i in range(1000000000):
    pass

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
