% Facts
parent(ravi, arun).
parent(ravi, priya).
parent(arun, kumar).
parent(priya, meena).
% Rules
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
