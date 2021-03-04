def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    # base case to break recursion
    if num == 0:
        return [""]

    elif 1 < num <= 9:
        return list(get_characters(num))

    else:
        pass


keypad(0)  # ['']
keypad(8)  # ["t", "u", "v"]
keypad(23)  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# def test_keypad(input, expected_output):
#     if sorted(keypad(input)) == expected_output:
#         print("Yay. We got it right.")
#     else:
#         print("Oops! That was incorrect.")


# Base case: list with empty string
# input = 0
# expected_output = [""]
# test_keypad(input, expected_output)


# # Example case
# input = 23
# expected_output = sorted(
#     ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# test_keypad(input, expected_output)


# # Example case
# input = 32
# expected_output = sorted(
#     ["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
# test_keypad(input, expected_output)


# # Example case
# input = 8
# expected_output = sorted(["t", "u", "v"])
# test_keypad(input, expected_output)


# input = 354
# expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh",
#                           "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
# test_keypad(input, expected_output)
