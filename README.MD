KSA Activation Script
Deployment:
1.	Create a new directory with a meaningful name on system and upload the folder KSA Activation Script in same.
Python installation:
2.	Please check the version of python i.e.  3.8.5  is installed on the Centos 7 system by the following  command mentioned below:

python3.8  -V********

(Please ensure V is in upper case and also a blank space after python3.8)


3.	If you find command not found error after running   python3.8 –V command on terminal, it means that python version 3.8.5 is not installed in your system, please install.

4.	Please verify the version of installed pip by below command :
 pip3.8 –V

(Please ensure V is in upper case and also a blank space after pip3.8)


Python Libraries Installation:

1.	Please install the required libraries by the command and also update the path of the directory as underlined and highlighted yellow. Please consider a blank space after pip-3.8, install and –r as shown below.
 pip3.8 install  -r path  of  directory/ksa_activation_script/requirements.txt  
        
Please ensure   requests ==2.24.0,  urllib3==1.25.11  are  successfully installed,  by running below command:
pip3.8 freeze

Configuration:

Please do the following modifications of the parameters in config.py file as per the requirements.


    
1.Please update validation (token)  API  URL, in config.py file, please ensure all the updated parameters should be under double quotes and also separated by comma marks. 

api_url = {
    "api_url": "https://partner.api.stc.com.sa/s-oidc/oAuth2/v1/token",
    "activated_sim_api_url": "https://partner.api.stc.com.sa/m2m/v2/sims/activated"
}

2.Please update  batch_count, imsi_from, serviceProfile in config.py.

batch_count = {
    "batch_count": 10
}

service_profile_id = {
    "serviceProfile": 9715
}

imsi_from = {
    "imsi_from": " "
}

 
RUN : 
1.RUN the script from below command, please update the path of the directory .

/path to directory/ksa_activation_script/   python3 main.py

 

LOGS:
1.Logs for Auth API , batch count, imsi_from, Activation API Response are stored in
activation_api_info.log files.






