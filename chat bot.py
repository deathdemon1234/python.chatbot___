import numpy as np
import pandas as pd
s=np.array([])
print("i am the chat bot")
print("ask any question in which you have a doubt")
var1=input("enter the subject you have doubt:")
if(var1=='maths'):
  print("which topic you have doubt? type down:-")
  var2=input("enter your topic:""(for example addition,sub....etc.)")
  if(var2=="addition"):
    var4=int(input("enter you first number:"))
    var5=int(input("enter you second number:"))
    print("your sum is:",var4+var5)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="subtraction"):
    var6=int(input("enter you first number:"))
    var7=int(input("enter you second number:"))
    print("your diff is:",var6-var7)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="multiplication"):
    var8=int(input("enter you first number:"))
    var9=int(input("enter you second number:"))
    print("your prod is:",var8*var9)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="division"):
    var10=int(input("enter you first number:"))
    var11=int(input("enter you second number:"))
    print("your quotient is:",var10/var11)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="square root"):
    var12=int(input("enter you number:"))
    s.append(var12)
    print("your root value is:",np.sqrt(s))
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="power"):
    var13=int(input("enter you first number:"))
    var14=int(input("enter you second number:"))
    print("your power value is:",var13**var14)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="factorise"):
    print("we can factorise sums in many ways and identities We can start by factoring out the greatest common factor (GCF) of the terms")
    print("identities:-(a + b)2 = a2 + b2 + 2ab(a – b)2 = a2 + b2 – 2ab ,(a + b)3 = a3 + b3 + 3ab(a + b) = a3 + b3 + 3a2b + 3ab2 ,(a – b)3 = a3 – b3 – 3ab(a – b) = a3 – b3 – 3a2b + 3ab2 ,(a + b + c)2 = a2 + b2 + c2 + 2ab + 2bc + 2ca ,a3 – b3 = (a – b)(a2 + ab + b2), a3 + b3 = (a + b)(a2 – ab + b2) ,a3 + b3 + c3 – 3abc = (a + b + c)(a2 + b2 + c2 – ab – bc – ca)")
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="hyportenuse"):
    print("Hypotenuse means, the longest side of a right-angled triangle compared to the length of the base and perpendicular. The hypotenuse side is opposite to the right angle, which is the biggest angle of all the three angles in a right triangle.")
    var15=int(input("enter you first number:"))
    var16=int(input("enter you second number:"))
    print("hyportenuse =",var15**var15+var16**var16)
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var2=="trignomentary"):
    print("Trigonometry (from Ancient Greek τρίγωνον (trígōnon) 'triangle', and μέτρον (métron) 'measure') is a branch of mathematics concerned with relationships between angles and side lengths of triangles.")
  else:
    print("this ai is not fully completed,you will get this topic in next version.")
elif(var1=='science'):
  var17=input("enter your question:")
  if(var17=="what is photosynthesis"):
    print("ans:-the process by which green plants and some other organisms use sunlight to synthesize nutrients from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a by-product.during photosynthesis plants absorb CO₂")
    print("i hope you are satisfied, please be free to ask any other doubts")
  elif(var17=="what is an atom"):
    print("An atom is a particle of matter that uniquely defines a chemical element. An atom consists of a central nucleus that is surrounded by one or more negatively charged electrons. The nucleus is positively charged and contains one or more relatively heavy particles known as protons and neutrons.")
  elif(var17=="what is the formula for force"):
    print("force=M*A")
  elif(var17=="what is the formula for pressure"):
    print("presure= F/A")
  elif(var17=="si units in physics"):
    print("Length - meter (m),Time - second (s),Amount of substance - mole (mol),Electric current - ampere (A),Temperature - kelvin (K),Luminous intensity - candela (cd),Mass - kilogram (kg),newton- N,passcal-P,ms2-meter per second aqiare .......etc",)
  elif(var17=="name me the first twenty elements in periodic table"):
    print("H – Hydrogen,He – Helium.,Li – Lithium,Be – Beryllium,B – Boron,C – Carbon,N – Nitrogen,O – Oxygen,F – Fluorine,Ne – Neon,Na – Sodium,Mg – Magnesium,Al – Aluminium,Si – Silicon,P – Phosphorus,S – Sulphur,Cl – Chlorine,Ar – Argon,K – Potassium,Ca – Calcium.")
  elif(var17=="who invented cell"):
    print("Cell was discovered by a British scientist, Robert Hooke in 1665. He observed cells in a cork slice under his self-designed microscope and noticed honeycomb like compartments. He coined them as cells.")


