text = list("welcomepython")

vowels = "aeiou"

length =len(text)

print("Original text:", ''.join(text))



left = 0

right = length-1

while left<right:

    start_character = text[left]

    end_character = text[right]

    if text[left] in vowels and text[right] in vowels:

        text[right],text[left]=text[left],text[right]

        left+=1

        right-=1
    
    else:
        if start_character not in vowels:

            left += 1

        if end_character not in vowels:

            right -= 1


swaping_text= ''.join(text)

print("swaping text:", ''.join(swaping_text))



txt = "python"

if "py" in text:
    print("yes")

else:
    print("no")