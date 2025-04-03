import math
from tabulate import tabulate
from utils import get_float_input, get_precision_input

def cos_taylor(x, eps=1e-10, max_iter=500):
   
    result = 1.0  
    term = 1.0    
    
    for n in range(1, max_iter + 1):

        term = -term * x**2 / ((2*n-1) * (2*n))
        result += term
        
      
        if abs(term) < eps:
            return result, n
    
 
    return result, max_iter

def run_task1():

    x = get_float_input("Enter the value of x (radians): ")
    eps = get_precision_input()
    
    taylor_result, terms = cos_taylor(x, eps)
    math_result = math.cos(x)
    
 
    headers = ["x", "n", "F(x)", "math F(x)", "eps"]
    data = [[f"{x:.2f}", f"{terms}", f"{taylor_result:.12f}", f"{math_result:.12f}", f"{eps:.2e}"]]
    
    print("\nMy table for task1")
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    
    