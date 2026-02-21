#1.import random module 
import random

#2.Create subjects
subjects =[
    "Aiswarya Rai Bachchan",
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Narendra Modi",
    "Auto Rickshaw Driver",
]
#3.Create Actions
actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "steals from",
    "celebrates with",
]
places_or_Things=[
    "at Red Fort",
    "in a Mumbai Slum",
    "on the Moon",
    "in a Bollywood Movie",
    "inside Parliament",
    "a plate of Biryani",
    "a cricket stadium",
]
#4. Generate a random headline
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_Things)
    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n"+headline)
    #5.ask user if they want to generate another headline
    user_input=input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input =="no":
        break
#5.print goodbye message
print("\nThank you for using the Fake News Headline Generator! Goodbye!")

       


