problem statement:
You are given a file containing 100 million email addresses. Some emails may appear multiple times. Design a solution to find all duplicate emails efficiently. 

proposed solution:
my solution maintains a seen set of encountered  email addresses.
first load the file
then read each email one by one and update the seen set
    - if an email has appeared before then add it to the duplicate set
    - else add that email to seen set