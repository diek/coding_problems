# blogapp/management/commands/generate_blog_data.py

import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from blogger.models import Blog, Like


class Command(BaseCommand):
    help = "Generate fake blogs and likes for testing purposes."

    def add_arguments(self, parser):
        parser.add_argument(
            "--blogs", type=int, default=10, help="Number of blogs to create"
        )
        parser.add_argument(
            "--likes", type=int, default=20, help="Number of likes to create"
        )

    def handle(self, *args, **kwargs):
        faker = Faker()

        num_blogs = kwargs["blogs"]
        num_likes = kwargs["likes"]
        User = get_user_model()
        users = list(User.objects.all())
        if not users:
            self.stdout.write(
                self.style.ERROR(
                    "No users found. Please create users before running this script."
                )
            )
            return

        # Generate Blogs
        blogs = []
        for _ in range(num_blogs):
            author = random.choice(users)
            title = faker.sentence(nb_words=6)
            content = faker.paragraph(nb_sentences=5)

            blog = Blog.objects.create(title=title, content=content, author=author)
            blogs.append(blog)
            self.stdout.write(f'Created blog: "{title}" by {author.first_name}')

        # Generate Likes
        for _ in range(num_likes):
            user = random.choice(users)
            blog = random.choice(blogs)

            # Prevent duplicate likes
            if not Like.objects.filter(user=user, blog=blog).exists():
                Like.objects.create(user=user, blog=blog)
                self.stdout.write(f'{user.first_name} liked "{blog.title}"')
            else:
                self.stdout.write(
                    f'{user.first_name} already liked "{blog.title}", skipping.'
                )

        self.stdout.write(
            self.style.SUCCESS(f"Generated {len(blogs)} blogs and {num_likes} likes.")
        )
