class Guitar:
    def play(self):
        return "Playing the guitar"

def start_playing(sth):
    return sth.play()

guitar = Guitar()
start_playing(guitar)
