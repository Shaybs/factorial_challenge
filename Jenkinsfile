pipeline{
	agent any
	stages{
		stage("Update git repo") {
			steps{
				sh '''ssh msh516@instance-python << EOF
				cd factorial_challenge/
				git pull'''
			}
		}
		stage("Test") {
			steps{
				sh '''ssh msh516@instance-python << EOF
				cd factorial_challenge/
				git checkout development
				pytest'''
			}
		}
	}
}