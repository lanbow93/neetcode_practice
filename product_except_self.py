# Unable to Complete
# Stuck on how not to nest for loops
def product_except_self(nums):
    array_of_values = []

    for count, num in enumerate(nums, 1):
        if(count == len(array_of_values)):
            print(num)
        #First need a way to make lists containig values without index value
        #Then need to multiple those numbers together
        # Then need to add to list to return
 
# Solution attempt after watching video
# Results: Runtime 181ms - Beat 94.64% | Memory 23.93 MB - Beat 68.10%  
def post_product_except_self(nums):
    final_array = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        final_array[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(len(nums) -1, -1, -1):
        final_array[i] *= suffix
        suffix *= nums[i]
    
    return(final_array)

test_one = [1,2,3,4]
test_two = [-1,1,0,-3,3]

post_product_except_self(test_two)
