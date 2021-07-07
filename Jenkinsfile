pipeline{
    agent any
    stages{
        stage("Start"){
            steps{
                sh 'echo Start..'
            }
        }
        stage("Execute"){
            steps{
                sh '''echo Execute....
                 pwd
                 cd /var/lib/jenkins/penv
                 ls
                 '''
            }
        }
        stage("Finish"){
            steps{
                sh 'echo Finish...'
            }
        }
    }
}