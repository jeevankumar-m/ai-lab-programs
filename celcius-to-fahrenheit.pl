temperature(C, F, Status) :-
    F is (C * 9 / 5) + 32,
    ( C =< 0 ->
        Status = freezing
    ;
        Status = not_freezing
    ).
