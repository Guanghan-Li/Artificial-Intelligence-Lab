# Value Iteration for the given 5-state MDP

states = ["S1","S2","S3","S4","S5"]
actions = ["a1","a2"]

# State-based rewards R(s)
R = {"S1":0.0,"S2":1.0,"S3":0.0,"S4":0.0,"S5":1.0}
gamma = 0.9
eps = 1e-4

# Transition model: P(s' | s, a)
T = {
    ("S1","a1"):[(0.5,"S2"),(0.5,"S3")],
    ("S2","a1"):[(0.5,"S4"),(0.5,"S5")],
    ("S3","a1"):[(0.9,"S4"),(0.1,"S5")],
    ("S4","a1"):[(1.0,"S4")],
    ("S5","a1"):[(1.0,"S5")],

    ("S1","a2"):[(0.9,"S2"),(0.1,"S3")],
    ("S2","a2"):[(0.9,"S4"),(0.1,"S5")],
    ("S3","a2"):[(0.5,"S4"),(0.5,"S5")],
    ("S4","a2"):[(1.0,"S4")],
    ("S5","a2"):[(1.0,"S5")],
}

def q_of(V, s, a):
    # Q(s,a) = sum_{s'} P(s'|s,a) [R(s) + gamma * V(s')]
    return sum(p * (R[s] + gamma * V[s2]) for p, s2 in T[(s, a)])

def value_iteration(max_iters=1000):
    V = {s: 0.0 for s in states}
    for _ in range(max_iters):
        # Compute Q for all (s,a) from current V
        Q = {(s,a): q_of(V, s, a) for s in states for a in actions}
        # Greedy backup
        V_new = {s: max(Q[(s,"a1")], Q[(s,"a2")]) for s in states}
        # Convergence check (max-norm)
        delta = max(abs(V_new[s] - V[s]) for s in states)
        V = V_new
        if delta < eps:
            break
    # Greedy policy from the last Q
    pi = {s: max(actions, key=lambda a: Q[(s, a)]) for s in states}
    return V, pi

if __name__ == "__main__":
    V_star, pi_star = value_iteration()
    # Print with two decimals (adjust as you like)
    print("Optimal state values:")
    for s in states:
        print(f"  {s}: {V_star[s]:.2f}")
    print("\nGreedy policy:")
    for s in states:
        print(f"  {s}: {pi_star[s]}")
