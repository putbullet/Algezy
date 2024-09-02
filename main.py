import matix

text_art_1 = """

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
"""

text_art_2 = """  ____ ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ _________ ____ ____ ____ ____ _________ 
||C |||H |||O |||S |||E |||       |||O |||N |||       |||T |||H |||E |||       |||M |||E |||N |||U |||       ||
||__|||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||_______|||__|||__|||__|||__|||_______||
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|
"""
def print_menu():
    print(text_art_1)
    print("=======================")
    print(text_art_2)
    print("=======================\n")
    print("1. Matrix Calculations")
    print("2. Graphs and Charts")
    print("3. Solve Equations")
    print("4. Exit")

def main():
    print_menu()
    while True:
        try:
            number = int(input("Enter the number of your choice: "))
            
            if number == 1:
                matix.print_matrix_input_instructions()  # Print instructions when matrix calculations are selected
                matix.matrix_menu()
            elif number == 2:
                print("Graphs and Charts functionality not yet implemented.")
            elif number == 3:
                print("Solve Equations functionality not yet implemented.")
            elif number == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()