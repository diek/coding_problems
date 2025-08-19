# Enter your code here. Read input from STDIN. Print output to STDOUT
total_english = int(input())
english_students_enrolled = list(map(int, input().split()))
total_french = int(input())
french_students_enrolled = list(map(int, input().split()))

s = set(english_students_enrolled)
print(len(s.symmetric_difference(french_students_enrolled)))

H = set("Hacker")
R = set("Rank")
H.update(R)
print(H)
# => set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

# Update the set by keeping only the elements found in it and an iterable/another set.
R = set("Rank")
H.intersection_update(R)
print(H)
# => set(['a', 'k'])

# Update the set by removing elements found in an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)
# set(['c', 'e', 'H', 'r'])

# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.

H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print(H)
# set(['c', 'e', 'H', 'n', 'r', 'R'])


m = int(input())
A = set(map(int, input().split(" ")))
n = int(input())

for i in range(n):
    cmd, args = input().split()
    B = set(map(int, input().split()))
    eval('A.'+ cmd +'(B)')

print(sum(A))
