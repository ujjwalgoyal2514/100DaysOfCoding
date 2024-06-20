"""Given three non-collinear points whose co-ordinates are p(p1, p2), q(q1, q2) and r(r1, r2) in the X-Y plane. Return the number of integral / lattice points strictly inside the triangle formed by these points.
Note: - A point in the X-Y plane is said to be an integral / lattice point if both its coordinates are integral.

Examples

Input: p = (0,0), q = (0,5), r = (5,0)
Output: 6
Explanation: 

As shown in figure, points (1,1) (1,2) (1,3) (2,1) (2,2) and (3,1) are the integral points inside the triangle. So total 6 are there.
Input: p = (62,-3), q = (5,-45), r = (-19,-23)
Output: 1129
Explanation: There are 1129 integral points in the triangle formed by p, q and r.
Expected Time Complexity: O(Log2109)
Expected Auxillary Space: O(1)

Constraints:
-109 ≤ x-coordinate, y-coordinate ≤ 109"""
from math import gcd
class Solution:
    def InternalCount(self, p, q, r):
        x1,y1=p[0],p[1]
        x2,y2=q[0],q[1]
        x3,y3=r[0],r[1]
        m1,m2,m3=abs(x1-x2),abs(x1-x3),abs(x2-x3)
        n1,n2,n3=abs(y1-y2),abs(y1-y3),abs(y2-y3)
        a,b,c=gcd(m1,n1),gcd(m2,n2),gcd(m3,n3)
        x=a+b+c
        area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        res=(area-x+2)//2
        return res