Library = {"James": ["Gaint Peach","Gainter peach","Gaintest peach"], "Moby": ["Dick", "Richard", "Rich"], "Decartes": ["Meditations1", "Meditations2", "Meditations3"]}
Search = input("What Author do you want?: ")
discography = Library.get(Search, "This authour is not apart of the library")
print(", ".join(discography))