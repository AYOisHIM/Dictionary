edo = edo_dict = {
    "plum": "plom",
    "garden egg": "egbon",
    "wild plum": "ukpon",
     "banana" : "ogede",
     "cocnut" : "agbon",
     "kolanut" : "ivbi",
     "orange" : "osan",
     "bitter kola" : "atigba",
     "african pear" : "ugba",
      "local pear" : "ukpe",
      "bitter fruit" : "orogbo",
      "bush apple" : "ukhi",
      "date palm fruit" : "iyan",
      "lime" : "laimu",
      "cashew" : "kashu",
      "apple" : "apulu",
      "peach" : "pesh",
      "cherry" : "cheri",
      "cranberry" : "kranberi",
      "blackberry" : "blackberi",


}
key = input("Welcome to the Edo Dictionary, what word you would like to translate to Edo?")

if key in edo:
    print(f"The meaning of {key} in edo is {edo[key]} ")

else:
    print(f"This word is not in here.")
