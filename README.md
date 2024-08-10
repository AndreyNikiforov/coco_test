# Exploring coconut lang

Main application -- building typed finite state machine for icloudpd:
- exhaustiveness check through types
- functional composition, functors/applicatives/monads for managing complexity
- pure vs side-effects (== Event/Command separation??? OR IO monad as "cmd")
- ADT for state and events
- State monad for passing state around

Bonus:
- parsing combinator for json parsing?
- 

# Setting up

```shell
pip install -e .
```

# Running

```shell
coconut-run src/main.coco
```

# Plan

1. Get FSM in Python (depth first)
    - should be easy to understand pain points and boilerplate code
    - should be easy to confirm that fsm is right choice for response processing in `icloudpd`
1. get coconut
    - ADT for responses
    - matching