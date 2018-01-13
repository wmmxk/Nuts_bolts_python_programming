# This code is to show how to invoke different functions in a module using getattr function
import funs
fun1 = getattr(funs,"fun1")
print fun1(1,2)


fun2 = getattr(funs,"fun2")
print fun2(1,2)



