def fake_bin(x):
    result = ""  # Start with an empty string
    for digit in x:
        if int(digit) < 5:  # Check if the digit is below 5
            result += "0"  # Append '0' if it's less than 5
        else:
            result += "1"  # Append '1' if it's 5 or greater
    return result
