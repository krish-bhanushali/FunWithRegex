import re
wiki = r"""(?ix)                       # case insensitive & verbose mode
    https?://                          # perhaps you should make this optional?
    (
        [a-z0-9.]{,3}                  # 
        wikipedia.org/wiki/
        (?:
            [/!@i^*$a-z0-9_-]+         # part without parenthesis
          |                            # OR
            [(] [/!@i^*$a-z0-9_-]+ [)] # part between parenthesis
        )*                             # repeat the group 0 or more times
    )"""
#source stackoverflow https://stackoverflow.com/questions/23870764/extracting-wikipedia-links-regex
test_string = 'https://en.wikipedia.org/wiki/Badminton_games'
result = re.match(wiki, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	