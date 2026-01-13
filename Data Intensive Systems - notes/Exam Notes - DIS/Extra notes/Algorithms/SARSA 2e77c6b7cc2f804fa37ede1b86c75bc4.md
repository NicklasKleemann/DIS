# SARSA

## SARSA (State–Action–Reward–State–Action)

### Term definition table

| Term | Definition |
| --- | --- |
| SARSA | An **on-policy reinforcement learning** algorithm for learning action values. |
| State (s) | Current situation of the agent. |
| Action (a) | Move taken by the agent. |
| Reward (r) | Feedback from the environment. |
| Next State (s′) | State after taking an action. |
| Next Action (a′) | Action chosen in the next state. |
| Q-value | Expected future reward for a state–action pair. |
| Policy | Strategy for selecting actions. |
| Learning Rate (α) | How fast learning happens. |
| Discount Factor (γ) | Importance of future rewards. |

---

### Definition about the algorithm

**SARSA** learns the value of actions based on the **current policy** being followed.

Unlike Q-Learning, which uses the best possible next action, SARSA updates its values using the **actual action chosen**, making it more conservative and stable.

---

### Advantages / disadvantages

**Advantages**

- More stable than Q-Learning.
- Safer in risky environments.
- Learns behavior consistent with the policy.

**Disadvantages**

- Converges slower than Q-Learning.
- May learn suboptimal policies.
- Still struggles with large state spaces.

---

### Math equation

### SARSA update rule

$Q(s,a) \leftarrow Q(s,a) + \alpha \bigl[r + \gamma Q(s',a') - Q(s,a)\bigr]$

---

### Runtime

Let:

- S = number of states
- A = number of actions

**Training**

- Best & Worst: $O(S \cdot A)$ per episode

**Prediction**

- Best & Worst: $O(A)$

---

### Python-like pseudo code

```python
def sarsa(env, alpha, gamma, episodes):
    Q = initialize_Q(env.states, env.actions)

for _inrange(episodes):
        s = env.reset()
        a = choose_action(Q, s)

whilenot env.done():
            s2, r = env.step(a)
            a2 = choose_action(Q, s2)

            Q[s][a] += alpha * (r + gamma * Q[s2][a2] - Q[s][a])
            s, a = s2, a2

return Q
```

---

### Step-by-step through the algorithm

1. Initialize Q-table.
2. Choose initial state and action.
3. Take action.
4. Observe reward and next state.
5. Choose next action using policy.
6. Update Q-value using SARSA rule.
7. Move to next state and action.
8. Repeat until episode ends.
9. Repeat for many episodes.
10. Learned Q-table represents policy.