def count_sheeps(sheep):
  # TODO May the force be with you
    return sum( bool(i) for i in sheep)

list = [True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True , True,  True,  True,  True , False, False, True,  True ]
print(count_sheeps(list))