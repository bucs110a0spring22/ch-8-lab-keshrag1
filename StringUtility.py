class StringUtility(object):
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return self.string

  def vowels(self):
    """
    The function counts the number of vowels in a word
    args: self(object) the function uses its class of StringUtility as its argument
    returns: count(str) this is the number of vowels in the word, many(str)occurs if there are 5 or more vowels in a word or phrase
    """
    count = 0
    for i in self.string:
      if i in "aeiouAEIOU":
        count += 1
    if count < 5:
      return str(count)
    elif count >= 5:
      return str("many")

  def bothEnds(self):
    """
    this function checks and retruns the first 2 and last 2 characters of a word or phrase
    args: self(object) the function uses its class of StringUtility as its argument
    returns: self.string[:2]+self.string[-2:](str) this is the first and last two characters of a word or phrase, ""(str) this is an empty string
    """
    if len(self.string)>=2:
      return self.string[:2]+self.string[-2:]
    else:
      return ""

  def fixStart(self):
    """
    This function replaces the any character that is the same value as the first character with a *
    args: self(object) the function uses its class of StringUtility as its argument
    returns: self.string[0]+self.string[1:].replace(self.string[0], "*")(str) replaces character with *, ""(str) an empty string
    """
    if len(self.string)>=2:
      return self.string[0]+self.string[1:].replace(self.string[0], "*")
    else:
      return ""

  def asciiSum(self):
    """
    this function adds up all the ascii values in a string
    args: self(object) the function uses its class of StringUtility as its argument
    returns:sum(int) the total ascii value of the word or phrase
    """
    sum = 0
    for i in self.string:
      sum += ord(i)
    return sum

  def cipher(self):
    """
    The function shifts letters by the amount of letters in the word
    args: self(object) the function uses its class of StringUtility as its argument
    returns: encoded_string(str) the new phrase with new letters
    """
    if not self.string:
      return ""
    encoded_string = ""
    size = len(self.string)
    for i in self.string:
      ascii_val= None
      if not self.condition_in_alphabet(i):
        encoded_string += i
      elif i.lower() == i:
        ascii_val = ((ord(i) - ord('a')) + size) %26
        encoded_string += chr(ascii_val+ord("a"))
      elif i.upper() == i:
        ascii_val = ((ord(i) - ord('A')) + size) %26
        encoded_string += chr(ascii_val+ord("A"))
    return encoded_string

  def condition_in_alphabet(self, i):
    """
    the function loops z to a and Z to A for the cipher function
    args: self(object) the function uses its class of StringUtility as its argument, i(int) this is the number of letters in the word or phrase
    returns: none
    """
    return (ord(i) >= 65 and ord(i) <=90) or (ord(i) >=97 and ord(i) <= 122)