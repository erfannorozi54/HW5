import unittest
from shape import Point, Shape, Line, Triangle, Rectangle

# class Test(unittest.TestCase):
#     ## ---------------- HW5 TEST1 ----------------
#     def test1(self):
#         p1 = Point(2.5, 3)
#         print(p1)
#         str = p1.__str__()
#         self.assertTrue(str.find("2.5") != -1)
#         self.assertTrue(str.find("3") != -1)

#     ## ---------------- HW5 TEST2 ----------------
#     def test2(self):
#         p1 = Point(2.5, 3)
#         p2 = Point(3, 4)
#         add = p1+p2
#         self.assertTrue(add.x == p1.x+p2.x)
#         self.assertTrue(add.y == p1.y+p2.y)

#     ## ---------------- HW5 TEST3 ----------------
#     def test3(self):
#         p1 = Point(2.5, 3)
#         p2 = Point(3, 4)
#         sub = p1-p2
#         self.assertTrue(sub.x == p1.x-p2.x)
#         self.assertTrue(sub.y == p1.y-p2.y)

#     ## ---------------- HW5 TEST4 ----------------
#     def test4(self):
#         p1 = Point(2.5, 3)
#         p2 = Point(3, 4)
#         print(p1.length())
#         self.assertAlmostEqual(p1.length(), 3.905, places=2)
#         self.assertAlmostEqual(p2.length(), 5, places=2)

#     ## ---------------- HW5 TEST5 ----------------
#     def test5(self):
#         s = Shape()
#         with self.assertRaises(RuntimeError):
#             print(s.perimeter()) # runtime error - no vertex added yet

#     ## ---------------- HW5 TEST6 ----------------
#     def test6(self):
#         s = Shape()
#         s.add_vertex(Point(0, 0))
#         s.add_vertex(Point(3, 0))
#         s.add_vertex(Point(0, 4))
#         print(s)
#         str = s.__str__()
#         self.assertTrue(str.find("3") != -1) # find number of vertices in the output

#     ## ---------------- HW5 TEST7 ----------------
#     def test7(self):
#         s = Shape()
#         s.add_vertex(Point(0, 0))
#         s.add_vertex(Point(3, 0))
#         s.add_vertex(Point(0, 4))
#         self.assertAlmostEqual(s.perimeter(), 12, places=2)

#     ## ---------------- HW5 TEST8 ----------------
#     def test8(self):
#         p1 = Point(-1, 2)
#         p2 = Point(1, 4)
#         l = Line(p1, p2)
#         print(l)
#         str = l.__str__()
#         self.assertTrue(str.find("-1") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("2") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("1") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("4") != -1) # find value of vertices in the output
#         self.assertAlmostEqual(l.perimeter(), 2.828, places=2)

#     ## ---------------- HW5 TEST9 ----------------
#     def test9(self):
#         p1 = Point(-1, 2)
#         p2 = Point(1, 4)
#         l = Line(p1, p2)
#         self.assertAlmostEqual(l.area(), 0, places=2)

#     ## ---------------- HW5 TEST10 ----------------
#     def test10(self):
#         p1 = Point(0, 0)
#         p2 = Point(0, 3)
#         p3 = Point(0, 4)
#         with self.assertRaises(RuntimeError):
#             t = Triangle(p1, p2, p3) # runtime error - vertices on one line

#     ## ---------------- HW5 TEST11 ----------------
#     def test11(self):
#         p1 = Point(0, 0)
#         p2 = Point(0, 3)
#         p3 = Point(4.1, 0)
#         t = Triangle(p1, p2, p3)
#         print(t)
#         str = t.__str__()
#         self.assertTrue(str.find("0") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("3") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("4.1") != -1) # find value of vertices in the output

#     ## ---------------- HW5 TEST12 ----------------
#     def test12(self):
#         p1 = Point(0, 0)
#         p2 = Point(0, 3)
#         p3 = Point(4.1, 0)
#         t = Triangle(p1, p2, p3)
#         self.assertAlmostEqual(t.area(), 6.15, places=2)

#     ## ---------------- HW5 TEST13 ----------------
#     def test13(self):
#         p1 = Point(0, 0)
#         p2 = Point(2, 2)
#         r = Rectangle(p1, p2)
#         print(r)
#         str = r.__str__()
#         self.assertTrue(str.find("0") != -1) # find value of vertices in the output
#         self.assertTrue(str.find("2") != -1) # find value of vertices in the output

#     ## ---------------- HW5 TEST14 ----------------
#     def test14(self):
#         p1 = Point(0, 0)
#         p2 = Point(2, 2)
#         r = Rectangle(p1, p2)
#         self.assertAlmostEqual(r.area(), 4, places=2)


# if __name__=='__main__':
#     unittest.main(verbosity=0)