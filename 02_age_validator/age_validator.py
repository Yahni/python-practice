# Simple Python script to validate the user's age

def main():
    try:
        age_input = input("How old are you? ")
        age = int(age_input)
    except ValueError:
        print("Please enter a valid number.")
        return

    if age >= 18:
        print("You’re legally an adult!")
    else:
        years_left = 18 - age
        print(f"Not yet—come back in {years_left} year(s).")

if __name__ == "__main__":
    main()
