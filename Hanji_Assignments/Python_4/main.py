def create_greeting(name) :
    return f"Hello {name}! Welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!\n"

try: 
    name = input("\nEnter your Name: ")
    greet = create_greeting(name)

    print (f"\nThe Message is: \n{greet} ")

except ValueError:
        print("\nInvalid input: Please enter a valid name.")