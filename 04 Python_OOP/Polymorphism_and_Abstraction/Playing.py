
def start_playing(obj):
    return obj.play()



class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
start_playing(guitar)
class Children:
    def play(self):
        return "Children are playing"

piano = Children()
print(start_playing(piano))


# import unittest

# class PlayingTest(unittest.TestCase):
#     def test(self):
#         class Test:
#             def play(self):
#                 return "test"
#         res = start_playing(Test())
#         self.assertEqual(res, "test")

# if __name__ == '__main__':
#     unittest.main()
        
