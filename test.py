import pycraigslist

site = pycraigslist.housing.apa(site="sfbay")

if __name__ == "__main__":
    for s in site.search(limit=10):
        print(s)
