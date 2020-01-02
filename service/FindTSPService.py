import math


# Service class to calculate two sided prime
class FindTSPService:

    def __init__(self):
        pass

    # Method to determine whether a number is a prime or not
    @staticmethod
    def find_prime(number: int) -> bool:
        if number <= 1:
            return False
        for i in range(2, math.floor(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    # Method to determine whether a number is a Two Sided prime or not
    @staticmethod
    def find_tsp_service(number: int) -> bool:
        flag = FindTSPService.find_prime(number)
        if flag:
            tmp = number
            count = 0
            tmp = int(tmp / 10)
            # Determining right truncate-able prime
            while tmp != 0:
                count = count + 1
                if not FindTSPService.find_prime(tmp):
                    return False
                tmp = int(tmp / 10)
            tmp = number
            if int(tmp / 10) != 0:
                tmp = tmp % (10 * count)
            else:
                tmp = 0
            # Determining left truncate-able prime
            while tmp != 0:
                count = count - 1
                if not FindTSPService.find_prime(tmp):
                    return False
                if int(tmp / 10) == 0:
                    tmp = 0
                else:
                    tmp = tmp % (10 * count)
        else:
            return False
        return True
