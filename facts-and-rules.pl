% Student Facts
student(arun).
student(bala).
student(charan).
student(divya).
student(esha).
% Subject Facts
subject(arun, prolog).
subject(arun, dbms).
subject(bala, prolog).
subject(bala, dbms).
subject(charan, prolog).
subject(charan, dbms).
subject(divya, prolog).
subject(divya, dbms).
subject(esha, prolog).
subject(esha, dbms).
% Marks Facts
marks(arun, prolog, 85).
marks(arun, dbms, 78).
marks(bala, prolog, 65).
marks(bala, dbms, 72).
marks(charan, prolog, 45).
marks(charan, dbms, 38).
marks(divya, prolog, 92).
marks(divya, dbms, 88).
marks(esha, prolog, 55).
marks(esha, dbms, 60).
% Rule to check pass
pass(Student, Subject) :-
    marks(Student, Subject, Mark),
    Mark >= 40.
% Rule to check fail
fail(Student, Subject) :-
    marks(Student, Subject, Mark),
    Mark < 40.
% Rule to identify high scorer
high_scorer(Student, Subject) :-
    marks(Student, Subject, Mark),
    Mark >= 80.
% Rule to identify excellent student
excellent(Student) :-
    marks(Student, prolog, Mark1),
    marks(Student, dbms, Mark2),
    Mark1 >= 80,
    Mark2 >= 80.
% Rule to find student and marks
student_marks(Student, Subject, Mark) :-
    student(Student),
    subject(Student, Subject),
    marks(Student, Subject, Mark).
