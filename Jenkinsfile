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
            when {
              branch 'production'
            }
            steps{
                sh 'echo Start..'
            }
        } 
        stage("Setup Python Env"){
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
                input message: 'Do you Approve?'
            }
        }
        stage("Test Python"){
            steps{
            echo "RESULT: ${currentBuild.result}"
                script {
		  try {
		    sh """#!/bin/bash
			 # Enable Python virtual environment for tests
			 source ${PYTHON_VENV_PATH}/${PYTHON_ENV}/bin/activate 

			 # Python tests for libs
			 pytest 
             cd terraform/platform
             ls
			 """
		  } catch(err) {
		    sh 'echo ERROREEE'
		  }
	     }
         
        }
        }
        stage("Test Terraform"){
            environment{
                TF_IN_AUTOMATION      = '1'
                CHECKPOINT_DISABLE    = '1'
                HTTPS_PROXY           = credentials('HTTP_PROXY')
                HTTP_PROXY            = credentials('HTTP_PROXY')
                NO_PROXY              = credentials('NO_PROXY')
                TF_VAR_HTTP_PROXY     = credentials('HTTP_PROXY')
                TF_VAR_HTTPS_PROXY    = credentials('HTTP_PROXY')
                TF_VAR_NO_PROXY       = credentials('NO_PROXY')
            }
            options {
                azureKeyVault(
                    credentialID: 'SON_SERVICE_APP',
                    keyVaultURL: 'https://terraformconnector.vault.azure.net/',
                    secrets: [
                        [envVariable: 'ARM_CLIENT_ID', name: 'terraform-client-id', secretType: 'Secret'],
                        [envVariable: 'ARM_CLIENT_SECRET', name: 'terraform-secret', secretType: 'Secret'],
                        [envVariable: 'ARM_SUBSCRIPTION_ID', name: 'terraforr-subscriptio-id', secretType: 'Secret'],
                        [envVariable: 'ARM_TENANT_ID', name: 'terraform-tenant-id', secretType: 'Secret']
                    ]
                )

            }
            steps{
                echo "deploy infra"
                sh '''
                    cd Terraform
                    terraform init
                    echo $ARM_CLIENT_ID
                    echo $ARM_CLIENT_SECRET
                    echo $ARM_SUBSCRIPTION_ID
                    echo $ARM_TENANT_ID
                    terraform plan
                 '''
            }
        }
    }
    post{
            always{
                echo 'Ho terminato la pipeline'
            }
            failure{
                echo 'Pipeline fallita'
            }
            success{
                echo 'Pipeline riuscita'
            }
        }
}