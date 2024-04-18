str = "X-DSPAM-Confidence: 0.8475"

colon_pos = str.find(':')
if colon_pos >= 0:
    value = str[colon_pos + 1:]
    value = value.lstrip()
    try:
        fvalue = float(value)
        print(fvalue)
    except:
        print("value is invalid")
        raise
else:
    print("invalid string")