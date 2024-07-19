import hashlib

# Sample data to hash
data = "This is a sample string".encode()

# Generate SHA-256 hash
hash_result = hashlib.sha256(data).hexdigest()

# Print the hash
print(hash_result)
