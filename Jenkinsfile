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
                 PyTest Test
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