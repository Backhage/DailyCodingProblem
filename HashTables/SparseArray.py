class SparseArray:
    def __init__(self, arr, size):
        self.n = size
        self._dict = {}

        for i, e in enumerate(arr):
            if e != 0:
                self._dict[i] = e

    def _check_bounds(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("Out of bounds")

    def get(self, i):
        self._check_bounds(i)
        return self._dict.get(i, 0)

    def set(self, i, val):
        self._check_bounds(i)
        if i in self._dict and val == 0:
            del self._dict[i]
        else:
            self._dict[i] = val
