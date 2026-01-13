# Q-Learning

## Q-Learning

### Term definition table

| Term | Definition |
| --- | --- |
| Q-Learning | A **model-free reinforcement learning** algorithm that learns the optimal action to take in each state. |
| Agent | The learner that takes actions. |
| Environment | The world the agent interacts with. |
| State (s) | A description of the current situation. |
| Action (a) | A possible move the agent can take. |
| Reward (r) | Feedback from the environment. |
| Q-value | Expected future reward for taking action aaa in state sss. |
| Q-Table | Table storing Q-values for all (state, action) pairs. |
| Learning Rate (α) | Controls how much new information overrides old. |
| Discount Factor (γ) | How much future rewards are valued. |
| Policy | Rule for choosing actions. |

---

### Definition about the algorithm

**Q-Learning** teaches an agent how to act optimally by learning the **quality (Q-value)** of each action in each state.

The agent explores the environment and updates Q-values based on the rewards it receives.

---

### Advantages / disadvantages

**Advantages**

- No model of the environment required.
- Guaranteed to find optimal policy with enough exploration.
- Works well for discrete state/action spaces.

**Disadvantages**

- Slow for large state spaces.
- Requires storing a large Q-table.
- Needs careful tuning of α and γ.

---

### Math equation

### Q-value update rule

$Q(s,a) \leftarrow Q(s,a) + \alpha \bigl[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\bigr]$

Where:

- s = current state
- a = action taken
- r = reward
- s' = next state

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
def q_learning(env, alpha, gamma, episodes):
    Q = initialize_Q(env.states, env.actions)

for _inrange(episodes):
        s = env.reset()

whilenot env.done():
            a = choose_action(Q, s)
            s2, r = env.step(a)

            Q[s][a] += alpha * (r + gamma *max(Q[s2]) - Q[s][a])
            s = s2

return Q
```

---

### Step-by-step through the algorithm

1. Initialize Q-table to zero.
2. Start in an initial state.
3. Choose an action (explore or exploit).
4. Perform the action.
5. Receive reward and next state.
6. Update Q-value using the update rule.
7. Move to the new state.
8. Repeat until episode ends.
9. Repeat for many episodes.
10. The learned Q-table defines the optimal policy.