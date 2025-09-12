# tours/tests.py
from django.test import TestCase
from django.urls import reverse


class ToursTests(TestCase):

    def test_home_page(self):
        """首頁 /zh-tw/ 是否能正常開啟"""
        response = self.client.get("/zh-tw/")  # ✅ i18n_patterns 預設首頁
        self.assertEqual(response.status_code, 200)

    def test_tours_api_list(self):
        """Tours API 是否能回應 JSON"""
        url = reverse("tour-list")  # ✅ DRF router 自動生成的名稱
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 403])  # 未登入可能 403
        self.assertIn("application/json", response["Content-Type"])

    def test_language_switch(self):
        """測試多語言網址 /zh-tw /zh-cn /en"""
        langs = ["zh-tw", "zh-cn", "en"]
        for lang in langs:
            url = f"/{lang}/"
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 200,
                f"{lang} 語言首頁測試失敗"
            )
