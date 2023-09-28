# ECEGR4750

## Labs
### Getting started
0. Ensure that Python version > 3.8.0 is installed.
1. Clone this repository into a local folder in your computer
2. Navigate to that folder
   ```
    a. $ cd <Path to Folder>
   ```
4. Setup a virtual environment, called '.venv'
   ```
    a. In your Powershell or Windows CMD: $ python -m venv .venv
    b. In your Linux terminal: $ python3 -m venv .venv
   ```
6. Activate the virtual environment
   ```
    a. In Powershell or Windows CMD: $ .venv\Scripts\activate
    b. In Linux: $ source .venv/bin/activate
   ```
8. Install all necessary librarires
   ```
    a. $ pip install -r ./labs/requirements.txt
    b. Upgrade pip if necessary: $ python -m pip install --upgrade pip
   ```
10. Open up Jupyter Notebook
    ```
    a. $ jupyter notebook
    ```
12. Or, you can choose to open up the notebook using VSCode
    a. Ensure that the notebook in VSCode is using the venv kernel

### Git comamnds
1. Every single time you touch your code, always pull from the remote (the one in the cloud / online) repository
   ```
   $ git checkout master # ensure that you are at the master branch
   $ git pull
   ```
2. Create a new branch for that particular week's lab session
   ```
   $ git checkout -b <yourname>/weekX
   Or, if you have already created that branch, just swith to that branch: $ git checkout <yourname>/weekX
   ```
3. Ensure that your branch is updated with the latest master
   ```
   $ git merge master
   ```
5. At the end of each lesson, "commit" your work
   ```
   $ git status # check what are the files changed. if you use VSCode, install the Git extension and the UI provided is amazing for this
   $ git add . # either add the files one by one, or add all changes by using the . notation
   $ git commit -m <Commit description here>
