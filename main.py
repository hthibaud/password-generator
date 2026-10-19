from utils.generation_functions import generate_password

def main():
    try:
        generate_password()
    except KeyboardInterrupt:
        print("\nBye")
main()