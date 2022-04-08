def makeup(girlfriend):
    def add_makeup():
        print('Added Face Makeup')
        print('She programs!')
        print('She is stable')
        return girlfriend()
    return add_makeup
@makeup
def girlfriend():
    print("Got pretty smile and pretty face")
    print("Has a cool hairstyle!")

girlfriend()
