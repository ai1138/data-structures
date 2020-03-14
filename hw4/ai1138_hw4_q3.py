def print_triangle(n):
    if(n == 1):
        print('*')
    else:
        print_triangle(n - 1)
        print((n * '*'))
def printReverse(n):
    if(n == 1):
        print('*')
    else:
        print((n * '*'))
        printReverse(n-1)
def print_oposite_triangles(n):
    printReverse(n)
    print_triangle(n)

def print_ruler(n):
    if n == 1:
        print('-')
    else:
        print_ruler(n - 1)
        print('-' * n)
        print_ruler(n - 1)
