Uname = input("Input your name to see its reverse str : ").strip()
N_len = len(Uname)
Reverse_Str =''

for char in range(N_len-1,-1,-1):
    Reverse_Str +=Uname[char]
print(f"Reversed Str : {Reverse_Str}")
    
