#14/4/2021
#By Jedsada Luengaramsuk 

#! python3 
#mapIT.py Launches a map in the browser using an address from the commanline or clipboard 
#Example: mapit 870 Valencia St, San Francisco, CA 94110
#This will be the final program




import webbrowser, sys, pyperclip

#sys.argv = stores a list of commandline argument 
# len(sys.argv) > 1 show that if interger greater than 1 = command line argument has be provided 
# join because command line argument is a list not string.  

if len(sys.argv) > 1: 
    #Get address from command line 
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard 
    address = pyperclip.paste() 


#open the browser with address above
webbrowser.open('https://www.google.com/maps/place/' + address)





