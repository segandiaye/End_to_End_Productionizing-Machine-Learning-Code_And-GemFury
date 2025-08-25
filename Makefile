create_env:
	pyenv virtualenv ml_build_package_env
	pyenv local ml_build_package_env

install_deps:
	pip install -r requirements.in