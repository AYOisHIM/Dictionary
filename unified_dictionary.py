def load_all_dictionaries():
    """hopefully, this code will discover and add any dictionary added to the rep."""
    import os
    import importlib
    
    dictionaries = {}
    available_languages = []
    
    # List all Python files in current directory
    all_files = os.listdir('.')
    
    # Look for dictionary files (case-insensitive)
    dictionary_files = []
    for file in all_files:
        if file.endswith('.py') and 'dictionary' in file.lower():
            dictionary_files.append(file)
    
    print(f"Found {len(dictionary_files)} dictionary files: {dictionary_files}")
    
    # Try to load each dictionary
    for file in dictionary_files:
        try:
            # Extract language name from filename
            # Examples: "igbo_dictionary.py" -> "igbo"
            #           "yoruba_dict.py" -> "yoruba"  
            #           "edo_dictionary.py" -> edo"
            language_name = file.lower().replace('_dictionary.py', '').replace('_dict.py', '').replace('.py', '')
            
            # Import the module
            module_name = file.replace('.py', '')
            dictionary_module = importlib.import_module(module_name)
            
            # Store with language name as key
            dictionaries[language_name] = dictionary_module
            available_languages.append(language_name)
            
            print(f"✓ Loaded: {language_name.title()} Dictionary")
            
        except Exception as e:
            print(f"✗ Could not load {file}: {str(e)}")
    
    return dictionaries, available_languages

class AfricanDictionaryHub:
    """Central hub for all language dictionaries"""
    
    def __init__(self):
        self.dictionaries, self.available_languages = load_all_dictionaries()
        print(f"\n✅ Ready! {len(self.available_languages)} languages available: {self.available_languages}")
    
    def translate(self, word, target_language=None):
        """Translate a word to one or all languages"""
        results = {}
        
        if target_language:
            # Translate to specific language
            if target_language in self.dictionaries:
                dict_module = self.dictionaries[target_language]
                # Try common function names
                for func_name in ['translate', 'lookup', 'get_meaning', 'search']:
                    if hasattr(dict_module, func_name):
                        return getattr(dict_module, func_name)(word)
                return f"Dictionary found but no translate function in {target_language}"
            else:
                return f"Language '{target_language}' not found. Available: {self.available_languages}"
        else:
            # Translate to all available languages
            for lang, dict_module in self.dictionaries.items():
                # Try common function names
                for func_name in ['translate', 'lookup', 'get_meaning', 'search']:
                    if hasattr(dict_module, func_name):
                        results[lang] = getattr(dict_module, func_name)(word)
                        break
