import subprocess

def open_allure_report():
    subprocess.call("allure serve allure_report", shell=True)

if __name__ == "__main__":
    open_allure_report()