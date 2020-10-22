# 3D Environment Navigation

This repository contains experiments run on DeepMind Lab and custom 2D toy grid environments. Here are a list of trials run using different reward functions, models, and more:

**Reward**
1. Distance-based 
2. Goal count-based

**Actions**
1. Free movement in 8 cardinal directions
2. Accessibility-related
    - pick up
    - carry
    - drop

**Memory Buffers**
- [ ] LSTM
- [ ] Neural Map (*Original implementation missing*)
- [ ] Cognitive Mapping and Planning (CMP)
- [ ] Active Neural SLAM (Occupancy Anticipation)

**RL Approaches**
- [ ] Actor Critic
- [ ] PPO
- [ ] TRPO
- [ ] Imitation Learning
    - Behavioural Cloning
    - Teacher Enforcing (for RNN/LSTM)
    - Learning from Demonstrations
