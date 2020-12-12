s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k : (index + 1) * k]
    print(t)
    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
              print("u:{}".format(u))
              print("c:{}".format(c))
              u += c

    # Print final converted string
    print(u)
