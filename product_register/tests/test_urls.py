"""URLs Tests"""
from django.urls import reverse, resolve

# Create your tests here.

class TestUrls:
    """Classe para Tetses de URL"""
    def test_product_list_url(self):
        """Função para Testar a URL product_list"""
        path = reverse('product_list')
        assert resolve(path).view_name == 'product_list'

    def test_product_insert_url(self):
        """Função para Testar a URL product_insert"""
        path = reverse('product_insert')
        assert resolve(path).view_name == 'product_insert'

    def test_product_update_url(self):
        """Função para Testar a URL product_update"""
        path = reverse('product_update', kwargs = {'product_id':1})
        assert resolve(path).view_name == 'product_update'

    def test_product_delete_url(self):
        """Função para Testar a URL product_delete"""
        path = reverse('product_delete', kwargs = {'product_id':1})
        assert resolve(path).view_name == 'product_delete'

    def test_category_insert_url(self):
        """Função para Testar a URL category_insert"""
        path = reverse('category_insert')
        assert resolve(path).view_name == 'category_insert'
