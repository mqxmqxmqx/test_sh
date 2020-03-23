import allure


class TestContact:
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach("输入用户名", "测试输入了1")
        print("输入用户名")
        allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        allure.attach("登录", "登录的描述")
        print("点击登录")
        assert 1

