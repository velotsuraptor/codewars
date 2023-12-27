class Primes:
    @staticmethod
    def stream():
        n = 2
        while True:
            yield n
            n+1