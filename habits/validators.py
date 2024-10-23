from rest_framework import serializers

class HabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['is_positive']:
            if value['associated_habit'] or value['reward']:
                raise serializers.ValidationError(
                    'У позитивной привычки не может быть связанной привычки или награды.')
            if value['associated_habit'] and value['reward']:
                raise serializers.ValidationError(
                    'Может быть только одна: либо связанная привычка, либо награда.')
            if value['duration_minutes'] > 5:
                raise serializers.ValidationError(
                    'Продолжительность не может превышать 5 минут.')
            if value['associated_habit']:
                if not value['associated_habit'].is_positive:
                    raise serializers.ValidationError('Связанная привычка также должна быть позитивной.')