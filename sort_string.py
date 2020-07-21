def sort_string(words):
    words = words.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    print(" ".join(words))


sort_string("banana ORANGE apple")
