% Family Tree Facts
% Parent relationships
parent(john, mary).
parent(john, david).
parent(john, linda).
parent(mary, susan).
parent(mary, robert).
parent(david, james).
parent(david, anna).
parent(linda, peter).
parent(linda, sophia).
% Gender facts
male(john).
male(david).
male(robert).
male(james).
male(peter).
female(mary).
female(linda).
female(susan).
female(anna).
female(sophia).
% Rule for child
child(X, Y) :-
    parent(Y, X).
% Rule for grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
% Rule for grandchild
grandchild(X, Y) :-
    grandparent(Y, X).
% Rule for sibling
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
% Rule for father
father(X, Y) :-
    parent(X, Y),
    male(X).
% Rule for mother
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Rule for brother
brother(X, Y) :-
    sibling(X, Y),
    male(X).
% Rule for sister
sister(X, Y) :-
    sibling(X, Y),
    female(X).
