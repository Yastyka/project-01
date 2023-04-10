Пункт А.

foo("Hi! Hello!") -> "Hi Hello"
foo("") -> ""
foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(string):
    mark = {ord('!') : None}
    return string.translate(mark)

words1 = "Hi! Hello!"
words2 = ""
words3 = "Oh, no!!!"   
print(remove_exclamation_marks(words1))
print(remove_exclamation_marks(words2))
print(remove_exclamation_marks(words3))

Пункт В

Удалите восклицательный знак из конца строки. 
remove("Hi!") == "Hi"
remove("Hi!!!") == "Hi!!"
remove("!Hi") == "!Hi"


def remove_last_em(s):
    return s[:-1] if s and s[-1] == '!' else s

print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))


# вот про пункт С, если интересно
# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))
