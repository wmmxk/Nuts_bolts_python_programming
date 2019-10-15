import foo
print(dir(foo))
print(foo.__path__)

import foo.my_math as mm
import foo.level2.another_mod as am
# import foo.level2 as l2
# l2.another_mod.add(6, 7) 
# alias for a folder is not allowed; for a module file is OK

print(am.add(4, 5))
print(mm.add(3, 4))
