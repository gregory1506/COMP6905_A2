# COMP6905_A2
Assignment2
Installation instructions (Windows) :
1. Download and install python 3.6.3 https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe and set appropriate environment variables if required. http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/
2. Open powershell and git Clone Assignment repositiory $git clone https://github.com/gregory1506/COMP6905_A2.git
3. From powershell setup virtual python environment in inside the COMP69005_A2 folder $\path\to\python -m venv COMP6905_A2
4. Activate the virtual environment from powershell with $.\COMP6905_A2\Scripts\Activate.ps1
   You may need to enable scripts to be run within powershell by running "PS C:\> Set-ExecutionPolicy AllSigned" as admin.
5. Download requirements with $ pip install -r requirements.txt
6. Run the application with $ python .\app.py


Data for Testing
1. Data is located in the COMP6905_A2/data folder
2. Text files labeled based on desired action eg. "add_4trc.txt" means add 4 events to the app.
