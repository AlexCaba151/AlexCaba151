# Adventure Game
"""
Welcome to the Enchanted Forest Adventure!
Embark on a journey through a magical forest filled with mystical creatures and hidden wonders.
Your choices will shape your destiny, so choose wisely and see where the path takes you!
"""
user_choice_1 = input("Choose your item: GLOWING CRYSTAL or SHIMMERING DAGGER? ")

if user_choice_1.upper() == "GLOWING CRYSTAL":
    # Level 2 - Glowing Crystal Scenario
    print("As you touch the glowing crystal, a magical light surrounds you. You hear whispers from the trees.")
    print("Do you want to LISTEN to the whispers or MOVE deeper into the forest?")
    user_choice_2_crystal = input("Your choice: LISTEN or MOVE? ")

    if user_choice_2_crystal.upper() == "LISTEN":
        # Level 3 - Listen to Whispers Scenario
        print("The whispers reveal a hidden path. You follow it and encounter a mystical unicorn.")
        print("Do you want to RIDE the unicorn or OFFER a gift?")
        user_choice_3_unicorn = input("Your decision: RIDE or OFFER? ")

        if user_choice_3_unicorn.upper() == "RIDE":
            print("Congratulations! The unicorn takes you to a secret glade filled with treasures.")
        elif user_choice_3_unicorn.upper() == "OFFER":
            print("The unicorn appreciates your gesture and grants you a magical charm for protection.")
        else:
            print("Invalid choice. The mystical energy fades, and you lose the opportunity for a magical encounter.")

    elif user_choice_2_crystal.upper() == "MOVE":
        # Level 3 - Move Deeper into the Forest Scenario
        print("You venture deeper into the forest, where you encounter a mischievous fairy.")
        print("Do you want to PLAY with the fairy or ASK for guidance?")
        user_choice_3_fairy = input("Your decision: PLAY or ASK? ")

        if user_choice_3_fairy.upper() == "PLAY":
            print("The fairy guides you to a hidden grove where rare herbs grow. You gain special knowledge.")
        elif user_choice_3_fairy.upper() == "ASK":
            print("The fairy shares ancient wisdom and grants you the ability to communicate with animals.")
        else:
            print("Invalid choice. The fairy loses interest, and the magical connection fades away.")

    else:
        print("Invalid choice. The glowing crystal's magic repels you, and you find yourself lost in the forest.")

elif user_choice_1.upper() == "SHIMMERING DAGGER":
    # Level 2 - Shimmering Dagger Scenario
    print("You grab the shimmering dagger, and a surge of power flows through you. A shadowy figure appears.")
    print("Do you want to CHALLENGE the figure or FOLLOW its lead?")
    user_choice_2_dagger = input("Your choice: CHALLENGE or FOLLOW? ")

    if user_choice_2_dagger.upper() == "CHALLENGE":
        # Level 3 - Challenge the Shadowy Figure Scenario
        print("You engage in a fierce battle with the figure and discover it's a shape-shifting guardian.")
        print("Do you want to ALLY with the guardian or TAKE its cloak for protection?")
        user_choice_3_guardian = input("Your decision: ALLY or TAKE? ")

        if user_choice_3_guardian.upper() == "ALLY":
            print("Congratulations! The guardian becomes your ally and leads you to hidden treasures.")
        elif user_choice_3_guardian.upper() == "TAKE":
            print("You take the cloak, gaining invisibility for a short time. Use it wisely.")
        else:
            print("Invalid choice. The guardian senses your hesitation and disappears into the shadows.")

    elif user_choice_2_dagger.upper() == "FOLLOW":
        # Level 3 - Follow the Shadowy Figure Scenario
        print("You cautiously follow the figure and discover a secret gathering of magical beings.")
        print("Do you want to JOIN the gathering or WATCH from the shadows?")
        user_choice_3_gathering = input("Your decision: JOIN or WATCH? ")

        if user_choice_3_gathering.upper() == "JOIN":
            print("You become part of the magical gathering, gaining new skills and knowledge.")
        elif user_choice_3_gathering.upper() == "WATCH":
            print("You observe in silence, learning ancient rituals and gaining insights into mystical arts.")
        else:
            print("Invalid choice. The magical beings sense your uncertainty and vanish into thin air.")

    else:
        print("Invalid choice. The power of the shimmering dagger overwhelms you, and you lose control.")

else:
    print("Invalid choice. The forest reacts to your indecision, and you find yourself in a dense fog.")

# The adventure concludes with unique outcomes based on the user's choices, I hope you  enjoy it :D
