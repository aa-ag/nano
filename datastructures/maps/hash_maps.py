class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37                  # a prime numbers
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    # Returns the bucket_index
    def get_bucket_index(self, key):
        # The returned hash code will be the bucket_index
        return self.get_hash_code(key)

    # Returns the hash code

    def get_hash_code(self, key):
        key = str(key)

        # represents (self.p^0) which is 1
        current_coefficient = 1

        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p

        return hash_code  # The generated hash code will be the bucket_index


hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("abcd")
print(bucket_index)


hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("bcda")
print(bucket_index)
