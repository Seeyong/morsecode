
# coding: utf-8

# In[1]:


# morse_code
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# In[2]:


# variables

not_str_list = ['_','@','#','$','%','^','&','*','(',')','-','+','=',
                '[',']','{','}','"',"'",';',':',"\\",'|','`','~']
spec_not_str = [' ', '.',',','!','?']
alert_message = 'Wrong Input'
morse_code_source = ["-","."," "]
help_code = ['h','help']


# In[3]:


# when_user_ask_help
def get_help_message():
    morse_code = get_morse_code_dict()
    message = "HELP - International Morse Code List\n"

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
                message += "\n"

    return message


# In[4]:


# when_user_ask_help_function(O)
def is_help_command(user_input):
    help_code = ['h','help']
    for i in range(0,len(help_code)):
        if user_input.lower() in help_code:
            return True
        else:
            return False


# In[5]:


# when_user_put_in_not_ENGLISH (O)
def is_validated_english_sentence(user_input):
    morse_code = get_morse_code_dict()
    morse_code_key = []
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        morse_code_key.append(key)
        
    str_list = []
    for i in user_input:
        str_list.append(i)
    
    # remove '.,!?' and left-right blank 
    divided_sent_list = user_input.split(' ')
    cleaned_list = []

    for i in range(0,len(divided_sent_list)):
        if divided_sent_list[i] != '':
            cleaned_list.append(divided_sent_list[i].strip(' .,?!'))
    new_english_sentence = ''.join(cleaned_list)

    for j in range(0, len(str_list)):
        if str_list[j].upper() not in morse_code_key + spec_not_str:
            return False
        else:
            if new_english_sentence.isalpha() == True:
                return True
            else:
                return False


# In[6]:


# when_user_put_in_not_MORSE_CODE(O)
def is_validated_morse_code(user_input):
    morse_code = get_morse_code_dict()
    morse_code_value = []
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        morse_code_value.append(morse_code[key])
    
    splited_morse = user_input.split(' ')
    for i in splited_morse: 
        if i not in morse_code_source + morse_code_value:
            return False
        else:
            return True


# In[7]:


# remove '.,!?' and left-right blank (O)
def get_cleaned_english_sentence(raw_english_sentence):
    divided_sent_list = raw_english_sentence.split(' ')
    cleaned_list = []

    for i in range(0,len(divided_sent_list)):
        if divided_sent_list[i] != '':
            cleaned_list.append(divided_sent_list[i].strip(' .,?!'))
    new_english_sentence = ' '.join(cleaned_list)
    return new_english_sentence


# In[8]:


# morse code to alphabet(O)
def decoding_character(morse_character):
    decoded_char = ''
    morse_code = get_morse_code_dict()
    for key, value in morse_code.items():
        if morse_character == value:
            decoded_char = key
    return decoded_char


# In[9]:


# alphabet to morse code(O)
def encoding_character(english_character):
    encoded_char = ''
    morse_code = get_morse_code_dict()
    for key, value in morse_code.items():
        if english_character == key:
            encoded_char = value
    return encoded_char


# In[10]:


# morse sentence to alphabet sentence(O)
def decoding_sentence(morse_sentence):
    morse_code = get_morse_code_dict()
    separated_morse = morse_sentence.replace('  ',' ! ').split(' ')
        
    for i in range(0,len(separated_morse)):
        for key, value in morse_code.items():
            if separated_morse[i] == value:
                separated_morse[i] = key
            elif separated_morse[i] == '!':
                separated_morse[i] = ' '
        
    decoded_sentence = ''.join(separated_morse)
    return decoded_sentence


# In[24]:


# alphabet sentence to morse sentence(O)
def encoding_sentence(english_sentence):
    divided_sent_list = english_sentence.split(' ')
    cleaned_list = []

    for i in range(0,len(divided_sent_list)):
        if divided_sent_list[i] != '':
            cleaned_list.append(divided_sent_list[i].strip('.,?!'))
    new_english_sentence = ' '.join(cleaned_list)
    
    morse_code = get_morse_code_dict()
    final_morse_list = []
    for i in new_english_sentence:
        if i == ' ':
            final_morse_list.append('')
        else:
            for key, value in morse_code.items():
                if i.upper() == key:
                    final_morse_list.append(value)
                
    final_morse = ' '.join(final_morse_list)
                
    return final_morse


# In[26]:


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    help_code = ['h', 'help']
    user_input = ''

    # when user want to exit the program
    while user_input != '0':
        # ask user_input
        user_input = input('Input your message(H - Help, 0 - Exit):')

        if user_input == '0':
            print("Good Bye")
            print("Morse Code Program Finished!!")
            break

        else:
            # when_user_ask_help_execution
            if user_input.lower() in help_code:
                print(get_help_message())

            #main encoder and decoder
            #english True
            if is_validated_english_sentence(user_input) == True:
                cleaned_eng = get_cleaned_english_sentence(user_input)

                if len(cleaned_eng) != 1:
                    print(encoding_sentence(user_input))
                else:
                    print(encoding_character(user_input))

            #morse True
            elif is_validated_morse_code(user_input) == True:
                if len(decoding_sentence(user_input)) != 1:
                    print(decoding_sentence(user_input))
                else:
                    print(decoding_character(user_input))

            #Error
            else:
                print(alert_message)

    # ==================================


if __name__ == "__main__":
    main()