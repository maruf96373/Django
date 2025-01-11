class FileManager:
    """Context manager to handle file operations safely."""
    
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Open the file and return the file object."""
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the file and handle exceptions if any."""
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate the exception if it occurs


# Example Usage
try:
    with FileManager("example.txt", "w") as file:
        file.write("This is a test file.\n")
        file.write("It ensures safe file handling.\n")
        # Uncomment the line below to simulate an exception
        # raise ValueError("An error occurred while writing to the file!")
except Exception as e:
    print(f"Handled exception: {e}")

# Reading the file to verify content
try:
    with FileManager("example.txt", "r") as file:
        print("\nFile Content:")
        print(file.read())
except Exception as e:
    print(f"Handled exception: {e}")
