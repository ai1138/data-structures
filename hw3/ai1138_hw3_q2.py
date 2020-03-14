import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()
class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __repr__(self):
        lst = []
        for i in range(self.n):
            lst.append(self[i])
        return str(lst)
    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1
    def insert(self, index, val):
        if not (0 <= index <= self.n):
            raise IndexError('Invalid Index')
        self.append(val)
        for i in range(self.n-1,index,-1):
            temp = self.data_arr[i-1]
            self.data_arr[i-1] = self.data_arr[i]
            self.data_arr[i] = temp
    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def pop(self,index = -2):
        if(self.n == 0):
            raise IndexError('Invalid Index')
        if(index == -2):
            index = self.n -1
            temp = self.data_arr[index]
            self.data_arr[index] = None
        else:
            temp = self.data_arr[index]
            for i in range(index,self.n-1):
                self.data_arr[i], self.data_arr[i+1] = self.data_arr[i+1],self.data_arr[i]
            self.data_arr[self.n - 1] = None
        if self.n < (0.25 * self.capacity):
            self.capacity = 0.5
        self.n-=1
        return temp

    def __getitem__(self, ind):
        if not(0 <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not(0 <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)
def main():
    arr = ArrayList()
    for i in range(23):
        arr.append(i)
    arr.pop()
    print(arr)
main()
