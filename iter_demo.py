# Inspired by the following YouTube video
# ---------------------------------------
# Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
# by Corey Schafer
# https://youtu.be/jTYiNjvnHZY

# Implements all the necessary methods of an iterator
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

# A generator function that yields values one by one creating an iterator
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# Custom print function using the iterator features
def my_iterable_print(an_iterable):
    an_iterator = iter(an_iterable)
    while True:
        try:
            item = next(an_iterator)
            print(item)
        except StopIteration:
            break
    
# nums = [1, 2, 3]
# my_iterable_print(nums)

# nums = MyRange(1, 10)
# my_iterable_print(nums)

nums = my_range(1, 10)
my_iterable_print(nums)

# for num in nums:
#     print(num)
