import math


class FindTSPService:

    @staticmethod
    def find_prime(number: int) -> bool:
        if number == 2 or number == 3:
            return True
        sq = int(math.sqrt(number))
        for i in range(2, sq + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def find_tsp_service(number: int) -> bool:
        if number <= 1:
            return False

        flag = FindTSPService.find_prime(number)
        if flag:
            tmp = number
            count = 0
            tmp = int(tmp / 10)
            while tmp != 0:
                count = count + 1
                print(tmp)
                if tmp <= 1:
                    return False
                flag = FindTSPService.find_prime(number)
                if not flag:
                    return False
                tmp = int(tmp / 10)
            tmp = number
            if int(tmp / 10) != 0:
                tmp = tmp % (10 * count)
            else:
                tmp = 0
            while tmp != 0:
                count = count - 1
                if tmp <= 1:
                    return False
                flag = FindTSPService.find_prime(number)
                if not flag:
                    return False
                if int(tmp / 10) == 0:
                    tmp = 0
                else:
                    tmp = tmp % (10 * count)
        else:
            return False
        return True
