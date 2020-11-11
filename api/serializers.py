from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator

from .models import Comment, Review, Title, Category, Genre


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    score = serializers.IntegerField(min_value=1, max_value=10)

    def validate(self, data):
        action = self.context['view'].action
        if action == 'create':
            author = self.context['request'].user
            title = get_object_or_404(
                Title, id=self.context['view'].kwargs['title_id'])
            if title.reviews.filter(author=author).exists():
                raise ValidationError("You can't review same title twice")
        return super(ReviewSerializer, self).validate(data)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        required_fields = ('text', 'score')
        read_only_fields = ('id', 'author')
        model = Review


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        max_length=50, validators=[UniqueValidator(
            queryset=Category.objects.all())])

    class Meta:
        exclude = ('id', )
        lookup_field = 'slug'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        lookup_field = 'slug'
        model = Genre


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)

    class Meta:
        fields = '__all__'
        model = Title
