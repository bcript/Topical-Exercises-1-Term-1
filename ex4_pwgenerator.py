import random
pw = []
def main():
  global pw_length
  while True:
    try:
      pw_length = int(input("How long d you want this password to be?: "))
      generate_pwd(pw_length)
    except ValueError:
       print("Please enter a valid number.")

def generate_pwd(num_chars):
  for i in range(pw_length):
    random_char = chr(random.randint(32, 126))
    print(random_char)
    pw.append(random_char)
    
  print(''.join(map(str, pw)))
  
if __name__ == "__main__":
  main()
