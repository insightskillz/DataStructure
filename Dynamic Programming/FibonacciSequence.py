from line_profiler import LineProfiler
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

lp = LineProfiler(fibonacci(200))

print(lp.print_stats())