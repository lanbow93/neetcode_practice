def longest_consecutive(nums):
    nums.sort()
    final_count = 1
    current_count = 1
    print(nums)
    for i in range(1, len(nums)):
        if(nums[i]-1 == nums[i-1]):
            current_count += 1
            print(current_count)
        else:
            if(current_count > final_count):
                final_count = current_count 
                print(current_count)
            current_count == 1
            

    return(final_count)
        
test1 = [100,4,200,1,3,2]
test2 = [0,3,7,2,5,8,4,6,0,1]
longest_consecutive(test2)