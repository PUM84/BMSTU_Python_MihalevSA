import sys
sys.path.append('.')

import mymodule
print("Версия mymodule:", mymodule.VERSION)
mymodule.hello()

from mymodule import calc_expression, process_array
y1, y2 = calc_expression(1.5)
print(f"y1={y1:.3f}, y2={y2:.3f}")
arr, mult, s = process_array(8)
print(f"mult={mult:.3f}, sum={s:.3f}")

import mymodule as mm
mm.hello()

print(hello())
print(process_array)

import mypackage.mod1
print(mypackage.mod1.unique_elements([1,2,2,3]))

from mypackage.mod2 import is_prime
print(is_prime(17))

import mypackage.subpkg.extra
print(mypackage.subpkg.extra.multiply(3, 7))
