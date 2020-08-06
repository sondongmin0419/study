scores = [0]*5
 
for i in range(5):
    scores[i] = int(input())
    
    if scores[i] < 40:
        scores[i] = 40
        
avg  = sum(scores)/5       
print(int(avg))