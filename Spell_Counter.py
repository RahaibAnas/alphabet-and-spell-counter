string= input("Write Your Text here:  ")
def spell_counter(a):
    print("===== Spell Counter =====")
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    for item in range(0,len(alphabet)):
        count =0
        b=a.lower()
        for item1 in range(0,len(b)):
            if alphabet[item] == b[item1]:
                count +=1
        c=print(f"{item+1}. {alphabet[item].upper()} comes {count} times. \n ")
    d =print(f"This Text contains {len(b.split(" "))} words")
    return c ,  d  

spell_counter(string)