
# Introduction

* Real world learning
    * Scarcity of data, expensive testing => fails to generalize.
* Learning in simulations
    * Non-robustness to modelling errors => unsuccessful transfer of
      learnt policy.

In a past work - high friction helped model adversarial forces at
contact points helping learning. Can we use this further?

## Proposition

 * RARL: Robust Adversarial Reinforcement Learning
    * Jointly train protagonist, adversary.

### Evaluations

 * OpenAI gym environments.
    * InvertedPendulum
    * HalfCheetah
    * Swimmer
    * Hopper
    * Walker2D

#### Objective

Proposed approach is:

* Robust to model initializations
* Robust to modelling errors and uncertainties.

## Premises

### Overview

* train on carpet - test on ice: *must generalize*.
* Parameters: mass, friction. 
* Methods:
    * Learn ensemble of policies on variations.
* Problems:
    * Possible to sample trajectories under possible disturbances?
    * Unconstrained scenarios - disturbances >> actions => very sparse.

* Proposed solution.
    * Adversarial agents model disturbances.
    * Adversaries incorporate domain knowledge.

## Past work
### Standard RL on MDPs

* Batch policy algorithms 
    * REINFORCE, NPG, TRPO
    * Learn stochastic policy maximizes cumulative discouted reward.

### Two player zero-sum discounted games.
    * [expand]

## RARL


### Results

