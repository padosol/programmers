def solution(bandage, health, attacks):
    answer = health
    
    new_attacks = [[i, 0] for i in range(attacks[-1][0] + 1)]
    for attack in attacks:
        time, damage = attack
        new_attacks[time] = attack
        
        
    print(new_attacks)
    
    count = 0
    for time, attack in new_attacks:
        if attack:
            answer -= attack
            count = 0
        else:
            count += 1
            
            answer += bandage[1]

            if count == bandage[0]:
                answer += bandage[2]
                count = 0        
        
            if answer > health:
                answer = health
                
        if answer <= 0:
            return -1
        
    return answer