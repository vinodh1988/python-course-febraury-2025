def fileLineAppender(sno: int, name: str, city: str, filename: str) -> None:
    try:
        with open(filename, 'a') as file:
            file.write(f"{sno},{name},{city}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# fileLineAppender(1, 'John Doe', 'New York', 'data.txt')
while True:
    sno = int(input("Enter serial number: "))
    name = input("Enter name: ")
    city = input("Enter city: ")
    fileLineAppender(sno, name, city, 'textfiles/data.txt')
    
    cont = input("Do you want to add another entry? (yes/no): ").strip().lower()
    if cont != 'yes':
        break