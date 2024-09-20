# Pyrametrize
### Easy, flexible configuration inheritance & parametrization for Python

`pyrametrize` provides a simple, robust and extensible system for managing configuration inheritance and parameterization in Python projects. It allows developers to flexibly merge configurations and control how various nodes (pieces of data) interact, based on customizable rules.

# Features
Extensible merging logic: Define how to merge specific nodes, skip them, or handle them in other ways.
Flexible configuration: Easily supply configuration for which nodes to merge and how to merge them.
Recursive structure: The merging process is recursive, making it adaptable to a variety of complex data structures.

# Algorithm Overview
The core algorithm traverses a hierarchical tree of nodes. For each node encountered, the algorithm determines:

Merge Decision: Should the node be merged or skipped?
Merge Strategy: If merging is required, what merging strategy should be applied?
This merge process is highly configurable, meaning that you can define both which nodes to merge and the rules for how they should be merged or skipped.
