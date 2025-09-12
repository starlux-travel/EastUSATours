from django.test import TestCase
from django.urls import reverse


class AccountsTests(TestCase):
    def test_login_page(self):
        """測試登入頁面是否存在"""
        url = f"/zh-tw{reverse('login')}"  # Django 自帶 login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        """測試登出頁面是否存在"""
        url = f"/zh-tw{reverse('logout')}"  # Django 自帶 logout
        response = self.client.get(url)
        # logout 頁面有時候會 redirect，所以允許 200 或 302
        self.assertIn(response.status_code, [200, 302])

    def test_dashboard_page(self):
        """測試會員儀表板頁面"""
        url = f"/zh-tw{reverse('accounts:dashboard')}"
        response = self.client.get(url)
        # 未登入可能會 redirect，所以允許 200 或 302
        self.assertIn(response.status_code, [200, 302])

    def test_profile_page(self):
        """測試會員資料頁面"""
        url = f"/zh-tw{reverse('accounts:profile')}"
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302])

    def test_orders_page(self):
        """測試會員訂單頁面"""
        url = f"/zh-tw{reverse('accounts:orders')}"
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302])
