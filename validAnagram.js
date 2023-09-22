// Before Video Solution
// Results: Runtime 89ms - Beat 20.63% | Memory 47.57 - Beat 36.00%
function validAnagram(s, t){
    s = s.split('').sort().join('')
    t = t.split('').sort().join('')
    return s === t 
}