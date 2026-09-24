def clinic():
    print("You've just entered the clinic!")
    
    while True:
        print("Do you take the door on the left or the right?")
        answer = input("Type 'left' or 'right' and hit 'Enter': ").strip().lower()
        
        if answer in ("left", "l"):
            print("This is the Verbal Abuse Room, you heap of parrot droppings!")
            break
        elif answer in ("right", "r"):
            print("Of course this is the Argument Room, I've told you that already!")
            break
        else:
            print("You didn't pick left or right! Try again.\n")

clinic()
