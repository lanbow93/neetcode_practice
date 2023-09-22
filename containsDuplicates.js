// Before Video Solution
// Results: Runtime 5766ms - Beat 6.77% | Memory 51.88 - Beat 83.22%
function containsDuplicates(nums){
    const numArray = [...nums]
    while(numArray.length > 0){
        const numberToCheck = numArray.pop()
        if(numArray.indexOf(numberToCheck) > -1){
            return true
        }
    }
    return false
}

// Solution After Video (from memory)
// Results: Runtime 138ms - Beat 28.00% | Memory 51.51 - Beat 87.17%
function containsDuplicatesRev(nums){
    nums.sort((a, b) => a-b)
    for (let i=0; i<nums.length-1; i++){
        if(nums[i] === nums[i+1]){
            return true
        }
    }
    return false
}


// Solution After Video & Research into Set
// Results: Runtime 77ms - Beat 74.51% | Memory 52.68 - Beat 72.64%
function containsDuplicatesSet(nums){
    const numSet = new Set()
    for(let i=0; i<nums.length; i++){
        if(numSet.has(nums[i])){
            return true
        }
        numSet.add(nums[i])
    }
    return false
}