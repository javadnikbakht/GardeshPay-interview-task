from rest_framework import serializers

from apps.authentication.serializers import UserSerializer
from apps.comments.serializers import CommentSerializer
from apps.tweets.models import Tweet, TweetLike


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TweetLike
        fields = '__all__'


class TweetSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    retweets_count = serializers.SerializerMethodField()
    likes = LikeSerializer(source='tweetlike_set', many=True, read_only=True)
    comments = CommentSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Tweet
        fields = '__all__'

    @staticmethod
    def get_likes_count(self):
        return self.likes.count()

    @staticmethod
    def get_retweets_count(self):
        return self.retweets.count()


class TweetSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    content = serializers.CharField(required=False)

    class Meta:
        model = Tweet
        fields = ('content', 'image', 'created_at', 'user', 'parent', 'comment', 'image')
        extra_kwargs = {
            'content': {
                'error_messages': {
                    'max_length': "Tweet content is too Long"
                }
            }
        }

    def validate(self, data):
        if 'content' not in data:
            if 'parent' not in data or 'comment' not in data:
                raise serializers.ValidationError(
                    {
                        'message': 'Content is necessary'
                    }
                )

        if 'parent' in data and 'comment' in data:
            raise serializers.ValidationError(
                {
                    'message': 'Retweet only can related to a tweet or comment, not both'
                }
            )

        return data


class ActionSerializer(serializers.Serializer):
    ACTIONS = (
        ('LIKE', 'like'),
        ('UNLIKE', 'unlike'),
    )

    action = serializers.ChoiceField(choices=ACTIONS,
                                     error_messages={'invalid_choice': 'The request action is not valid'})
    content = serializers.CharField(max_length=300, required=False,
                                    error_messages={'max_length': "Tweet content is too Long"})
