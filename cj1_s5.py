import math
import numpy as np

def sin_table(lower,upper,entries):
    x_array= np.linspace(lower,upper, entries)
    sin_x_array= np.sin(x_array)
    merged= np.column_stack((x_array,sin_x_array))
    return merged

def main():

    print('x \t\t|\t\t sin(x)')
    table= sin_table(0,2*math.pi,1000)
    for i in table:
        print(f'{i[0]:.4f}\t\t|\t\t{i[1]:.4f}')

if __name__ == "__main__":
    main()


