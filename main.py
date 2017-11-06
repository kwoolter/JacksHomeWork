def main():
    name = ["Jack", "Rosie", "Jane", "Keith"]
    verb = ["kicks", "throws", "picks up", "punches"]
    noun = ["100 tons.", "a dinosuar.", "an Iphone.", "a car."]

    from random import randint
    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words - 1)
        word_picked = words[num_picked]
        return word_picked

    print(pick(name), pick(verb), pick(noun))

    while True:
        print(pick(name), pick(verb), pick(noun))
