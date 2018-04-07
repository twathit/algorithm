#在一个长度为n的数组里所有数字都在0~n-1的范围内，找出数组中的重复数字

class Solution:
    def countDuplicates(self, nums=[]):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        for i in range(len(nums)):
            if (nums[i]<0 or nums[i]>len(nums)-1):
                return None
        
        duplicate=[]
        for i in range(len(nums)):
            while(nums[i]!=i):
                if nums[i]==nums[nums[i]] and nums[i] not in duplicate:
                    duplicate.append(nums[i])
                    break
                #nums[i],nums[nums[i]]=nums[nums[i]],nums[i]
                temp=nums[i]
                nums[i]=nums[temp]
                nums[temp]=temp
        #return list(set(duplicate))
        return duplicate

if __name__ == '__main__':
    s=Solution()
    nums=s.countDuplicates([2,3,1,0,2,5,3])
    print('The duplicate numbers are:',[i for i in nums if nums is not None])