python golgotha.py test.txt && git diff --no-index expected.golgotha.test.txt golgotha.test.txt || wsl sdiff expected.golgotha.test.txt golgotha.test.txt
