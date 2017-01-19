Manual for Ubuntu (16.04):
1) first of all we need to install "virtualenv", write in terminal:
sudo apt-get install virtualenv

2) Then after instalation, to create virtual enviroment folder write in terminal:
virtualenv Jillerenv

3) Now, to activate enviroment, go to the new folder (in terminal write "cd Jillerenv") and write:
source bin/activate

4) Now your terminal is using your own virtual enviroment. Let's install pakages for our django project. Download our project from github in Jillerenv folder. To install pakages write in terminal:
pip install -r Jiller/requirements.txt 
 
5) After instalation you can check version of your Django by typing
django-admin.py --version

it should be 1.10.5
