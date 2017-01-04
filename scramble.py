import string

coded_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
split_words = coded_string.split(" ")
intable = string.ascii_lowercase
outtable = string.ascii_lowercase[2:]+string.ascii_lowercase[:2]

decoded_string = coded_string.translate(str.maketrans(intable, outtable))
coded_url = "http://www.pythonchallenge.com/pc/def/map.html"
decoded_url = coded_url.translate(str.maketrans(intable, outtable))

print(decoded_string, " ", end="")