def twoSum(nums, target):
        compliment_map = {}
        for i, element in enumerate(nums):
            compliment = target - element
            if compliment in compliment_map:
                return [compliment_map[compliment],  i]
            else:
                compliment_map[element] = i
                
        #This solution runs in O(N) time but needs space for the dict.
        #Could also look at sorting the array first (O(nlogn)) then for every element, running a binary
        #search for the compliment of that value O(N*logN) Which increases the runtime but takes up O(1)
        #Space.
        
if __name__ == "__main__":
    example_array = [1,8,4,5,6,3,2,14]
    target = 18
    print(twoSum(example_array, target))