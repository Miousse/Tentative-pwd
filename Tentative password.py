def password():
   trouve = 5
   print('Il faut un mot de passe')
   
   for k in range(trouve):
       psd =input(f"Tu es au {k + 1} tentative, Le mot de passe ?")
       if psd != "NON":
           print("FAUX")
       else:
           print("Iphone 16 PRO MAX ULTRA ANGLE 5G ouvert")
           
           break
   else:
       print("BIPPP IPHONE BLOQUE")

print(password())
