def solution(players, m, k):
    answer = 0
    servers = [0] * 24
    
    for i in range(24):
        servers_required = players[i] // m
        
        if servers[i] < servers_required:
            servers_added = servers_required - servers[i]
            answer += servers_added
            
            for j in range(i, min(i + k, 24)):
                servers[j] += servers_added
    return answer