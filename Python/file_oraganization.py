class File: # Represents a file with attributes name and owner.
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class SingleLevelDirectory: # Represents a single-level directory structure.
    def __init__(self): # Initializes an empty single-level directory.
        self.files = {}
    def add_file(self, file): # Adds a file to the single-level directory.
        self.files[file.name] = file
    def search_file(self, file_name): # Searches for a file in the single-level directory.
        if file_name in self.files:
            return self.files[file_name]
        else:
            return None
        
class TwoLevelDirectory: # Represents a two-level directory structure.
    def __init__(self):
        self.master_directory = {}
    def add_user_directory(self, user, directory):
        self.master_directory[user] = directory
    def search_file(self, user, file_name):
        if user in self.master_directory:
            user_directory = self.master_directory[user]
            return user_directory.search_file(file_name)
        else:
            return None
        
class HierarchicalDirectory: # Represents a hierarchical directory structure.
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}
    def add_file(self, file):
        self.files[file.name] = file
    def add_subdirectory(self, directory):
        self.subdirectories[directory.name] = directory
    def search_file(self, file_name):
        if file_name in self.files:
            return self.files[file_name]
        else:
            for subdirectory in self.subdirectories.values():
                result = subdirectory.search_file(file_name)
                if result:
                    return result
            return None

if __name__ == "__main__":
    print("Single Level Directory:")
    single_level_dir = SingleLevelDirectory()
    single_level_dir.add_file(File("single_level1.txt", "user1"))
    single_level_dir.add_file(File("single_level2.txt", "user2"))
    print(single_level_dir.search_file("single_level1.txt"))
    print("\nTwo Level Directory:")
    two_level_dir = TwoLevelDirectory()
    user1_dir = SingleLevelDirectory()
    user1_dir.add_file(File("two_level1.txt", "user1"))
    user2_dir = SingleLevelDirectory()
    user2_dir.add_file(File("two_level2.txt", "user2"))
    two_level_dir.add_user_directory("user1", user1_dir)
    two_level_dir.add_user_directory("user2", user2_dir)
    print(two_level_dir.search_file("user1", "two_level1.txt"))
    print("\nHierarchical Directory:")
    root_dir = HierarchicalDirectory("root")
    user1_dir = HierarchicalDirectory("user1")
    user1_dir.add_file(File("file1.txt", "user1"))
    user2_dir = HierarchicalDirectory("user2")
    user2_dir.add_file(File("file2.txt", "user2"))
    root_dir.add_subdirectory(user1_dir)
    root_dir.add_subdirectory(user2_dir)
    print(root_dir.search_file("file1.txt"))
