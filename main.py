from DataRepo import DataRepo
repo = DataRepo("test_houses.csv")   # one-time setup
rows = repo.load()                    # call whenever needed
rows2 = repo.load() 
#load function from DataRepo call