from Fuzzer import SQLiFuzzer

payload = input("Enter a payload: ")

fuzzer = SQLiFuzzer()

new_payload = fuzzer.mutate()

print(new_payload)