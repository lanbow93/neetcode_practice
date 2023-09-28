# Unable to Complete
# Stuck on what to do after getting count of occuring numbers
def top_k_elements(nums, k):
    element_count = {}
    for num in nums:
        element_count[num] = 1 + element_count.get(num, 0)
    print(element_count)

# Solution attempt after watching video
# Results: Runtime 99ms - Beat 57.99% | Memory 21.78 MB - Beat 31.26%  
def post_top_k_elements(nums, k):
    element_dict = {}
    counter_list = [[] for i in range(len(nums) + 1) ]
    for num in nums:
        element_dict[num] = element_dict.get(num, 0) + 1
    for key, value in element_dict.items():
        counter_list[value].append(key)
    solution = []

    for i in range(len(counter_list) -1, 0 , -1):
        if(counter_list[i]):
            for value in counter_list[i]:
                solution.append(value)
                if(len(solution) == k):
                    return solution


test_1 = [1,1,1,3,2,2]
test_1_k = 2
test_2 = [1]
test_2_k = 1

post_top_k_elements(test_1, test_1_k)