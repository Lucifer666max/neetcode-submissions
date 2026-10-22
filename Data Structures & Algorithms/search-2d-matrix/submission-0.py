class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        low=0
        high=m-1

        while (low<=high):
            mid=(low+high)//2
            if target > matrix[mid][-1]:
                low=mid+1
            elif target < matrix[mid][0]:
                high=mid-1
            else:
                break

        if not (low<=high):
            return False

        mid=(low+high)//2
        l=0
        r=n-1
        while l<=r:
            mm=(l+r)//2
            if target>matrix[mid][mm]:
                l=mm+1
            elif target<matrix[mid][mm]:
                r=mm-1
            else:
                return True
        return False