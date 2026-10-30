max_min(A, B, Max, Min) :-
    A >= B,
    Max = A,
    Min = B.
max_min(A, B, Max, Min) :-
    A < B,
    Max = B,
    Min = A.
