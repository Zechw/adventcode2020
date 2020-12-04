


"""

conceptually:

count the number of main capture groups -- which is a valid passport
 (
    ((
        (byr:\d*)|
        (iyr:\d*)|
        (eyr:\d*)|
    )(\\n| )?){7}
    (\\n\\n|$)     # ending in \n\n or $
 )





heuristic; count there are _any_ 7 valid fields contained (skipping--and hoping--there's no dupe-valids missing another)
                                                           i.e. 7 `byr:1980`




---


splits passports
((.*?)(\\n\\n|$))


match anything but a split
(:?(?:\w|\s|#|:|\\n(?!\\n))*?)


look-around split
(?<=^|\\n\\n)(.*?)(?=\\n\\n|$)


()



try 1
(((:?(?:\w|\s|#|:|\\n(?!\\n))*?)(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)(:?(?:\w|\s|#|:|\\n(?!\\n))*?)){7}(\\n\\n|$))
problem: the .* matches \n\n..


try2
(?:^|\\n\\n)((.*)(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)(.*)){7}(?=\\n\\n|$)







(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)
byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:
"""





"((((byr:\d*)|(iyr:\d*)|(eyr:\d*)|)(\\n| )?){7})"
