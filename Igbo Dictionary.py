
igbo = igbo_dict = {
    "dog": "nkita",
     "cat": "pusi",
    "goat": "ewu",
    "cow": "ehi",
     "horse": "hai",
    "sheep": "aturu",
    "pig": "ezi" ,
    "chicken": "okuko",
    "rat": "oke",
    "fish": "azu",
    "hawk": "ugo",
    "snail": "ejula",
    "rabbit": "onyeokuku",
    "bat": "anwanta",
    "turkey": "tooki",
    "tortoise": "mbe",
    "snake": "agwo",
    "elephant": "enyi",
     "monkey": "enwe",
    "grasshopper": "ukpana",
}
key = input("Welcome to the igbo dictionary, Enter an animal you would like to translate to igbo ")
if key in igbo_dict:
    print(f"The igbo translation for {key} is {igbo_dict[key]}")
else:
    print('Sorry, the animal you are trying to translate is not in the dictionary')

    hausa = hausa_dict = {
    "hello" : "sannu",
    "good afternoon": "ina wuni",
    "good evening" : "ina yamma",
    "how are you" : "lafiya lau",
    "welcome" : "barka da zuwa",
    "please" : "don allah",
    "thank you" : "na gode",
    "you are welcome" : "ba komai",
    "sorry" : "yi hakuri",
    "good luck" : "saa mai kyau",
    "take care" : "allah ya kiyaye",
    "best wishes" : "fatan alheri",
    "good night" : "barka de dare",
    "congratulations" : "taya murna",
    "see you tomorrow" : "sai gobe",
    "all the best" : "allah ya sa a dace",
    "goodbye" : "sai mun hadu ",
    "no problem" : "ba matasala",
    "well done" : "an yi kyau",
    "best of luck" : "allah ya sa a"
}

key = input("welcome to the hausa dictionary, enter any pleasantry you would like to translate to hausa")

if key in hausa_dict:
     print(f"the Hausa translation for '{key}' is '{hausa_dict[key]}'")
else:
     print("the pleasantry you are trying to translate is not registered in the dictionary")


