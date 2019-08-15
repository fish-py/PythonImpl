"""
如何提取一个字符串中的英文字母？
"""


def get_alpha(string):
    alpha_string = ""
    for char in string:
        if char.isalpha():
            alpha_string += char
    return alpha_string

s = "刺激1995 The Shawshank Redemption"

if __name__ == "__main__":
    print(get_alpha(s))

