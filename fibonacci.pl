fibonacci(N, Series) :-
    fib(N, 0, 1, Series).
fib(0, _, _, []).
fib(N, A, B, [A|Rest]) :-
    N > 0,
    N1 is N - 1,
    C is A + B,
    fib(N1, B, C, Rest).
