import allure
import pytest


@allure.feature("一级标签")
class TestAllure:
    @allure.title("用例1")
    @allure.description("用例的详细说明")
    @allure.story("二级标签")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        print("test1")

    @allure.title("用例2")
    @allure.story("用例的详细说明")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test2")


if __name__ == '__main__':
    pytest.main("allure_demo.py",)