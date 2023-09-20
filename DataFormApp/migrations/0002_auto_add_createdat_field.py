operations = [
    migrations.CreateModel(
        name='Contribution',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ('contributor_email', models.EmailField(max_length=254)),
            ('createdAt', models.DateTimeField(auto_now_add=True)),  # Add this line
        ],
    ),
]
