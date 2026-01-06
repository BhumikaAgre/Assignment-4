Task_1
try:
    print("Reading file content:")

    with open("sample.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

Task_2
text=input("Enter text to write to the file:")
with open("output.txt",'w')as file:
    file.write(text + "\n")
    print("Data succesfully written to the output.txt.")

additional_text=input("Enter the additional text to append:")
with open("output.txt","a") as file:
    file.write(additional_text + "\n")
    print("Data successfully append.")
    print("\nFinal content of output.txt.")

with open("output.txt","r") as file:
    print(file.read())
