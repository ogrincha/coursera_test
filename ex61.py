text = "X-DSPAM-Confidence:    0.8475";
pos_0 = text.find('0')
result = text[pos_0:100]
fresult = float(result)
print(fresult)
