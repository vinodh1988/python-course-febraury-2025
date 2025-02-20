def process(plist: list, callback: callable):
    print("Going to process the list")
    for p in plist:
        callback("Preprocessed"+p)
    print("Done processing the list")
    #return "success"

def userprocess(product):
    print(f"User processing product: {product}")

process(["Computer", "Printer", "Monitor"], userprocess)
