# coroutines in python
#coroutines are used when our function takes time in initializing. but once our function is initialized then it works properly
def searcher():
    import time
    book= "I am reading a book which contains a good content"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("content")
search.close()
#search("This")      as search is closed this line is not callable