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
                 python3.7 -m pytest Test
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