import random
import time


class Algorithm:
    def __init__(self):
        self.liste = []
    
    def randomize_list(self, _len: int):
        self.liste = []
        for _ in range(_len):
            self.liste.append(random.randint(0, 10000))

    def is_sorted(self):
        for i in range(len(self.liste) - 1):
            if self.liste[i] > self.liste[i + 1]:
                return False
        return True

    def bubblesort(self, _len: int = 1000):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Bubblesort...")
        for i in range(len(self.liste) - 1):
            for j in range(len(self.liste) - i - 1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j + 1] = self.liste[j + 1], self.liste[j]
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")
    
    def insertionsort(self, _len: int = 1000):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Insertionsort...")
        for i in range(1, len(self.liste)):
            key = self.liste[i]
            j = i - 1
            while j >= 0 and key < self.liste[j]:
                self.liste[j + 1] = self.liste[j]
                j -= 1
            self.liste[j + 1] = key
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")
    
    def selectionsort(self, _len: int = 1000):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Selectionsort...")
        for i in range(len(self.liste)):
            min_index = i
            for j in range(i + 1, len(self.liste)):
                if self.liste[j] < self.liste[min_index]:
                    min_index = j
            self.liste[i], self.liste[min_index] = self.liste[min_index], self.liste[i]
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")
    
    def quicksort(self, _len: int = 1000):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Quicksort...")
        self._quicksort(0, len(self.liste) - 1)
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")

    def _quicksort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quicksort(low, pi - 1)
            self._quicksort(pi + 1, high)
    
    def _partition(self, low, high):
        pivot = self.liste[high]
        i = low - 1
        for j in range(low, high):
            if self.liste[j] < pivot:
                i += 1
                self.liste[i], self.liste[j] = self.liste[j], self.liste[i]
        self.liste[i + 1], self.liste[high] = self.liste[high], self.liste[i + 1]
        return i + 1
    
    def mergesort(self, _len: int = 1000):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Mergesort...")
        self._mergesort(self.liste)
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")

    def _mergesort(self, liste):
        if len(liste) > 1:
            mid = len(liste) // 2
            left = liste[:mid]
            right = liste[mid:]

            self._mergesort(left)
            self._mergesort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    liste[k] = left[i]
                    i += 1
                else:
                    liste[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                liste[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                liste[k] = right[j]
                j += 1
                k += 1

    def bogosort(self, _len: int = 10):
        if self.is_sorted() or len(self.liste) == 0 or _len != len(self.liste):
            self.randomize_list(_len)
        start = time.time()
        print("Starte Bogosort...")
        while not self.is_sorted():
            random.shuffle(self.liste)
        end = time.time()
        print(f"Benötigte Zeit: {end - start} Sekunden bei {len(self.liste)} Elementen.")


        

        


if __name__ == "__main__":
    algorithms = Algorithm()

    algorithms.bubblesort(10000)
    algorithms.insertionsort(10000)
    algorithms.selectionsort(10000)
    algorithms.quicksort(10000)
    algorithms.mergesort(10000)
    algorithms.bogosort()