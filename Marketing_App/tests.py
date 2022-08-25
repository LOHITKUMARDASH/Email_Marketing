# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"super@123")
# print(type(cipher_text))
# plain_text = cipher_suite.decrypt(cipher_text)
# print(plain_text)

###########################################################################################################################

# from cryptography.fernet import Fernet
# message = "super@123"
# key = Fernet.generate_key()
# fernet = Fernet(key)
# test_string = "pbkdf2_sha256$320000$DHqiEKX3DMBAI65GylG8RV$Cy0JiXg6FoYpgZPMcTQVPCRE5W0nyUei/thk1QN/jEo="
# res = bytes(test_string, 'utf-8')
# print(res)
# # encMessage = fernet.encrypt(message.encode())
# # encMessage = fernet.encrypt(message.encode())
# # print("original string: ", message)
# # print("encrypted string: ", type(encMessage))
# decMessage = fernet.decrypt(res).decode()
# print("decrypted string: ", decMessage)
