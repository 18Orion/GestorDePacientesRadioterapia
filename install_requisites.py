import pip

f=open("requirements.txt","r")
for package in f:
    pip.main(["install", package, "--break-system-packages"])
f.close()