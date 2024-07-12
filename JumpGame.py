class Solution:   
       

    def main():
       nums = [3,2,1,0,4]

       jump_distance = 0
       
       for n in nums:
        if jump_distance < 0:
            print(False)
        if n > jump_distance:
            jump_distance = n
        jump_distance = jump_distance-1

        print(True)