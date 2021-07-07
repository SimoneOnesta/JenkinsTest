pipeline{
    agent {label 'azubl00013'}
     environment {
	  PYTHON_VENV_PATH	        = "/var/lib/jenkins/penv"
	  PYTHON_ENV        	    = "dbconnect"
	  USERNAME_ARTIFCATORY      = credentials('USERNAME_MDA_ARTIFCATORY')
	  PWD_ARTIFACTORY           = credentials('PWD_MDA_ARTIFACTORY')
    }  
    stages{
        stage("Start"){
            steps{
                sh 'echo Start..'
            }
        }
        post{
            always{
                echo 'Ho terminato lo start'
            }
            failure{
                echo 'Start fallito'
            }
            success{
                echo 'Start riuscito'
            }
        }
        stage("Setup Python Env"){
            input {
                message "Posso Testare?"
                ok "Si"
            }
            steps{
                sh """#!/bin/bash
			    # Enable Python virtual environment for tests
			    source ${PYTHON_VENV_PATH}/${PYTHON_ENV}/bin/activate 
				pip config set global.index-url  https://artifacts.st.com/artifactory/api/pypi/dit-mda-python/simple
				pip config set global.extra-index-url  https://artifacts.st.com/artifactory/api/pypi/dit-mda-python-local
				pip config set install.trusted-host  artifacts.st.com
				"""
				configFileProvider([configFile(fileId: 'MDA_pypirc', targetLocation: '/var/lib/jenkins/.pypirc')]) {
				   sh"""
				   echo 'username:${USERNAME_ARTIFCATORY}' >> /var/lib/jenkins/.pypirc
				   echo 'password:${PWD_ARTIFACTORY}' >> /var/lib/jenkins/.pypirc
				   """
				}
            }
        }
        stage("Execute"){
            steps{
                script {
		  try {
		    sh """#!/bin/bash
			 # Enable Python virtual environment for tests
			 source ${PYTHON_VENV_PATH}/${PYTHON_ENV}/bin/activate 

			 # Python tests for libs
			 pytest 
			 """
		  } catch(err) {
		    sh 'echo ERROREEE'
		  }
	     }
        }
        }
    }
}