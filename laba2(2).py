#метод "раздляй и властвуй"
def find_positions(s, t, n=1000):  
    if len(s) <= n:  
        positions = []
        for i in range(len(s) - len(t) + 1):
            if s[i:i + len(t)] == t:
                positions.append(i)
        return positions
    else:  
        mid = len(s) // 2  
        left_s = s[:mid]  
        right_s = s[mid:]  

        
        left_positions = find_positions(left_s, t, n)
        right_positions = [pos + mid for pos in find_positions(right_s, t, n)]  

        
        overlap_positions = []
        for i in range(max(0, mid - len(t) + 1), mid):  
            if s[i:i + len(t)] == t:
                overlap_positions.append(i)

        
        return left_positions + right_positions + overlap_positions



s = input("what s?")
t = input("what t?")
n = int(input("What n?")) 

positions = find_positions(s, t, n)  


print(*positions)