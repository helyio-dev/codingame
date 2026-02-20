import sys

def solve():
    data0 = sys.stdin.readline().split()
    data1 = sys.stdin.readline().split()
    
    name0, hp0, b0, hit0, dmg0 = data0[0], int(data0[1]), int(data0[2]), int(data0[3]), int(data0[4])
    name1, hp1, b1, hit1, dmg1 = data1[0], int(data1[1]), int(data1[2]), int(data1[3]), int(data1[4])

    memo = {}

    def get_prob(h0, h1, r0, r1, turn):
        if h1 <= 0:
            return 0.0, 1.0
        if h0 <= 0:
            return 1.0, 0.0
        if r0 == 0 and r1 == 0:
            return 0.0, 0.0
        
        state = (h0, h1, r0, r1, turn)
        if state in memo:
            return memo[state]
        
        p_a_dies, p_d_dies = 0.0, 0.0
        
        if turn == 0:
            if r0 > 0:
                p_hit = hit0 / 100.0
                pa1, pd1 = get_prob(h0, h1 - dmg0, r0 - 1, r1, 1)
                pa2, pd2 = get_prob(h0, h1, r0 - 1, r1, 1)
                p_a_dies = p_hit * pa1 + (1 - p_hit) * pa2
                p_d_dies = p_hit * pd1 + (1 - p_hit) * pd2
            else:
                p_a_dies, p_d_dies = get_prob(h0, h1, r0, r1, 1)
        else:
            if r1 > 0:
                p_hit = hit1 / 100.0
                pa1, pd1 = get_prob(h0 - dmg1, h1, r0, r1 - 1, 0)
                pa2, pd2 = get_prob(h0, h1, r0, r1 - 1, 0)
                p_a_dies = p_hit * pa1 + (1 - p_hit) * pa2
                p_d_dies = p_hit * pd1 + (1 - p_hit) * pd2
            else:
                p_a_dies, p_d_dies = get_prob(h0, h1, r0, r1, 0)
                
        memo[state] = (p_a_dies, p_d_dies)
        return p_a_dies, p_d_dies

    prob_a, prob_d = get_prob(hp0, hp1, b0, b1, 0)
    
    print(f"{round(prob_a * 100)} {round(prob_d * 100)}")

if __name__ == "__main__":
    solve()