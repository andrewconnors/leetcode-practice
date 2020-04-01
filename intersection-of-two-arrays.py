def get_intersection_fast(nums1, nums2):
    arr_dict = {}
    #O(N)
    for item in nums1:
        if item not in arr_dict:
            arr_dict[item] = 1
    #O(N)
    for item in nums2:
        if item in arr_dict:
            arr_dict[item] = 2
    #O(N)
    return [x for x in arr_dict.keys() if arr_dict[x] == 2]

def get_intersection_space_conscious(nums1, nums2):
    result = []
    i = 0
    j = 0
    nums1.sort()
    nums2.sort()
    while i < len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            if not (len(result) and nums1[i] != result[len(result)-1]):
                result.append(nums1[i])
        i += 1
        j += 1
    return result

if __name__ == "__main__":
    ex_nums1 = [1,2,2,1]
    ex_nums2 = [2,2]
    print(get_intersection_fast(ex_nums1, ex_nums2))
    print(get_intersection_space_conscious(ex_nums1, ex_nums2))

    '''
    In the first solution the runtime is O(n) but the space complexity is also potentially O(n)

    In solution number two, commented out, we solve the space issue while sacrificing time to O(nlogn) for the sort
    '''