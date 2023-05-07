from translator import english_to_french, french_to_english

print("Conversion from English to French")
#Test for English to French
    #Test for Null Input
#null_input_test=english_to_french()
    #test for hello Text
test1=english_to_french("Hello!")
test2=english_to_french("Bonjour")
print(f"result of Hello Text is : {test1}, Result of Bonjour Text is : {test2} ")


#test for French to english
print("Conversion from French to English")
    #Test for Null Input
#null_input_test=french_to_english()

    #test for hello Text
test1=french_to_english("Hello!")
test2=french_to_english("Bonjour")    
print(f"result of Hello Text is : {test1}, Result of Bonjour Text is : {test2} ")