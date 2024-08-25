from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS,COLS=len(matrix), len(matrix[0])
        
        def find_row()->int:
            row = 0            
            
            while row<ROWS:
                if matrix[row][0]<=target<=matrix[row][COLS-1]:
                    return row
                row+=1
            
            return -1
        
        def search(row)->bool:
            l,r = 0,COLS-1
            
            while l<=r:
                mid = int((l+r)/2)
                
                if matrix[row][mid]<target:
                    l=mid+1
                elif matrix[row][mid]>target:
                    r=mid-1
                else:
                    return True
            return False
        
        row = find_row()
        if row == -1 : return False
        
        return search(row)
        
        
# print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]],10))
print(Solution().searchMatrix([[1]],1))