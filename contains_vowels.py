def vowels(s):
  
    vowels = set("aeiouAEIOU")
    
    
    for char in s:
        if char not in vowels:
            return "No"
    
    return "Yes"


s = input().strip() 


print(vowels(s))
