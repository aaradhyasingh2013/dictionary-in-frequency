text_dict={"color":"orange","name":"orange","fuit":"orange","shake":"orange"}
a= "orange"
res= 0
for i in text_dict:
    if text_dict[i]== a:
        res= res+1
print("Frequency of a is: " + str(res))