import time
import numpy as np # type: ignore

# Number of elements to test
num_elements = 100000

# --- (a) Measuring Python List (Appending 100,000 elements) ---
start_time = time.time()

python_list = []
for i in range(num_elements):
    python_list.append(i)

end_time = time.time()
list_duration = end_time - start_time


# --- (b) Measuring NumPy Array (Creating 100,000 elements) ---
start_time = time.time()

# np.arange creates an array sequentially, similar to the list loop
numpy_array = np.arange(num_elements)

end_time = time.time()
numpy_duration = end_time - start_time


# --- Print Results and Compare ---
print(f"Time taken to append to Python List:  {list_duration:.6f} seconds")
print(f"Time taken to create NumPy Array:     {numpy_duration:.6f} seconds")

# Calculate the speed difference
speed_factor = list_duration / numpy_duration
print(f"\nNumPy was approximately {speed_factor:.1f}x faster than the Python list loop!")