#Write a program that:
#– prompts the user for degrees in Fahrenheit
#– converts the number into Celsius
#– prints out the number in Celsius
# to just 2 decimal places, if you dare
#C = (5 / 9) * (F - 32)
f=input("Input from Temperature (F)")
c=(5/9)*(float(f)-32)
print ("Temperature is {:.2f} degrees".format(c))