# give 3 examples of multiple inheritance in python
class A:
    def method_a(self):
        return "Method A from class A"
class B:
    def method_b(self):
        return "Method B from class B"
class C(A, B):
    def method_c(self):
        return "Method C from class C"
c = C()
print(c.method_a())  # Output: Method A from class A
print(c.method_b())  # Output: Method B from class B
print(c.method_c())  # Output: Method C from class C    

class X:
    def method_x(self):
        return "Method X from class X"
class Y:
    def method_y(self):
        return "Method Y from class Y"
class Z(X, Y):
    def method_z(self):
        return "Method Z from class Z"
z = Z()
print(z.method_x())  # Output: Method X from class X
print(z.method_y())  # Output: Method Y from class Y
print(z.method_z())  # Output: Method Z from class Z

class P:
    def method_p(self):
        return "Method P from class P"
class Q:
    def method_q(self):
        return "Method Q from class Q"
class R(P, Q):
    def method_r(self):
        return "Method R from class R"
r = R()
print(r.method_p())  # Output: Method P from class P
print(r.method_q())  # Output: Method Q from class Q
print(r.method_r())  # Output: Method R from class R