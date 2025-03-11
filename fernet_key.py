from cryptography.fernet import Fernet

# Function to generate a Fernet key
def generate_fernet_key():
    key = Fernet.generate_key()
    return key

# Generate the key
fernet_key = generate_fernet_key()

# Print the generated key
print("Generated Fernet Key:", fernet_key.decode())
