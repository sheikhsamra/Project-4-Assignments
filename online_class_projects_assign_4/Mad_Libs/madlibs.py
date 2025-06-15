def mad_libs():
    print("Let\'s play Mad Libs! fill in the blanj=k with your own words.")

    name = input("Give me a name: ")
    place = input("Live me a place: ")
    funny_adj = input("Give me a funny adjactive: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f'''
Once upon a time, there was a person named {name} who lived in {place}.
one day, they found a {funny_adj} {random_object} that blonged to a {animal}.
The {animal} was very upset and started to {action_verb} around.
{name} couldn't help but laugh and shouted "{funny_exclamation}!".'''
    print("\nHere is your Mad Lib story ")
    print(story)
if __name__ =="__main__":
    mad_libs()