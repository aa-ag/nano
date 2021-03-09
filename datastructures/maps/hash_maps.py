class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        # The returned hash code will be the bucket_index
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        # length of array to be used in Mod operation
        num_buckets = len(self.bucket_array)

        # represents (self.p^0) which is 1
        current_coefficient = 1

        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            # compress hash_code (Mod operation)
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            # compress coefficient as well
            current_coefficient = current_coefficient % num_buckets

        # one last compression before returning
        return hash_code % num_buckets

    def size(self):
        return self.num_entries


# Check the bucket_index for two different strings made with same set of characters
hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("one")
print(bucket_index)

bucket_index = hash_map.get_bucket_index("neo")
print(bucket_index)                                  # Collision might occur
