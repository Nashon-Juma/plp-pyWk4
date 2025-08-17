def process_file():
    """Reads a file, modifies its content, and writes to a new file with error handling"""
    try:
        # Get input filename from user
        input_filename = input("Enter the input filename: ")
        
        # Read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Get output filename from user
        output_filename = input("Enter the output filename: ")
        
        # Write to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File processed successfully! Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    process_file()