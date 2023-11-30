def reverse(input):
    if not input:
        return ""
    return reverse(input[1:]) + input[0]


print(reverse("ab"))