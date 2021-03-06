'''
multiple inheritance
'''
class A:
	def foo(self) -> int:
		return 1

class B:
	def bar(self) -> int:
		return 2

class C( A, B ):
	def call_foo_bar(self) -> int:
		a = self.foo()
		a += self.bar()
		return a

	## extend foo ##
	def foo(self) -> int:
		a = A.foo(self)
		a += 100
		return a

def main():
	a = A()
	TestError( a.foo()==1 )
	b = B()
	TestError( b.bar()==2 )

	c = C()
	TestError( c.foo()==101 )
	TestError( c.bar()==2 )

	TestError( c.call_foo_bar()==103 )
