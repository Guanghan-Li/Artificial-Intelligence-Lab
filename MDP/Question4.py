# Value Iteration for the rover MDP (γ = 0.8, ε = 1e-4)

states = ["L","M","H"]           # Low, Medium, High
actions = ["spin","no_spin"]
L, M, H = 0, 1, 2
spin, no_spin = 0, 1

# Deterministic transitions
T = {
    (L, spin):   [(1.0, M)],
    (L, no_spin):[(1.0, L)],
    (M, spin):   [(1.0, H)],
    (M, no_spin):[(1.0, L)],
    (H, spin):   [(1.0, H)],
    (H, no_spin):[(1.0, M)],
}

# Rewards R(s,a)
R = {
    (L, spin):-1.0, (L, no_spin):0.0,
    (M, spin): 2.0, (M, no_spin):3.0,
    (H, spin): 2.0, (H, no_spin):3.0,
}

gamma = 0.8
eps = 1e-4

def q_of(V, s, a):
    # Q(s,a) = sum_{s'} P(s'|s,a) [ R(s,a) + gamma * V(s') ]
    return sum(p * (R[(s,a)] + gamma * V[s2]) for p, s2 in T[(s,a)])

def value_iteration(max_iters=10000):
    V_hist = []
    V = [0.0, 0.0, 0.0]  # V0(s) = 0
    for _ in range(max_iters):
        Q = {(s,a): q_of(V, s, a) for s in range(3) for a in range(2)}
        V_new = [max(Q[(s,spin)], Q[(s,no_spin)]) for s in range(3)]
        V_hist.append(V_new.copy())
        delta = max(abs(V_new[i]-V[i]) for i in range(3))
        V = V_new
        if delta < eps:
            break
    return V, V_hist

V_star, V_hist = value_iteration()

# Values after one and two iterations
V1 = V_hist[0]
V2 = V_hist[1]

print("After 1 iteration:", {states[i]: round(V1[i], 2) for i in range(3)})
print("After 2 iterations:", {states[i]: round(V2[i], 2) for i in range(3)})
print("Converged values:", {states[i]: round(V_star[i], 2) for i in range(3)})
