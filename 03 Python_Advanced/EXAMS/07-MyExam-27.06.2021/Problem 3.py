from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    count = 1
    while args:
        if count == 1:
            kwargs["a"] += args.popleft()

        elif count == 2:
            kwargs["s"] = kwargs["s"] - args.popleft()

        elif count == 3:
            if args[0] == 0:
                args.popleft()
                count += 1
                continue
            else:
                kwargs["d"] = kwargs["d"] / args.popleft()

        elif count == 4:
            kwargs["m"] = kwargs["m"] * args.popleft()
            if args:
                count = 1
                continue
        count += 1
    return kwargs


# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(6, a=0, s=0, d=0, m=0))
