// Before Video Solution
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