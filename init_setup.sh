echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.9 version" 


conda create --prefix ./venv python=3.9.19 -y


echo [$(date)]: "activating the environment" 

source activate ./venv

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 