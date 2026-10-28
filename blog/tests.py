from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password123')
        self.post = Post.objects.create(
            title='Prueba de Post',
            subtitle='Subtítulo de prueba',
            content='Contenido para testing automatizado.',
            author=self.user
        )

    def test_post_list_view_anonymous(self):
        """El visitante anónimo debe poder ver el listado de posts."""
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prueba de Post')

    def test_post_detail_view_anonymous(self):
        """El visitante anónimo puede ver el detalle de un post."""
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contenido para testing automatizado.')

    def test_post_create_protected(self):
        """Un usuario anónimo debe ser redirigido al intentar crear un post."""
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_post_create_authenticated(self):
        """Un usuario autenticado puede crear un post vía formulario."""
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('blog:post_create'), {
            'title': 'Nuevo post creado por test',
            'subtitle': 'Subtítulo',
            'content': 'Contenido válido',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Nuevo post creado por test').exists())

    def test_search_posts(self):
        """El motor de búsqueda debe filtrar correctamente por título o contenido."""
        response = self.client.get(reverse('blog:post_list') + '?q=automatizado')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prueba de Post')

        # Búsqueda que no arroja resultados
        response_empty = self.client.get(reverse('blog:post_list') + '?q=inexistenteXYZ')
        self.assertEqual(response_empty.status_code, 200)
        self.assertContains(response_empty, 'No se encontraron publicaciones')
