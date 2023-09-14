"""
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)


"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        n=len(A)
        m=len(A[0])
        for i in range(m):
            s=0
            for j in range(n):
                if A[j][i]==1:
                    s+=1
                    A[j][i]=s
                else:
                    s=0
        resultArea=0
        for i in range(n):
            firstMinLeft=[]
            firstMinRight=[]
            st=[]
            for j in range(m):
                while st and st[-1][0]>=A[i][j]:
                    st.pop()
                if st:
                    firstMinLeft.append(st[-1][1])
                else:
                    firstMinLeft.append(-1)
                st.append((A[i][j],j))
            st=[]
            for j in range(m-1,-1,-1):
                while st and st[-1][0]>=A[i][j]:
                    st.pop()
                if st:
                    firstMinRight.append(st[-1][1])
                else:
                    firstMinRight.append(m)
                st.append((A[i][j],j))
            firstMinRight=firstMinRight[::-1]
            for j in range(m):
                area=(firstMinRight[j]-firstMinLeft[j]-1)*A[i][j]
                resultArea=max(area,resultArea)
        return resultArea
