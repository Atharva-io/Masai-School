import numpy as np

# 1. Set a random seed for reproducibility.
np.random.seed(42)

# 2. Generate a 2D NumPy array representing a dataset with 100 samples and 3 features
data = np.random.rand(100, 3)

# 3. Compute the mean and standard deviation per feature using axis-aware operations.
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

# 4. Normalize the dataset using broadcasting
normalized = (data - mean) / std

# 5. Extract the first 80% (80) of samples as a training set, and remaining 20% (20) as test set
train_data = normalized[:80]
test_data = normalized[80:]

# 6. Modify a sliced value intentionally and observe its effect on the original array
train_data[0, 0] = 999.9  # Modifying the slice

# 7. Print output as required
print(f"Original data shape: {data.shape}")
print(f"Mean shape: {mean.shape}")
print(f"Training data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")
print("Note: Modifying the slice affected the original array")
