import os

def tranverse(directory, test):
    os.chdir(directory)
    print os.getcwd()
    subdirs = os.listdir(directory)
    print subdirs
    for li in subdirs:
	li_t = directory+'/'+li
	print li_t
        if os.path.isdir(li_t):
            test_subs = test+'/'+li
	    source_subs = directory+'/'+li
	    if (os.path.exists(test_subs) == False):
            	os.mkdir(test_subs)
            tranverse(source_subs, test_subs)
        elif os.path.isfile(li):
            if li.split('.')[-1] == 'h':
                temp_file = test+'/'+li
                open(temp_file, "wb").write(open(li, "rb").read())


if __name__ == '__main__':
    tranverse('C:\Program Files (x86)\Autodesk\Scaleform\GFx SDK 4.4\Src', 'C:/test')
         
        
            
            
            

            
            
