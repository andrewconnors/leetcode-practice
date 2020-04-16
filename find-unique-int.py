def find_unique_int(arr):
    unique_id = 0

    for item in arr:
        unique_id ^= item
    
    return unique_id
if __name__=="__main__":
    arr = [1,2,4,3,4,5,1,3, 5]
    print(find_unique_int(arr))