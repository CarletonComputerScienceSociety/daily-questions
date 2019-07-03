max([H|T], X):- myMax(T, H, X).

myMax([], X, X):- !.
myMax([H|T], X, Y):-
    (H > X -> myMax(T, H, Y);
    myMax(T, X, Y)
    ).