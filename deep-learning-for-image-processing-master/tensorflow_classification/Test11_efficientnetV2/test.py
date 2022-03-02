import itertools

bid = itertools.count(0)
print(bid)
get_norm_name = lambda: 'batch_normalization' + ('' if not next(
    bid) else '_' + str(next(bid) // 2))
print(get_norm_name())
cid = itertools.count(0)
print(cid)
get_conv_name = lambda: 'conv2d' + ('' if not next(cid) else '_' + str(
    next(cid) // 2))
print(next(cid))
print(get_conv_name())
iterator = (itertools.count(start=1, step=2))

# prints a odd list of integers
print("Odd list:",
      list(next(iterator) for _ in range(5)))
print(next(iterator))
