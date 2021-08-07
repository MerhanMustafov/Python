import math
def get_primes(num_lst):
    for ind in range(len(num_lst)-1,-1 , -1):
        number = num_lst[ind]
        if number > 1:
            for n in range(2, int(math.sqrt(number)+1)):
                if (number % n) == 0:
                    num_lst.remove(number)
                    break
        else:
            num_lst.remove(number)

    for x in num_lst:
        yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# test zero
# import unittest
#
# class Tests(unittest.TestCase):
#     def test_zero(self):
#         res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
#         self.assertEqual(res, [2, 3, 5])
#
# if __name__ == '__main__':
#     unittest.main()