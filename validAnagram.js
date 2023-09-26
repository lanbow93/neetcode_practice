// Before Video Solution
// Results: Runtime 89ms - Beat 20.63% | Memory 47.57 - Beat 36.00%
function validAnagram(s, t){
    if(s.length !== t.length){ 
        // Adding statement decreased runtime to 85ms 
       // Decreased memory 47.52
        return false;
    }
    s = s.split('').sort()
    t = t.split('').sort()
    return s === t 
}

// Second Attempt At Solution Before Video