import os
if __name__ =='__main__':
    os.system('pytest -q TestCase/test_docker.py --alluredir allure-results')